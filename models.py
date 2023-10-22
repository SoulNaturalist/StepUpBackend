from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    password: str
    email: str

class LoginUserData(BaseModel):
    email: str
    password: str

class StepsData(BaseModel):
    count_steps: int


class LogConfig(BaseModel):

    LOGGER_NAME: str = "step_up_application"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }