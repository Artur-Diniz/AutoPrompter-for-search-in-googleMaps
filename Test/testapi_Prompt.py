
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis 

from Crud.Promptcrud import PromptCRUD
from datetime import datetime


def NovoPrompt(Query: str, id_Subquery: int, id_Categoria: int, id_Local: int, adicionadoIn: datetime, contatosGerados):
    novo = PromptCRUD.criar(Query, id_Subquery, id_Categoria, id_Local, adicionadoIn, contatosGerados)
    print("Criado:", novo)
    return novo.id

def autogenarte(id_Subquery: int, id_Categoria: int, id_Local: int, ):
    novo = PromptCRUD.autogenarte(id_Subquery, id_Categoria, id_Local)
    print("Criado:", novo)
    return novo.id

# Buscar
def GetPromptId(Id:int):
    buscado = PromptCRUD.buscar_por_id(Id)
    print("Buscado:", buscado)
    
    
def Get_prompt_novo():
    buscado = PromptCRUD.buscar_query_novo_mais_antiga()
    if buscado == False:
        print("Sem Propmts Disponiveis")
    else:
     print(buscado)
    return buscado


def GetDuplicate(id_Subquery: int,id_categoria:int,id_local:int):
    if PromptCRUD.buscar_por_Idquery_Idcategoria_IdLocal(id_Subquery,id_categoria,id_local):
         print("foi true")
    else:
         print("foi else")
        


# Atualizar
def UpdatePrompt(Id:int, Query: str, id_Subquery: int, id_Categoria: int, id_Local: int, adicionadoIn: datetime, contatosGerados):
    atualizado = PromptCRUD.atualizar(Id, Query, id_Subquery, id_Categoria, id_Local, adicionadoIn, contatosGerados)
    print("Atualizado:", atualizado)

def UpdateUso(id:int,contatosGerados:int):
    PromptCRUD.atualizar_Usado(id,contatosGerados)

# Listar todos
def GetAllPrompt():
    print("Todos:", PromptCRUD.listar_todos())


# Deletar
def DeletePrompt(Id:int):
    PromptCRUD.deletar(Id)
    print("Depois de deletar:", PromptCRUD.buscar_por_id(Id))


def testPrompt():
    data_agr=datetime.now()
    Id = NovoPrompt("Barbearia em São Paulo", 2, 4, 9, data_agr, 0)
    GetPromptId(Id);
    UpdatePrompt(Id, "Melhores Barbearias em São Paulo", 3,  4, 9, data_agr, 25);
    GetAllPrompt();
    DeletePrompt(Id)
    GetAllPrompt();
    
    
# testPrompt()

def testAutogeneratePrompt(subquery=1,Categoria=1,Local=1):    
    Id=autogenarte(subquery,Categoria,Local)
    GetPromptId(Id);    


# testAutogeneratePrompt();

newprompt=Get_prompt_novo()
UpdateUso(newprompt.id,1)
GetAllPrompt();
