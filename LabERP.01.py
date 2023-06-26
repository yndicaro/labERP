usuarios = {}
equipamentos = {}

class Usuario:
    def __init__(self, nome, idade, setor, cpf, data_inicio, status):
        self.nome = nome
        self.idade = idade
        self.setor = setor
        self.cpf = cpf
        self.data_inicio = data_inicio
        self.status = status

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ").capitalize()
    idade = int(input("Digite a idade do usuário: "))
    setor = input("Digite o setor do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    
    while len(cpf) != 11:
        print('CPF Inválido! É necessário ter 11 dígitos.')
        cpf = input("Digite o CPF do usuário: ")
        cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        
    if not cpf.isdigit():
        print("CPF inválido! O CPF deve conter apenas dígitos numéricos.")
        cpf = input("Digite o CPF do usuário: ")
        cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        
    data_inicio = input("Digite a data de início do usuário: ")
    
    while len(data_inicio) != 8 or not data_inicio.isdigit():
        print('Data Inválida! É necessário ter 8 dígitos numéricos (DDMMAAAA).')
        data_inicio = input("Digite a data de início do usuário (DDMMAAAA): ")
    
    # Formatação da Data de inicio.
    
    data_inicio = '{}/{}/{}'.format(data_inicio[:2], data_inicio[2:4], data_inicio[4:])
 
    status = input("Digite o status do usuário (Ativo/Inativo): ").capitalize() == 'Ativo'
    
    # 'Capitalize' faz com que a primeira letra seja maiúscula (evitando erro no case sensitive)
    # Atribuindo as variáveis até as classes.
    
    usuario = Usuario(nome, idade, setor, cpf_formatado, data_inicio, status)
    usuarios[cpf_formatado] = usuario
    print("Usuário cadastrado com sucesso!")

# Cadastro de equipamento.

def cadastrar_produto():
    nome = input("Digite o nome do equipamento: ")
    tamanho = input("Digite o tamanho do equipamento: ")
    setor = input("Digite o setor do equipamento: ")
    equipamento = {
        'nome': nome,
        'tamanho': tamanho,
        'setor': setor,
    }
    # O len foi usado para cadastrar o código automaticamente de cada produto.
    codigo = len(equipamentos) + 1
    equipamentos[codigo] = equipamento
    print("Equipamento cadastrado com sucesso!")

# Buscar usuário, A pesquisa é feita pelo CPF do usuário.

def buscar_usuario():
    opcao = input("Digite '1' para buscar por CPF,\n'2' para buscar por Data de Início,\n"
              "'3' para buscar pelo Primeiro Nome,\n'4' para buscar por Atividade\n"
              "ou '5' para exibir todos os usuários cadastrados: ")
    if opcao == '1':
        
        # Busca atraves do CPF do usuario.
        
        cpf = input("Digite o CPF do usuário que deseja buscar: ")
        cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        if cpf_formatado in usuarios:
            usuario = usuarios[cpf_formatado]
            exibir_info_usuario(usuario)
        else:
            print("Usuário não encontrado.")
    elif opcao == '2':
        
        # Busca atraves da data de Inicio.
        
        data_inicio = input("Digite a data de início do usuário que deseja buscar (DD/MM/AAAA): ")
        data_inicio = '{}/{}/{}'.format(data_inicio[:2], data_inicio[2:4], data_inicio[4:])
        
        # Feita a formatação novamente para evitar o erro quando fazer a busca.
        
        usuarios_encontrados = [usuario for usuario in usuarios.values() if usuario.data_inicio == data_inicio]
        exibir_usuarios_encontrados(usuarios_encontrados)
    elif opcao == '3':
        
        # Busca pelo Nome
        
        primeiro_nome = input("Digite o primeiro nome do usuário que deseja buscar: ")
        usuarios_encontrados = [usuario for usuario in usuarios.values() if usuario.nome.startswith(primeiro_nome)]
        
        # Starswitch pega a primeira parte do nome do usuario.
        
        exibir_usuarios_encontrados(usuarios_encontrados)
    elif opcao == '4':
        
        # Busca pela atividade
        
        atividade = input("Digite a atividade do usuário que deseja buscar (Ativo ou Inativo): ")
        atividade = atividade.capitalize()
        usuarios_encontrados = [usuario for usuario in usuarios.values() if (atividade == 'Ativo' and usuario.status) or (atividade == 'Inativo' and not usuario.status)]
        exibir_usuarios_encontrados(usuarios_encontrados)
    elif opcao == '5':
        if usuarios:
            print("Usuários cadastrados:")
            for cpf, usuario in usuarios.items():
                print("CPF:", cpf)
                print("Nome:", usuario.nome)
                print("Idade:", usuario.idade)
                print("Setor:", usuario.setor)
                print("Data de Início:", usuario.data_inicio)
                print("Status:", "Ativo" if usuario.status else "Inativo")
                print()
        else:
            print("Não há mais usuários cadastrados.")
    else:
        print("Opção inválida!")

def exibir_info_usuario(usuario):
    print("Informações do Usuário:")
    print("Nome:", usuario.nome)
    print("Idade:", usuario.idade)
    print("Setor:", usuario.setor)
    print("CPF:", usuario.cpf)
    print("Data de Início:", usuario.data_inicio)
    print("Status:", "Ativo" if usuario.status else "Inativo")

def exibir_usuarios_encontrados(usuarios_encontrados):
    if usuarios_encontrados:
        print("Usuários encontrados:")
        for usuario in usuarios_encontrados:
            print("Nome:", usuario.nome)
            print("CPF:", usuario.cpf)
            print("Data de Início:", usuario.data_inicio)
            print("Status:", "Ativo" if usuario.status else "Inativo")
            print()
    else:
        print("Nenhum usuário encontrado.")

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

# Editar informações do Usuario, Pesquisa pelo CPF do usuário e é possível modificar Nome, Idade, Setor, Data do início e Status.

def editar_info_usuario():
    cpf = input("Digite o CPF do usuário que deseja editar: ")
    cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    
    # Feito a formatação novamente quando digitado para evitar o erro durante a busca.
    
    if cpf_formatado in usuarios:
        usuario = usuarios[cpf_formatado]
        print("Digite as novas informações do usuário (deixe em branco para manter o valor atual):")
        usuario.nome = input(f"Nome ({usuario.nome}): ") or usuario.nome
        usuario.setor = input(f"Setor ({usuario.setor}): ") or usuario.setor
        usuario.data_inicio = input(f"Data de Início ({usuario.data_inicio}): ") or usuario.data_inicio
        status = input(f"Status ({'Ativo' if usuario.status else 'Inativo'}): ")
        if status:
            usuario.status = status.capitalize() == 'Ativo'
        print("Usuário editado com sucesso!")
    else:
        print("Usuário não encontrado.")

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

# Função de gerenciamento de usuário, serve para adicionar ou remover usuário.
def confirmar_exclusao(nome):
    confirmacao = input(f"Você tem certeza que deseja excluir o Usuário: {nome}? (s/n) ")
    return confirmacao.lower() == 's'

def gerenciar_usuarios():
    opcao = input("Digite '1' para adicionar usuário ou '2' para remover usuário: ")
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        cpf = input("Digite o CPF do usuário que deseja remover: ") 
        cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        if cpf_formatado in usuarios:
            nome_completo = usuarios[cpf_formatado].nome
            # Obtém o nome completo do usuário a partir do CPF
            if confirmar_exclusao(nome_completo):
                del usuarios[cpf_formatado]
                
# Remove o usuario com base no CPF q foi cadastrado, Usado CPF para evitar erros de nomes parecidos.
                
                print("Usuário removido com sucesso!")
            else:
                print("Exclusão cancelada.")
        else:
            print("Usuário não encontrado.")
    else:
        print("Opção inválida!")

# Função de Gerenciar equipamentos, utilizada para cadastrar ou remover equipamentos.
def gerenciar_equipamentos():
    opcao = input("Digite '1' para adicionar equipamento ou '2' para remover equipamento: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        codigo = int(input("Digite o código do equipamento que deseja remover: "))
        if codigo in equipamentos:
            
            # faz confirmação se possui o codigo cadastrado na tabela de Equipamentos.
            
            del equipamentos[codigo]
            print("Equipamento removido com sucesso!")
        else:
            print("Equipamento não encontrado.")
    else:
        print("Opção inválida!")

#Menu Principal onde vai começar o codigo, aqui leva a qualquer outra parte do codigo sendo a função de cadastrar, gerenciar ou editar 

def menu():
    while True:
        print("=== LabERP Menu ===")
        print("1 - Menu de Cadastros")
        print("2 - Menu de Gerenciamentos")
        print("3 - Menu de Edições")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            menu_cadastrar()
        elif opcao == 2:
            menu_exibir()
        elif opcao == 3:
            menu_editar()
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

# Menu cadastrar, uma das partes principais do codigo, serve para levar a tela de cadastro do Equipamento ou do usuario

def menu_cadastrar():
    while True:
        print("=== Menu de Cadastros ===")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Equipamento")
        print("3 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            cadastrar_produto()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")

#Menu de Exbição, parte do codigo que designada para Buscar ou Exibir equipamentos ou Usuarios cadastrados.

def menu_exibir():
    while True:
        print("=== Menu de Gerenciamentos ===")
        print("1 - Buscar Usuário")
        print("2 - Exibir Equipamentos")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Equipamentos")
        print("5 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            buscar_usuario()
        elif opcao == 2:
            exibir_equipamentos()
        elif opcao == 3:
            gerenciar_usuarios()
        elif opcao == 4:
            gerenciar_equipamentos()
        elif opcao == 5:
            break
        else:
            print("Opção inválida!")

# Menu de Edições, principal parte onde vai encaminhar para o que vai ser editado.

def menu_editar():
    while True:
        print("=== Menu de Edições ===")
        print("1 - Editar Informações de Usuário")
        print("2 - Editar Informações de Equipamento")
        print("3 - Voltar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            editar_info_usuario()
        elif opcao == 2:
            editar_info_equipamento()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")

menu()