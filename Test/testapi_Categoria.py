

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from Crud.Categoriacrud import CategoriaCRUD


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
    
    
def testCategoria():
    Id = NovoCategoria("Clínicas odontológicas", 1)
    GetCategoriaId(Id);
    UpdateCategoria(Id, "Clínicas odontológica", 1);
    GetAllCategoria();
    DeleteCategoria(Id)
    GetAllCategoria();
