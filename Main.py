import sys
from pathlib import Path
import random

sys.path.append(str(Path(__file__).parent.parent))

from Crud.Promptcrud import PromptCRUD
from Crud.Localcrud import LocalCRUD
from Crud.Categoriacrud import CategoriaCRUD


def Main():
    lastPrompt = PromptCRUD.buscar_ultimo()

    categoria = 1
    local = 1
    subqueries = random.sample(range(1, 14), 4)


    if lastPrompt:
        categoria = lastPrompt.id_Categoria
        local = lastPrompt.id_Local  

        proxima_categoria = CategoriaCRUD.buscar_por_id(categoria + 1)

        if proxima_categoria:
            #  Caso ainda esteja nas categorias de prioridade até 4 → continua no mesmo local
            if proxima_categoria.prioridade <= 4:
                categoria = proxima_categoria.id
            else:
                # Caso a prioridade seja >=5 → muda de local e reseta categoria para 1
                local += 1
                categoria = 1
        else:
            # Se acabou as categorias → vai para próximo local
            local += 1
            categoria = 1

        #  Caso não existam mais locais → reinicia locais e muda para categorias de prioridade >=5
        proximo_local = LocalCRUD.buscar_por_id(local)
        if not proximo_local:
                    # Se acabou os locais → reinicia locais e começa nas categorias de prioridade >=5
                    local = 1
                    categoria_prioridade_5 = CategoriaCRUD.buscar_primeiro_categoria_com_prioridade_5()

                    if categoria_prioridade_5:
                        categoria = categoria_prioridade_5.id
               


    for subquery in subqueries:
        novo = PromptCRUD.autogenarte(subquery, categoria, local)
        print(novo)

    return True


Main()
