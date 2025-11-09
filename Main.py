import sys
from pathlib import Path
import random
from datetime import datetime

sys.path.append(str(Path(__file__).parent.parent))

from Crud.Promptcrud import PromptCRUD
from Crud.Localcrud import LocalCRUD
from Crud.Categoriacrud import CategoriaCRUD


def Main():
    lastPrompt = PromptCRUD.buscar_ultimo()
    categoria = 1 
    local = 1

    subqueries = random.sample(range(1, 14), 4)

    ultima_categoria = CategoriaCRUD.buscar_utlima_categoria_Id()
    categoria_prioridade_5 = CategoriaCRUD.buscar_primeiro_categoria_com_prioridade_5()

    if lastPrompt:
        categoria = lastPrompt.id_Categoria
        local = lastPrompt.id_Local

        # 🧩 Caso chegue na última categoria do banco
        if ultima_categoria and categoria == ultima_categoria.id:
            proximo_local = LocalCRUD.buscar_por_id(local + 1)

            if proximo_local:
                local = proximo_local.id
            else:
                # 🔴 Nenhum próximo local — significa que terminou tudo
                raise RuntimeError(
                    f"🚨 Fim de execução: atingido último local ({local}) e última categoria ({categoria})."
                )

            if categoria_prioridade_5:
                categoria = categoria_prioridade_5.id
            else:
                categoria = 1

        else:
            # fluxo normal
            proxima_categoria = CategoriaCRUD.buscar_por_id(categoria + 1)

            if proxima_categoria:
                if proxima_categoria.prioridade <= 4:
                    categoria = proxima_categoria.id
                else:
                    # próxima categoria é prioridade >=5 → muda local
                    proximo_local = LocalCRUD.buscar_por_id(local + 1)
                    if proximo_local:
                        local = proximo_local.id
                    else:
                        # 🔴 acabou locais, erro controlado
                        raise RuntimeError(
                            f"🚨 Fim de execução: atingido último local ({local}) sem próximo disponível."
                        )

                    categoria = 1
            else:
                # acabou categorias → tenta avançar local
                proximo_local = LocalCRUD.buscar_por_id(local + 1)
                if proximo_local:
                    local = proximo_local.id
                    categoria = 1
                else:
                    # 🔴 Sem categorias nem locais → encerra
                    raise RuntimeError(
                        f"🚨 Fim de execução: atingido último local ({local}) e última categoria ({categoria})."
                    )

    for subquery in subqueries:
        novo = PromptCRUD.autogenarte(subquery, categoria, local)
        print(
            f"[{datetime.now()}] Gerado: {novo.query} (cat={categoria}, local={local}, sub={subquery})"
        )

    return True


if __name__ == "__main__":
    try:
        Main()
    except RuntimeError as e:
        print(str(e))
        print("⛔ Encerrando execução por limite máximo atingido.")
        sys.exit(1)
