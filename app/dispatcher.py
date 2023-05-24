from fastapi import FastAPI
from app.handlers import router as handlers_router


def dispatcher(context):
    app = FastAPI()
    app.include_router(router=handlers_router, prefix="/api")

    @app.get("/")
    async def root():
        return {
            "file": __name__,
            "upd": context["upd"],
            "build": context["build"],
            "start_time": context["start_time"],
        }

    return app
