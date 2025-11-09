
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from Db.db import SessionLocal
from Models.Contacts import Contacts
from datetime import datetime


class ContactsCRUD:

    @staticmethod
    def criar(
        id_categoria: int,
        nome: str,
        num_fone: int,
        endereco: str,
        cidade: str,
        bairro: str,
        cep: str,
        ddd: int,
        whatsapp: bool = False,
        site_proprio: bool = False,
        website: str = "",
        abre_em: str = "",
        num_reviews: int = 0,
        nota_review: float = 0.0,
        loja_fisica: bool = False,
        retirada_local: bool = False,
        delivery: bool = False,
        data_coleta: datetime = None,
        ativo: bool = True,
    ):
        
        data_coleta=datetime.now()
        """ serve para estrutara o gerador de prompts
            query = f"{contacts.prefix} {categoria.categoria} {contacts.content} {local.cidade} {contacts.suffix}"

        Args:
            prefix (str, optional): [prefixo]. Defaults to None.
            content (str, optional): [conteudo]. Defaults to None.
            suffix (str, optional): [sifixo]. Defaults to None.

        Returns:
            [type]: [Contacts classe]
        """
        session = SessionLocal()
        novo = Contacts(
                id_categoria=id_categoria,
                nome=nome,
                num_fone=num_fone,
                endereco=endereco,
                cidade=cidade,
                bairro=bairro,
                cep=cep,
                ddd=ddd,
                whatsapp=whatsapp,
                site_proprio=site_proprio,
                website=website,
                abre_em=abre_em,
                num_reviews=num_reviews,
                nota_review=nota_review,
                loja_fisica=loja_fisica,
                retirada_local=retirada_local,
                delivery=delivery,
                data_coleta=data_coleta,
                ativo=ativo,
            )
        session.add(novo)
        session.commit()
        session.refresh(novo)  # garante que os dados estão carregados
        session.expunge(novo)  # tira da sessão, mas mantém os atributos
        session.close()
        return novo

    @staticmethod
    def buscar_por_id(contacts_id: int):
        """ get ID
        Args:
            contacts_id (int): [get Id]

        Returns:
            [type]: [Contacts]
        """
        session = SessionLocal()
        contacts = session.query(Contacts).filter_by(id=contacts_id).first()
        if contacts:
            session.expunge(contacts)  # tira da sessão
        session.close()
        return contacts

    @staticmethod
    def listar_todos():
        """Get all basico

        Returns:
            [contacts[]]: [todos os query do banco]
        """
        session = SessionLocal()
        contacts = session.query(Contacts).all()
        for l in contacts:
            session.expunge(l)  # tira cada objeto da sessão
        session.close()
        return contacts

    @staticmethod
    def atualizar(contacts_id:int,
            id_categoria: int,
            nome: str,
            num_fone: int,
            endereco: str,
            cidade: str,
            bairro: str,
            cep: str,
            ddd: int,
            whatsapp: bool = False,
            site_proprio: bool = False,
            website: str = "",
            abre_em: str = "",
            num_reviews: int = 0,
            nota_review: float = 0.0,
            loja_fisica: bool = False,
            retirada_local: bool = False,
            delivery: bool = False,
            data_coleta: datetime = None,
            ativo: bool = True,
        ):      
        """ Update geral

        Args:
            contacts_id (int): [Id]
            prefix (str): [prefix]
            content (str): [content]
            suffix (str): [suffix]

        Returns:
            [contacts]
        """
        session = SessionLocal()
        contacts = session.query(Contacts).filter_by(id=contacts_id).first()
        if contacts:
                contacts.id_categoria = id_categoria
                contacts.nome = nome
                contacts.num_fone = num_fone
                contacts.endereco = endereco
                contacts.cidade = cidade
                contacts.bairro = bairro
                contacts.cep = cep
                contacts.ddd = ddd
                contacts.whatsapp = whatsapp
                contacts.site_proprio = site_proprio
                contacts.website = website
                contacts.abre_em = abre_em
                contacts.num_reviews = num_reviews
                contacts.nota_review = nota_review
                contacts.loja_fisica = loja_fisica
                contacts.retirada_local = retirada_local
                contacts.delivery = delivery
                contacts.ativo = ativo

        session.commit()
        session.refresh(contacts)  # atualiza os dados
        session.expunge(contacts)  # tira da sessão
        session.close()
        return contacts

    @staticmethod
    def deletar(contacts_id: int):
        """ Deleta com base no ID

        Args:
            contacts_id (int): [Contacts ID]
        """
        session = SessionLocal()
        contacts = session.query(Contacts).filter_by(id=contacts_id).first()
        if contacts:
            session.delete(contacts)
            session.commit()
        session.close()
        
