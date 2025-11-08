
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, Integer, String,DateTime
from Db.db import Base


class Prompt(Base):
    
    __tablename__="query_prompt"

    id = Column(Integer, primary_key=True, autoincrement=True)
    query = Column(String, nullable=False)
    id_Subquery = Column(Integer, nullable=False)
    id_Categoria = Column(Integer, nullable=False)
    id_Local = Column(Integer, nullable=False)
    adicionadoIn = Column(DateTime, nullable=False)
    contatosGerados = Column(Integer)

    def __repr__(self):
        return f"<Prompt id={self.id}, query='{self.query}', id_Subquery='{self.id_Subquery}', id_Categoria='{self.id_Categoria}', id_Local='{self.id_Local}', adicionadoIn='{self.adicionadoIn}', contatosGerados='{self.contatosGerados}'>"
        
    def __str__(self):
        return f"<Prompt id={self.id}, query='{self.query}', id_Subquery='{self.id_Subquery}', id_Categoria='{self.id_Categoria}', id_Local='{self.id_Local}', adicionadoIn='{self.adicionadoIn}', contatosGerados='{self.contatosGerados}'>"
        
