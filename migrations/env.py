from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from server.src.config import settings
from server.src.models import Base
from server.src.models.service import Service  # noqa
from server.src.models.user import User  # noqa

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

config.set_main_option('PG_USER', settings.PG_USER)
config.set_main_option('PG_PASS', settings.PG_PASS)
config.set_main_option('PG_HOST', settings.PG_HOST)
config.set_main_option('PG_PORT', settings.PG_PORT)
config.set_main_option('PG_BASE', settings.PG_BASE)


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
