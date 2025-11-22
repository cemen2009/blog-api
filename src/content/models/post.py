from enum import Enum

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Float, Text, DECIMAL, ForeignKey, Table, Column  # they're added just in case
from sqlalchemy import Enum as SQLAlchemyEnum

from database import Base


# TODO: implement enum for comment limitation: everyone/only people i follow/nobody
class CommentLimitationEnum(str, Enum):
    EVERYONE = "Everyone can comment"
    FOLLOWING = "Only people you follow can comment"
    NOBODY = "Nobody can comment"


PostsCommentsModel = Table(
    "posts_comments",
    Base.metadata,
    Column(
        "post_id",
        ForeignKey("post.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "comment_id",
        ForeignKey("comment.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )
)


class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, unique=False, nullable=True)
    likes: Mapped[int] = mapped_column(nullable=False)
    # not implemented feature
    # hide_likes_count: Mapped[bool] = mapped_column(nullable=False)

    comments: Mapped[list["CommentModel"]] = relationship(
        "CommentModel",
        secondary=PostsCommentsModel,
        back_populates="posts",
    )
    # NIF
    # limit_comments: Mapped[CommentLimitationEnum] = mapped_column(SQLAlchemyEnum(), nullable=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["UserModel"] = relationship("UserModel", back_populates="posts")
