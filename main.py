from database import session, Base, engine
from modelos.turma import Turma
from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota

def menu_principal():
    while True:
        print("\n===== Sistema Escolar =====")
        print("1 - Criar Aluno")
        print("2 - Criar Professor")
        print("3 - Criar Disciplina")
        print("4 - Sou Aluno")
        print("5 - Sou Professor")
        
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            Aluno.criar_aluno()
        elif escolha == '2':
            Professor.criar_professor()
        elif escolha == '3':
            Disciplina.criar_disciplina()
        elif escolha == '4':
            menu_aluno()
        elif escolha == '5':
            menu_professor()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            menu_principal()

def menu_aluno():
    while True:
        print("\n--- Menu Aluno ---")
        print("1 - Consultar minhas Disciplinas")
        print("2 - Adicionar Aluno a turma")
        print("3 - Listar Turma do Aluno")
        print("0 - Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            Aluno.consultar_disciplinas_e_notas_com_tratamento(session)
        elif escolha == '2':
            Aluno.adicionar_turma(session)
        elif escolha == '3':
            Aluno.listar_turma(session)
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

def menu_professor():
    while True:
        print("\n--- Menu Professor ---")
        print("1 - Criar Nota")
        print("2 - Consultar Notas")
        print("3 - Modificar Nota")
        print("4 - Excluir Notas")
        print("0 - Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            Professor.criar_nota(session)
        elif escolha == '2':
            Professor.consultar_notas(session)
        elif escolha == '3':
            Professor.modificar_nota(session)
        elif escolha == '4':
            Professor.excluir_nota(session)
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

def criar_nota():
    print("Criar nota - implementar lógica aqui")

def excluir_nota():
    print("Excluir nota - implementar lógica aqui")

def modificar_nota():
    print("Modificar nota - implementar lógica aqui")

def consultar_notas():
    print("Consultar notas - implementar lógica aqui")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu_principal()