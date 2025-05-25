from database import session
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
        print("3 - Sou Aluno")
        print("4 - Sou Professor")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            Aluno.criar_aluno_com_tratamento()
        elif escolha == '2':
            Professor.criar_prof_com_tratamentos()
        elif escolha == '3':
            menu_aluno()
        elif escolha == '4':
            menu_professor()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            menu_principal()

def menu_aluno():
    print("\n--- Menu Aluno ---")
    print("1 - Consultar minhas notas")
    print("0 - Voltar")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        print("Mostrando suas notas... (implemente a lógica aqui)")
    elif escolha == '0':
        return
    else:
        print("Opção inválida!")

def menu_professor():
    while True:
        print("\n--- Menu Professor ---")
        print("1 - Criar Nota")
        print("2 - Excluir Nota")
        print("3 - Modificar Nota")
        print("4 - Consultar Notas")
        print("0 - Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_nota()
        elif escolha == '2':
            excluir_nota()
        elif escolha == '3':
            modificar_nota()
        elif escolha == '4':
            consultar_notas()
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
    menu_principal()