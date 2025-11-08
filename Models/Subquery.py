from sqlalchemy import Column, Integer, String, Text
from Db.db import Base

class Subquery(Base):
    __tablename__ = "sub_query"

    id = Column(Integer, primary_key=True, autoincrement=True)
    prefix = Column(String(100))
    content = Column(Text)
    suffix = Column(String(100))

    def __repr__(self):
        return f"<Subquery id={self.id}, prefix='{self.prefix}', content='{self.content}', suffix='{self.suffix}'>"

    def __str__(self):
        return f"Subquery(id={self.id}, prefix='{self.prefix}', content='{self.content}', suffix='{self.suffix}')"