
from Crud.Categoriacrud import CategoriaCRUD
from Crud.Localcrud import LocalCRUD
from Crud.Subquerycrud import SubqueryCRUD


# Criar
def NovoCategoria(categoria:str, prioridade:int):
    novo = CategoriaCRUD.criar(categoria, prioridade)
    print("Criado:", novo)
    return novo.id

# Buscar
def GetCategoriaId(Id:int):
    buscado = CategoriaCRUD.buscar_por_id(Id)
    print("Buscado:", buscado)

# Atualizar
def UpdateCategoria(Id:int, categoria:str, prioridade:int):
    atualizado = CategoriaCRUD.atualizar(Id, categoria, prioridade)
    print("Atualizado:", atualizado)

# Listar todos
def GetAllCategoria():
    print("Todos:", CategoriaCRUD.listar_todos())

# Deletar
def DeleteCategoria(Id:int):
    CategoriaCRUD.deletar(Id)
    print("Depois de deletar:", CategoriaCRUD.buscar_por_id(Id))

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


def testCategoria():
    Id = 0
    Id = NovoCategoria("Clínicas odontológicas",1)
    GetCategoriaId(Id);
    UpdateCategoria(Id,"Clínicas odontológica",1);
    GetAllCategoria();
    DeleteCategoria(Id)
    GetAllCategoria();

def testLocal():
    Id = 0
    Id = NovoLocal("Osascoquence","")
    GetLocalId(Id);
    UpdateLocal(Id,"Guarulhos","");
    GetAllLocal();
    DeleteLocal(Id)
    GetAllLocal();

def testSubquery():
    Id = 0
    Id = NovoSubquery("","em","")
    GetSubqueryId(Id);
    UpdateSubquery(Id,"","perto de","");
    GetAllSubquery();
    DeleteSubquery(Id)
    GetAllSubquery();


testSubquery()

