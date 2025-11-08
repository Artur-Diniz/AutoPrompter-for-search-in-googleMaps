from Db.db import SessionLocal
from Models.Prompt import Prompt
from Models.Subquery import Subquery
from Models.Local import Local
from Models.Categoria import Categoria
from datetime import datetime


class PromptCRUD:

    @staticmethod
    def criar(query: str, id_Subquery: int, id_Categoria: int, id_Local: int, adicionadoIn: datetime, contatosGerados:int):
        """AI is creating summary for criar

        Args:
            query (str): [description]
            id_Subquery (int): [description]
            id_Categoria (int): [description]
            id_Local (int): [description]
            adicionadoIn (datetime): [description]
            contatosGerados (int): [description]

        Returns:
            [type]: [description]1
        """
        session = SessionLocal()
        novo = Prompt(query=query, id_Subquery=id_Subquery, id_Categoria=id_Categoria, id_Local=id_Local, adicionadoIn=adicionadoIn, contatosGerados=contatosGerados)
        session.add(novo)
        session.commit()
        session.refresh(novo)  # garante que os dados estão carregados
        session.expunge(novo)  # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def autogenarte(id_Subquery: int, id_Categoria: int, id_Local: int,):
        """AI is creating summary for criar

        Args:
            query (str): [description]
            id_Subquery (int): [description]
            id_Categoria (int): [description]
            id_Local (int): [description]
            adicionadoIn (datetime): [description]
            contatosGerados (int): [description]

        Returns:
            [type]: [description]1
        """     
        
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=id_Subquery).first()
        categoria = session.query(Categoria).filter_by(id=id_Categoria).first()
        local = session.query(Local).filter_by(id=id_Local).first()
        query = ''
    
            
        if local.bairro == ""or local.bairro == None:
            query = f"{subquery.prefix} {categoria.categoria} {subquery.content} {local.cidade} {subquery.suffix}"
        else:
            query = f"{subquery.prefix} {categoria.categoria} {subquery.content} {local.bairro} {subquery.suffix}"        
            
        query = query.replace("None ", "").replace(" None","").removeprefix(" ").replace("  ", "")

            
        novo = Prompt(query=query, id_Subquery=id_Subquery, id_Categoria=id_Categoria, id_Local=id_Local, adicionadoIn=datetime.now(), contatosGerados=0)
        session.add(novo)
        session.commit()
        session.refresh(novo)  # garante que os dados estão carregados
        session.expunge(novo)  # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(prompt_id: int):
        """AI is creating summary for buscar_por_id

        Args:
            prompt_id (int): [description]

        Returns:
            [type]: [description]
        """
        session = SessionLocal()
        prompt = session.query(Prompt).filter_by(id=prompt_id).first()
        if prompt:
            session.expunge(prompt)  # tira da sessão
        session.close()
        return prompt

    @staticmethod
    def listar_todos():
        """AI is creating summary for listar_todos

        Returns:
            [type]: [description]
        """
        session = SessionLocal()
        locais = session.query(Prompt).all()
        for l in locais:
            session.expunge(l)  # tira cada objeto da sessão
        session.close()
        return locais

    @staticmethod
    def atualizar(prompt_id:int, query: str, id_Subquery: int, id_Categoria: int, id_Local: int, adicionadoIn: datetime, contatosGerados:int):
        """AI is creating summary for atualizar

        Args:
            prompt_id (int): [description]
            query (str): [description]
            id_Subquery (int): [description]
            id_Categoria (int): [description]
            id_Local (int): [description]
            adicionadoIn (datetime): [description]
            contatosGerados (int): [description]

        Returns:
            [type]: [description]
        """
        session = SessionLocal()
        try:
            prompt = session.query(Prompt).filter_by(id=prompt_id).first()
            if not prompt:
                return None  # não encontrou o registro

            prompt.query = query
            prompt.id_Subquery = id_Subquery
            prompt.id_Categoria = id_Categoria
            prompt.id_Local = id_Local
            prompt.adicionadoIn = adicionadoIn
            prompt.contatosGerados = contatosGerados
            prompt.id_Subquery = id_Subquery
            session.commit()

            # garante que os dados estão carregados antes de fechar
            session.refresh(prompt)
            session.expunge(prompt)
            return prompt
        finally:
            session.close()

    @staticmethod
    def deletar(prompt_id: int):
        session = SessionLocal()
        prompt = session.query(Prompt).filter_by(id=prompt_id).first()
        if prompt:
            session.delete(prompt)
            session.commit()
        session.close()
