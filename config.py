from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    DB_NAME: str
    GENRE_PATH: str
    IMAGES_PATH: str

    class Config:
        env_file = "D:/diplom_kartigo/diplom_kartigo/.env"


settings = Settings()
