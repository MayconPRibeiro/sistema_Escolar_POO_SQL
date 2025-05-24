from database import Base, engine, session
from modelos.turma import Turma
from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota

Base.metadata.create_all(engine)

turma1 = Turma(nome="ADS1", periodo="Noturno")

aluno1 = Aluno(cpf="12345678900", nome="Gabriel")
aluno2 = Aluno(cpf="98765432100", nome="Lucas")

turma1.alunos.append(aluno1)
turma1.alunos.append(aluno2)

disciplina1 = Disciplina(nome="POO")

nota1 = Nota(aluno=aluno1, disciplina=disciplina1, av1=7, av2=8)
nota2 = Nota(aluno=aluno2, disciplina=disciplina1, av1=6, av2=5)

session.add(turma1)
session.add(disciplina1)
session.add(nota1)
session.add(nota2)

session.commit()

turmas = session.query(Turma).all()
for turma in turmas:
    print(f"\nTurma: {turma.nome} ({turma.periodo})")
    for aluno in turma.alunos:
        print(f" - Aluno: {aluno.nome} (CPF: {aluno.cpf})")
        for nota in aluno.notas:
            print(f"   Disciplina: {nota.disciplina.nome}")
            print(f"   AV1: {nota.av1} | AV2: {nota.av2} | Média: {nota.media} | Situação: {nota.situacao}")