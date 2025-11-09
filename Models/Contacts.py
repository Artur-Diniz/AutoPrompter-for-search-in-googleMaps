
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, Integer, String,DateTime,Boolean,Float
from Db.db import Base


class Contacts(Base):    
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_categoria = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)
    num_fone = Column(Integer, nullable=False)
    endereco = Column(String, nullable=False)
    num_fone = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    ddd = Column(Integer, nullable=False)
    whatsapp = Column(Boolean, default=False)
    site_proprio = Column(Boolean, default=False)  
    website = Column(String, nullable=False)
    abre_em = Column(String, nullable=False)
    num_reviews = Column(Integer, nullable=False)
    nota_review = Column(Float, nullable=False)
    loja_fisica = Column(Boolean, default=False)  
    retirada_local = Column(Boolean, default=False)  
    delivery = Column(Boolean, default=False)  
    data_coleta = Column(DateTime, nullable=False) 
    ativo = Column(Boolean, default=True)  
    
    
    

    def __repr__(self):
        return f"<Prompt id={self.id},id_categoria='{self.id_categoria}',nome='{self.nome}',num_fone='{self.num_fone}',endereco='{self.endereco}',cidade='{self.cidade}',bairro='{self.bairro}',cep='{self.cep}',ddd='{self.ddd}',whatsapp='{self.whatsapp}',site_proprio='{self.site_proprio}',website='{self.website}',abre_em='{self.abre_em}',num_reviews='{self.num_reviews}',nota_review='{self.nota_review}',loja_fisica='{self.loja_fisica}',retirada_local='{self.retirada_local}',delivery='{self.delivery}',data_coleta='{self.data_coleta}',ativo='{self.ativo}'>"
        
    def __str__(self):
        return f"<Prompt id={self.id},id_categoria='{self.id_categoria}',nome='{self.nome}',num_fone='{self.num_fone}',endereco='{self.endereco}',cidade='{self.cidade}',bairro='{self.bairro}',cep='{self.cep}',ddd='{self.ddd}',whatsapp='{self.whatsapp}',site_proprio='{self.site_proprio}',website='{self.website}',abre_em='{self.abre_em}',num_reviews='{self.num_reviews}',nota_review='{self.nota_review}',loja_fisica='{self.loja_fisica}',retirada_local='{self.retirada_local}',delivery='{self.delivery}',data_coleta='{self.data_coleta}',ativo='{self.ativo}'>"
        
