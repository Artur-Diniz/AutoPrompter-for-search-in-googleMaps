from Db.db import SessionLocal, engine, Base
from Models.Local import Local

# Criar tabelas no banco (se não existirem)
Base.metadata.create_all(bind=engine)

class LocalRepository:

    @staticmethod
    def salvar(local: Local):
        session = SessionLocal()
        session.add(local)
        session.commit()
        session.refresh(local)  # atualiza o objeto com o ID gerado
        session.close()
        return local

    @staticmethod
    def buscar_por_id(local_id: int):
        session = SessionLocal()
        local = session.query(Local).filter_by(Id=local_id).first()
        session.close()
        return local

    @staticmethod
    def listar_todos():
        session = SessionLocal()
        locais = session.query(Local).all()
        session.close()
        return locais

    @staticmethod
    def atualizar(local: Local):
        session = SessionLocal()
        session.merge(local)  # atualiza o objeto existente
        session.commit()
        session.close()

    @staticmethod
    def deletar(local_id: int):
        session = SessionLocal()
        local = session.query(Local).filter_by(Id=local_id).first()
        if local:
            session.delete(local)
            session.commit()
        session.close()