import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

from Crud.Localcrud import LocalCRUD


def NovoLocal(Cidade:str, Bairro):
    novo = LocalCRUD.criar(Cidade, Bairro)
    print("Criado:", novo)
    return novo.id


# Buscar
def GetLocalId(Id:int):
    buscado = LocalCRUD.buscar_por_id(Id)
    print("Buscado:", buscado)


# Atualizar
def UpdateLocal(Id:int, Cidade:str, Bairro:str):
    atualizado = LocalCRUD.atualizar(Id, Cidade, Bairro)
    print("Atualizado:", atualizado)


# Listar todos
def GetAllLocal():
    print("Todos:", LocalCRUD.listar_todos())


# Deletar
def DeleteLocal(Id:int):
    LocalCRUD.deletar(Id)
    print("Depois de deletar:", LocalCRUD.buscar_por_id(Id))


def testLocal():
    Id = NovoLocal("Osascoquence", "")
    GetLocalId(Id);
    UpdateLocal(Id, "Guarulhos", "");
    GetAllLocal();
    DeleteLocal(Id)
    GetAllLocal();
    
GetAllLocal();
