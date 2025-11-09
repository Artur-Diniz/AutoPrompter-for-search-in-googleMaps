
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from Crud.ContacstsCrud import ContactsCRUD
from datetime import datetime

def NovoContacts( id_categoria: int,
        nome: str,
        num_fone: int,
        endereco: str,
        cidade: str,
        bairro: str,
        cep: str,
        ddd: int,
        whatsapp: bool = False,
        site_proprio: bool = False,
        website: str = "",
        abre_em: str = "",
        num_reviews: int = 0,
        nota_review: float = 0.0,
        loja_fisica: bool = False,
        retirada_local: bool = False,
        delivery: bool = False,
        data_coleta: datetime = None,
        ativo: bool = True):
    
    
    novo = ContactsCRUD.criar(id_categoria,nome,num_fone,endereco,cidade,bairro,cep,
        ddd,whatsapp,site_proprio,website,abre_em,num_reviews,nota_review,loja_fisica,retirada_local,
        delivery,data_coleta,ativo)
    
    print("Criado:", novo)
    return novo.id

# Buscar
def GetContactsId(Id:int):
    buscado = ContactsCRUD.buscar_por_id(Id)
    print("Buscado:", buscado)

# Atualizar
def UpdateContacts( id:int, id_categoria: int,
        nome: str,
        num_fone: int,
        endereco: str,
        cidade: str,
        bairro: str,
        cep: str,
        ddd: int,
        whatsapp: bool = False,
        site_proprio: bool = False,
        website: str = "",
        abre_em: str = "",
        num_reviews: int = 0,
        nota_review: float = 0.0,
        loja_fisica: bool = False,
        retirada_local: bool = False,
        delivery: bool = False,
        data_coleta: datetime = None,
        ativo: bool = True):
    
    
    atualizado = ContactsCRUD.atualizar(id, id_categoria,nome,num_fone,endereco,cidade,bairro,cep,
        ddd,whatsapp,site_proprio,website,abre_em,num_reviews,nota_review,loja_fisica,retirada_local,
        delivery,data_coleta,ativo)
    print("Atualizado:", atualizado)

# Listar todos
def GetAllContacts():
    print("Todos:", ContactsCRUD.listar_todos())

# Deletar
def DeleteContacts(Id:int):
    ContactsCRUD.deletar(Id)
    print("Depois de deletar:", ContactsCRUD.buscar_por_id(Id))

def testContacts():
    Id = NovoContacts(    id_categoria=1,
    nome="Clínica Exemplo",
    num_fone=11987654321,
    endereco="Rua das Flores, Centro",
    cidade="São Paulo",
    bairro="Centro",
    cep="01000-000",
    ddd=11,
    whatsapp=True,
    site_proprio=True,
    website="https://clinicaexemplo.com.br",
    abre_em="08:00",
    num_reviews=120,
    nota_review=4.7,
    loja_fisica=True,
    retirada_local=True,
    delivery=False
)
    GetContactsId(Id);
    UpdateContacts(Id, id_categoria=1,nome="Clínica Exemplo 123",num_fone=11987654321,endereco="Rua das Flores, Centro",
        cidade="São Paulo",bairro="Centro",cep="01000-000",ddd=11,whatsapp=True,site_proprio=True,
    website="https://clinicaexemplo.com.br",abre_em="08:00",num_reviews=120,nota_review=4.7,
    loja_fisica=True,retirada_local=False,delivery=False);
    
    GetAllContacts();
    DeleteContacts(Id)
    GetAllContacts();

# GetAllContacts();

testContacts()