# Criando os dicionarios.
usuarios = {}
equipamentos = {}

# Criando uma classe para o usuario.
class Usuario:
    def __init__(self, nome, idade, setor, cpf, data_inicio, status):
        self.nome = nome
        self.idade = idade
        self.setor = setor
        self.cpf = cpf
        self.data_inicio = data_inicio
        self.status = status

# Função de cadastro de usuario
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ").capitalize()
    idade = int(input("Digite a idade do usuário: "))
    setor = input("Digite o setor do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_inicio = input("Digite a data de início do usuário: ")
    status = input("Digite o status do usuário (Ativo/Inativo): ").capitalize() == 'Ativo' 

# 'Capitalize' faz com que a primeira letra seja maiuscula (evitando erro no case sentive)


# Atribuindo as variaveis até as classes.
    usuario = Usuario(nome, idade, setor, cpf, data_inicio, status)
    usuarios[cpf] = usuario
    print("Usuário cadastrado com sucesso!")

# Cadastro de equipamento.
def cadastrar_produto():
    nome = input("Digite o nome do equipamento: ")
    tamanho = input("Digite o tamanho do equipamento: ")
    setor = input("Digite o setor do equipamento: ")


# Cria um dicionario chamado equipamento contendo as informações do produto.
    equipamento = {
        'nome': nome,
        'tamanho': tamanho,
        'setor': setor,

    }
#O len foi usado para cadastrar o codigo automaticamente de cada produto.
    codigo = len(equipamentos) + 1
    equipamentos[codigo] = equipamento
    print("Equipamento cadastrado com sucesso!")

# Exibir informações do usuario, A pesquisa é feita pelo CPF do usuario.
def exibir_info_usuario():
    cpf = input("Digite o CPF do usuário que deseja exibir as informações: ")
    if cpf in usuarios:
        usuario = usuarios[cpf]
        print("Informações do Usuário:")
        print("Nome:", usuario.nome)
        print("Idade:", usuario.idade)
        print("Setor:", usuario.setor)
        print("CPF:", usuario.cpf)
        print("Data de Início:", usuario.data_inicio)
        print("Status:", "Ativo" if usuario.status else "Inativo")
    else:
        print("Usuário não encontrado.")

# Exibe todos os equipamentos.
def exibir_equipamentos():
    if equipamentos:
        print("Equipamentos cadastrados:")
        for codigo, equipamento in equipamentos.items():
            print("Código:", codigo)
            print("Nome:", equipamento['nome'])
            print("Tamanho:", equipamento['tamanho'])
            print("Setor:", equipamento['setor'])

            print()
    else:
        print("Não há equipamentos cadastrados.")

# Editar informações do Usuario, Pesquisa pelo CPF do usuario e é possivel modificar Nome, Idade, Setor, Data do inicio e Status.
def editar_info_usuario():
    cpf = input("Digite o CPF do usuário que deseja editar: ")
    if cpf in usuarios:
        usuario = usuarios[cpf]

        print("Digite as novas informações do usuário (deixe em branco para manter o valor atual):")

        usuario.nome = input(f"Nome ({usuario.nome}): ") or usuario.nome
        usuario.idade = int(input(f"Idade ({usuario.idade}): ")) or usuario.idade
        usuario.setor = input(f"Setor ({usuario.setor}): ") or usuario.setor
        usuario.data_inicio = input(f"Data de Início ({usuario.data_inicio}): ") or usuario.data_inicio
        status = input(f"Status ({'Ativo' if usuario.status else 'Inativo'}): ")
        if status:
            usuario.status = status.capitalize() == 'Ativo'

        print("Usuário editado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Editar informações de equipamento, edita o Nome,Tamanho e o Setor do equipamento.
def editar_info_equipamento():
    codigo = int(input("Digite o código do equipamento que deseja editar: "))
    if codigo in equipamentos:
        equipamento = equipamentos[codigo]

        print("Digite as novas informações do equipamento (deixe em branco para manter o valor atual):")

        equipamento['nome'] = input(f"Nome ({equipamento['nome']}): ") or equipamento['nome']
        equipamento['tamanho'] = input(f"Tamanho ({equipamento['tamanho']}): ") or equipamento['tamanho']
        equipamento['setor'] = input(f"Setor ({equipamento['setor']}): ") or equipamento['setor']

        print("Equipamento editado com sucesso!")
    else:
        print("Equipamento não encontrado.")

# Função de gerenciamento de usuario, serve para adicionar ou remover usuario.
def gerenciar_usuarios():
    opcao = input("Digite '1' para adicionar usuário ou '2' para remover usuário: ")
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        cpf = input("Digite o CPF do usuário que deseja remover: ")
        if cpf in usuarios:
            del usuarios[cpf]
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado.")
    else:
        print("Opção inválida!")

# Função de Gerenciar equipamentos, utilizada para cadastrar ou remover  equipamentos.
def gerenciar_equipamentos():
    opcao = input("Digite '1' para adicionar equipamento ou '2' para remover equipamento: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        codigo = int(input("Digite o código do equipamento que deseja remover: "))
        if codigo in equipamentos:
            del equipamentos[codigo]
            print("Equipamento removido com sucesso!")
        else:
            print("Equipamento não encontrado.")
    else:
        print("Opção inválida!")

# O codigo na versão beta começará aqui, mas caso a gente continue isso no futuro terá tela de login antes da tela Menu.
# Menu. Libera a base para conseguir interagir com o codigo dando as opções abaixo.
def menu():
    while True:
        print("===LabERP Menu===")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Produto")
        print("3 - Exibir Informações do Usuário")
        print("4 - Exibir Equipamentos")
        print("5 - Editar Usuário")
        print("6 - Editar Equipamento")
        print("7 - Gerenciar Usuários")
        print("8 - Gerenciar Equipamentos")
        print("9 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            cadastrar_produto()
        elif opcao == 3:
            exibir_info_usuario()
        elif opcao == 4:
            exibir_equipamentos()
        elif opcao == 5:
            editar_info_usuario()
        elif opcao == 6:
            editar_info_equipamento()
        elif opcao == 7:
            gerenciar_usuarios()
        elif opcao == 8:
            gerenciar_equipamentos()
        elif opcao == 9:
            break
        else:
            print("Opção inválida!")

        print("\n")

menu()