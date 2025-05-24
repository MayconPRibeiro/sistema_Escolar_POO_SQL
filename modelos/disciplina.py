from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Disciplina(Base):
    __tablename__ = 'disciplinas'

    id = Column(Integer, primary_key=True, autoincrement = True, nullable=False, unique=True)
    nome = Column(String, nullable=False)

    notas = relationship("Nota", back_populates="disciplina", cascade="all, delete-orphan")

    def __init__(self, nome):
        self.nome = nome