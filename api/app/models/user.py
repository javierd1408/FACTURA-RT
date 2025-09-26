from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
__tablename__ = "users"
id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
nombre: Mapped[str] = mapped_column(String(100))
apellido: Mapped[str] = mapped_column(String(100))
username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
password_hash: Mapped[str] = mapped_column(String(255))
role: Mapped[str] = mapped_column(String(20), default="ANALISTA")
mfa_enabled: Mapped[bool] = mapped_column(Boolean, default=False)