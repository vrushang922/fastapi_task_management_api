from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from .database import Base


class Task(Base):

    __tablename__= "tasks"

    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    title: Mapped[str] = mapped_column(String(100), nullable= False)
    description: Mapped[str] = mapped_column(String, nullable = False)
    completed: Mapped[bool] = mapped_column(Boolean, default= False)

    