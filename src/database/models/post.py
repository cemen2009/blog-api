from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Float, Text, DECIMAL, ForeignKey  # they're added just in case

from src.database import Base, CommentModel


# TODO: implement enum for comment limitation: everyone/only people i follow/nobody


class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, unique=False, nullable=True)
    likes: Mapped[int] = mapped_column(nullable=False)
    hide_likes: Mapped[bool] = mapped_column(nullable=False)

    comments: Mapped[list[CommentModel]] = relationship(
        "CommentModel",
        secondary=...,
        back_populates="posts",
    )

    # need to implement enum first
    # limit_comments: Mapped[limitation_enum] = ...

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["UserModel"] = relationship("UserModel", back_populates="posts")
