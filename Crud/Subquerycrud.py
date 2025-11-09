
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Db.db import SessionLocal
from Models.Subquery import Subquery


class SubqueryCRUD:

    @staticmethod
    def criar(prefix: str=None, content: str=None, suffix: str=None):
        """ serve para estrutara o gerador de prompts
            query = f"{subquery.prefix} {categoria.categoria} {subquery.content} {local.cidade} {subquery.suffix}"

        Args:
            prefix (str, optional): [prefixo]. Defaults to None.
            content (str, optional): [conteudo]. Defaults to None.
            suffix (str, optional): [sifixo]. Defaults to None.

        Returns:
            [type]: [Subquery classe]
        """
        session = SessionLocal()
        novo = Subquery(prefix=prefix, content=content, suffix=suffix)
        session.add(novo)
        session.commit()
        session.refresh(novo)  # garante que os dados estão carregados
        session.expunge(novo)  # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(subquery_id: int):
        """ get ID
        Args:
            subquery_id (int): [get Id]

        Returns:
            [type]: [Subquery]
        """
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            session.expunge(subquery)  # tira da sessão
        session.close()
        return subquery

    @staticmethod
    def listar_todos():
        """Get all basico

        Returns:
            [subquery[]]: [todos os query do banco]
        """
        session = SessionLocal()
        subquery = session.query(Subquery).all()
        for l in subquery:
            session.expunge(l)  # tira cada objeto da sessão
        session.close()
        return subquery

    @staticmethod
    def atualizar(subquery_id: int, prefix: str, content: str, suffix: str):
        """ Update geral

        Args:
            subquery_id (int): [Id]
            prefix (str): [prefix]
            content (str): [content]
            suffix (str): [suffix]

        Returns:
            [subquery]
        """
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            subquery.prefix = prefix
            subquery.content = content
            subquery.suffix = suffix
            session.commit()
            session.refresh(subquery)  # atualiza os dados
            session.expunge(subquery)  # tira da sessão
        session.close()
        return subquery

    @staticmethod
    def deletar(subquery_id: int):
        """ Deleta com base no ID

        Args:
            subquery_id (int): [Subquery ID]
        """
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            session.delete(subquery)
            session.commit()
        session.close()
        
