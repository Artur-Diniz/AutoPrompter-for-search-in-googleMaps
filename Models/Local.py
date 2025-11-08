from sqlalchemy import Column, Integer, String
from Db.db import Base

class Local(Base):
    __tablename__ = "local"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cidade = Column(String, nullable=False)
    bairro = Column(String)

    def __repr__(self):
        return f"<Local id={self.id}, cidade='{self.cidade}', bairro='{self.bairro}'>"

    def __str__(self):
        return f"Local(id={self.id}, cidade='{self.cidade}', bairro='{self.bairro}')"