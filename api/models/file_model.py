from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class File(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bucket: str
    etag: str