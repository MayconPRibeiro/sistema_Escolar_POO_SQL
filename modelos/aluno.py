from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
from modelos.pessoa import Pessoa

class CPFInvalidoError(Exception):
    pass

class AlunoJaExisteError(Exception):
    pass

class Aluno(Base, Pessoa):
    __tablename__ = 'alunos'

    cpf = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    turma_nome = Column(String, ForeignKey('turmas.nome'))

    turma = relationship("Turma", back_populates="alunos")
    notas = relationship("Nota", back_populates="aluno", cascade="all, delete-orphan")

    def __init__(self, cpf, nome, turma=None):
        Pessoa.__init__(self, cpf, nome)  # chama construtor abstrato
        self.turma = turma

    @classmethod
    def criar_aluno(cls):
        print("\n--- Criar Aluno ---")
        try:
            cpf = input("Digite o CPF do aluno (somente números): ").strip()
            if not cpf.isdigit():
                raise CPFInvalidoError("CPF inválido, deve conter somente números.")
            cpf = int(cpf)
            
            nome = input("Digite o nome do aluno: ").strip()
            
            aluno_existente = session.query(cls).filter_by(cpf=cpf).first()
            if aluno_existente:
                raise AlunoJaExisteError("Já existe um aluno com esse CPF!")
            
            novo_aluno = cls(cpf=cpf, nome=nome)
            session.add(novo_aluno)
            session.commit()
            
            print(f"\nAluno {nome} cadastrado com sucesso!")
        
        except (CPFInvalidoError, AlunoJaExisteError) as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    @classmethod
    def criar_aluno_com_tratamento(cls):
        try:
            cls.criar_aluno()
        except (CPFInvalidoError, AlunoJaExisteError) as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def consultar_notas(self):
        if self.notas:
            for nota in self.notas:
                print(f"Disciplina: {nota.disciplina_nome} | AV1: {nota.av1} | AV2: {nota.av2}")
        else:
            print("Este aluno não possui notas cadastradas.")