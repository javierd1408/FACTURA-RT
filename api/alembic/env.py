from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os


config = context.config
section = config.config_ini_section
config.set_section_option(section, "POSTGRES_USER", os.getenv("POSTGRES_USER", "app"))
config.set_section_option(section, "POSTGRES_PASSWORD", os.getenv("POSTGRES_PASSWORD", "app_password_change_me"))
config.set_section_option(section, "POSTGRES_HOST", os.getenv("POSTGRES_HOST", "db"))
config.set_section_option(section, "POSTGRES_PORT", os.getenv("POSTGRES_PORT", "5432"))
config.set_section_option(section, "POSTGRES_DB", os.getenv("POSTGRES_DB", "facturas"))


if config.config_file_name is not None:
fileConfig(config.config_file_name)


target_metadata = None # usaremos autogenerate cuando definamos modelos


def run_migrations_offline():
url = config.get_main_option("sqlalchemy.url")
context.configure(url=url, literal_binds=True)
with context.begin_transaction():
context.run_migrations()


def run_migrations_online():
connectable = engine_from_config(
config.get_section(config.config_ini_section),
prefix="sqlalchemy.",
poolclass=pool.NullPool,
)
with connectable.connect() as connection:
context.configure(connection=connection, target_metadata=target_metadata)
with context.begin_transaction():
context.run_migrations()


if context.is_offline_mode():
run_migrations_offline()
else:
run_migrations_online()