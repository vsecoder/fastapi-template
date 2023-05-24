import asyncio
import logging
import git
import uvicorn

import coloredlogs

from app import db, version
from app.arguments import parse_arguments
from app.config import Config, parse_config
from app.db import close_orm, init_orm

from app.dispatcher import dispatcher

from datetime import datetime


async def on_startup(
    disp, loop, config: Config, **kwargs
):
    tortoise_config = config.database.get_tortoise_config()
    await init_orm(tortoise_config)

    #logging.info(f"None - {None}")

    web_config = config.web.get_config()
    
    logging.error("Started!")

    uvicorn.run(
        disp,
        host=web_config["host"],
        port=web_config["port"],
        #log_level=web_config["log_level"],
        #loop=loop
    )


async def on_shutdown(config: Config):
    logging.warning("Stopping...")
    await close_orm()


async def main(loop):
    coloredlogs.install(level=logging.INFO)
    logging.warning("Starting...")

    arguments = parse_arguments()
    config = parse_config(arguments.config)

    tortoise_config = config.database.get_tortoise_config()
    try:
        await db.create_models(tortoise_config)
    except FileExistsError:
        await db.migrate_models(tortoise_config)

    repo = git.Repo()
    build = repo.heads[0].commit.hexsha
    diff = repo.git.log([f"HEAD..origin/{version.branch}", "--oneline"])
    upd = "Update required" if diff else "Up-to-date"

    start_time = datetime.now()

    context_kwargs = {"build": build, "upd": upd, "start_time": start_time}

    disp = dispatcher(context_kwargs)

    await on_startup(disp, loop, config, **context_kwargs)


if __name__ == "__main__":
    try:
        asyncio.run(main(asyncio.get_event_loop()))
    except (KeyboardInterrupt, SystemExit):
        asyncio.run(on_shutdown())
        logging.error("Stopped!")
