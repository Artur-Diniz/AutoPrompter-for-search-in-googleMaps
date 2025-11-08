from Db.db import SessionLocal
from Models.Categoria import Categoria

class CategoriaCRUD:

    @staticmethod
    def criar(categoria: str, prioridade: int = None):
        session = SessionLocal()
        novo = Categoria(categoria=categoria, prioridade=prioridade)
        session.add(novo)
        session.commit()
        session.refresh(novo)      # garante que os dados estão carregados
        session.expunge(novo)      # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(Categoria_id: int):
        session = SessionLocal()
        categoria = session.query(Categoria).filter_by(id=Categoria_id).first()
        if categoria:
            session.expunge(categoria)  # tira da sessão
        session.close()
        return categoria

    @staticmethod
    def listar_todos():
        session = SessionLocal()
        locais = session.query(Categoria).all()
        for l in locais:
            session.expunge(l)      # tira cada objeto da sessão
        session.close()
        return locais

    @staticmethod
    def atualizar(Categoria_id: int, cat: str, prioridade: int):
        session = SessionLocal()
        categoria = session.query(Categoria).filter_by(id=Categoria_id).first()
        if categoria:
            categoria.categoria = cat
            categoria.prioridade = prioridade
            session.commit()
            session.refresh(categoria)   # atualiza os dados
            session.expunge(categoria)   # tira da sessão
        session.close()
        return categoria

    @staticmethod
    def deletar(Categoria_id: int):
        session = SessionLocal()
        categoria = session.query(Categoria).filter_by(id=Categoria_id).first()
        if categoria:
            session.delete(categoria)
            session.commit()
        session.close()