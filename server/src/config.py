import functools

from pydantic import BaseSettings


class Settings(BaseSettings):
    PG_USER: str = "postgres"
    PG_PASS: str = "postgres"
    PG_HOST: str = "localhost"
    PG_PORT: str = "5432"
    PG_BASE: str = "mo_cloud"

    BIND_HOST: str = "127.0.0.1"
    BIND_PORT: str = "8000"

    @functools.cached_property
    def db_url(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_BASE}"

    class Config:
        keep_untouched = (functools.cached_property,)


settings = Settings()
