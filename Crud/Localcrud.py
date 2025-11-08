
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Db.db import SessionLocal
from Models.Local import Local


class LocalCRUD:

    @staticmethod
    def criar(cidade: str, bairro: str=None):
        session = SessionLocal()
        novo = Local(cidade=cidade, bairro=bairro)
        session.add(novo)
        session.commit()
        session.refresh(novo)  # garante que os dados estão carregados
        session.expunge(novo)  # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(local_id: int):
        session = SessionLocal()
        local = session.query(Local).filter_by(id=local_id).first()
        if local:
            session.expunge(local)  # tira da sessão
        session.close()
        return local

    @staticmethod
    def listar_todos():
        session = SessionLocal()
        locais = session.query(Local).all()
        for l in locais:
            session.expunge(l)  # tira cada objeto da sessão
        session.close()
        return locais

    @staticmethod
    def atualizar(local_id: int, cidade: str, bairro: str):
        session = SessionLocal()
        try:
            local = session.query(Local).filter_by(id=local_id).first()
            if not local:
                return None  # não encontrou o registro

            local.cidade = cidade
            local.bairro = bairro
            session.commit()

            # garante que os dados estão carregados antes de fechar
            session.refresh(local)
            session.expunge(local)
            return local
        finally:
            session.close()

    @staticmethod
    def deletar(local_id: int):
        session = SessionLocal()
        local = session.query(Local).filter_by(id=local_id).first()
        if local:
            session.delete(local)
            session.commit()
        session.close()
