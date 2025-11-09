

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
    
#busca primeira caregoria com prioridade 5 do menor id para o maior
def get_primeiro_categoria_com_prioridade_5():
    buscado = CategoriaCRUD.buscar_primeiro_categoria_com_prioridade_5()
    print("Buscado:", buscado)
    
def get_utlima_categoria_Id():
    buscado = CategoriaCRUD.buscar_utlima_categoria_Id()
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

# get_primeiro_categoria_com_prioridade_5()

# get_utlima_categoria_Id()