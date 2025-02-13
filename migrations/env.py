import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from app.main.config import DevelopmentConfig as Config
from app.main import db, create_app


config = context.config

database_url = os.getenv("DATABASE_URL", Config.SQLALCHEMY_DATABASE_URI)
config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = db.metadata

def run_migrations_offline() -> None:
    """Executa as migrações em modo offline."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações em modo online, conectando ao banco."""
    engine = create_engine(database_url, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
