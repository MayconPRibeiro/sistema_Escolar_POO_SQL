from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Disciplina(Base):
    __tablename__ = 'disciplinas'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String, nullable=False, unique=True)

    notas = relationship("Nota", back_populates="disciplina", cascade="all, delete-orphan")
    professores = relationship("Professor", back_populates="disciplina")

    def __init__(self, nome):
        self.nome = nome

    def listar_notas(self):
        for nota in self.notas:
            print(f'Aluno: {nota.aluno.nome} || AV1: {nota.av1} || AV2: {nota.av2} || Média: {nota.media()}')