
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from Crud.Subquerycrud import SubqueryCRUD

def NovoSubquery(prefix:str, content:str, suffix:str):
    novo = SubqueryCRUD.criar(prefix, content, suffix)
    print("Criado:", novo)
    return novo.id

# Buscar
def GetSubqueryId(Id:int):
    buscado = SubqueryCRUD.buscar_por_id(Id)
    print("Buscado:", buscado)

# Atualizar
def UpdateSubquery(Id:int,prefix:str, content:str, suffix:str):
    atualizado = SubqueryCRUD.atualizar(Id, prefix, content, suffix)
    print("Atualizado:", atualizado)

# Listar todos
def GetAllSubquery():
    print("Todos:", SubqueryCRUD.listar_todos())

# Deletar
def DeleteSubquery(Id:int):
    SubqueryCRUD.deletar(Id)
    print("Depois de deletar:", SubqueryCRUD.buscar_por_id(Id))

def testSubquery():
    Id = NovoSubquery("","em","")
    GetSubqueryId(Id);
    UpdateSubquery(Id,"","perto de","");
    GetAllSubquery();
    DeleteSubquery(Id)
    GetAllSubquery();
    
testSubquery()