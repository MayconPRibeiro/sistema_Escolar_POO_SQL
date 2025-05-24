from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    aluno_cpf = Column(String, ForeignKey('alunos.cpf'))
    disciplina_nome = Column(String, ForeignKey('disciplinas.nome'))
    av1 = Column(Integer)
    av2 = Column(Integer)

    aluno = relationship("Aluno", back_populates="notas")
    disciplina = relationship("Disciplina", back_populates="notas")

    def __init__(self, aluno, disciplina, av1=0, av2=0):
        self.aluno = aluno
        self.disciplina = disciplina
        self.av1 = av1
        self.av2 = av2

    @property
    def media(self):
        return (self.av1 + self.av2) / 2

    @property
    def situacao(self):
        m = self.media
        if m >= 5:
            return "Aprovado"
        elif m == 4:
            return "Recuperação"
        else:
            return "Reprovado"