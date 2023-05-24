FROM python:3.8-slim-buster

WORKDIR /fastapi-template

COPY ./ ./

RUN python3 -m pip install -r requirements.txt

# Expose the listening port
EXPOSE 7860

# Run npm start script when container starts
CMD [ "python3", "-m", "app" ]
