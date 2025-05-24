from sqlalchemy import Column, String
from database import Base
from modelos.pessoa import Pessoa

class Professor(Pessoa):
    __tablename__ = 'professores'

    cpf = Column(String, primary_key=True, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    disciplina = Column(String)

    def __init__(self, cpf, nome, disciplina):
        super().__init__(cpf, nome)
        self.disciplina = disciplina

    def consultar_notas(self):
        pass