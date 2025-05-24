from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import Base
from modelos.pessoa import Pessoa

class Aluno(Pessoa):
    __tablename__ = 'alunos'

    cpf = Column(Integer, primary_key=True, nullable=False, unique=True)
    nome = Column(String)
    turma_nome = Column(String, ForeignKey('turmas.nome'))

    turma = relationship("Turma", back_populates="alunos")
    notas = relationship("Nota", back_populates="aluno", cascade="all, delete-orphan")

    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)

    def consultar_notas(self):
        return self.notas