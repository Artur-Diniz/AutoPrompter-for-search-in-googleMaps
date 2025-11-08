from sqlalchemy import Column, Integer, String
from Db.db import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), nullable=False)
    prioridade = Column(Integer, default=0)

    def __repr__(self):
        return f"<Categoria id={self.id}, categoria='{self.categoria}', prioridade={self.prioridade}>"

    def __str__(self):
        return f"Categoria(id={self.id}, categoria='{self.categoria}', prioridade={self.prioridade})"