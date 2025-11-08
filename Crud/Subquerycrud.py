from Db.db import SessionLocal
from Models.Subquery import Subquery

class SubqueryCRUD:

    @staticmethod
    def criar(prefix: str = None, content: str = None,suffix: str = None):
        session = SessionLocal()
        novo = Subquery(prefix=prefix, content=content, suffix=suffix)
        session.add(novo)
        session.commit()
        session.refresh(novo)      # garante que os dados estão carregados
        session.expunge(novo)      # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(subquery_id: int):
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            session.expunge(subquery)  # tira da sessão
        session.close()
        return subquery

    @staticmethod
    def listar_todos():
        session = SessionLocal()
        locais = session.query(Subquery).all()
        for l in locais:
            session.expunge(l)      # tira cada objeto da sessão
        session.close()
        return locais

    @staticmethod
    def atualizar(subquery_id: int, prefix: str, content: str,suffix: str):
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            subquery.prefix = prefix
            subquery.content = content
            subquery.suffix = suffix
            session.commit()
            session.refresh(subquery)   # atualiza os dados
            session.expunge(subquery)   # tira da sessão
        session.close()
        return subquery

    @staticmethod
    def deletar(subquery_id: int):
        session = SessionLocal()
        subquery = session.query(Subquery).filter_by(id=subquery_id).first()
        if subquery:
            session.delete(subquery)
            session.commit()
        session.close()