# Dicionário com os usuários e senhas
usuarios = {}

# Função para realizar o login
def fazer_login():
    print("== Login ==")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha inválidos. Tente novamente.")
        return False

# Função para realizar o cadastro
def fazer_cadastro():
    print("== Cadastro ==")
    novo_usuario = input("Digite um novo nome de usuário: ")
    if novo_usuario in usuarios:
        print("Usuário já existente. Tente novamente com um nome de usuário diferente.")
        return False
    nome_completo = input("Digite o nome completo: ")

    while True:
        telefone = input("Digite o telefone: ")
        if telefone.isdigit():
            break
        else:
            print("Telefone inválido. O telefone deve conter apenas números.")

    email = input("Digite o email: ")
    nova_senha = input("Digite uma nova senha: ")
    confirma_senha = input("Confirme a nova senha: ")
    if nova_senha != confirma_senha:
        print("As senhas não coincidem. Tente novamente.")
        return False
    usuarios[novo_usuario] = {
        "nome_completo": nome_completo,
        "telefone": telefone,
        "email": email,
        "senha": nova_senha,
    }
    print("Cadastro realizado com sucesso!")
    return True

# Função para exibir o menu de opções
def exibir_menu():
    print()
    print("== Saiba mais sobre o Armazenamento de Grãos ==")
    print()
    print("Opções disponíveis:")
    print("1. História do Produto")
    print("2. Problema")
    print("3. Solução")
    print("0. Sair")

# Função para validar a opção escolhida pelo usuário
def validar_opcao(opcao):
    if opcao.isdigit() and int(opcao) in range(4):
        return True
    return False

# Função para exibir a história do produto
def exibir_historia():
    print()
    print("História do Produto:")
    print()
    print("O produto de controle de armazenamento de grãos foi desenvolvido com o objetivo de oferecer uma solução eficiente para monitorar e gerenciar a quantidade de grãos armazenados.")
    print("Ele foi projetado para atender às necessidades de agricultores e empresas agrícolas, permitindo um controle preciso e facilitado do estoque de grãos.")
    print("Com o uso desse produto, é possível ter uma visão clara da quantidade de grãos armazenados, facilitando o planejamento e a tomada de decisões relacionadas ao armazenamento e comercialização dos grãos.")

# Função para exibir o problema
def exibir_problema():
    print()
    print("Problema:")
    print()
    print("Um dos principais problemas enfrentados pelos agricultores e empresas agrícolas é o controle e gerenciamento eficiente do estoque de grãos.")
    print("Sem uma solução adequada, é difícil ter uma visão precisa da quantidade de grãos armazenados, o que pode levar a problemas como falta ou excesso de estoque, dificuldades no planejamento e prejuízos financeiros.")
    print("Além disso, a falta de um controle eficiente também pode impactar a qualidade dos grãos, prejudicando a sua comercialização.")

# Função para exibir a solução
def exibir_solucao():
    print()
    print("Solução:")
    print()
    print("A solução oferecida pelo produto de controle de armazenamento de grãos é um sistema que permite adicionar, remover e exibir a quantidade atual de grãos armazenados.")
    print("Com esse sistema, os usuários podem facilmente adicionar grãos ao estoque quando ocorrerem novos armazenamentos e remover grãos quando houver vendas ou retiradas.")
    print("Todas as operações são registradas e atualizadas automaticamente, fornecendo uma visão atualizada e precisa da quantidade de grãos armazenados.")

# Função principal do programa
def main():
    # Carregar usuários do arquivo (se existir)
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario, nome_completo, telefone, email, senha = linha.strip().split(":")
                usuarios[usuario] = {
                    "nome_completo": nome_completo,
                    "telefone": telefone,
                    "email": email,
                    "senha": senha,
                }
    except FileNotFoundError:
        pass

    while True:
        logado = False
        while not logado:
            opcao = input("Digite '1' para fazer login ou '2' para fazer cadastro: ")
            if opcao == "1":
                logado = fazer_login()
            elif opcao == "2":
                logado = fazer_cadastro()
            else:
                print("Opção inválida. Digite '1' para login ou '2' para cadastro.")

        if logado:
            while True:
                exibir_menu()
                opcao = input("Digite o número da opção desejada: ")
                while not validar_opcao(opcao):
                    print("Opção inválida. Digite um número de 0 a 3.")
                    opcao = input("Digite o número da opção desejada: ")

                if opcao == "1":
                    exibir_historia()
                elif opcao == "2":
                    exibir_problema()
                elif opcao == "3":
                    exibir_solucao()
                else:
                    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
                    while reiniciar.lower() not in ["s", "n"]:
                        reiniciar = input("Resposta inválida. Deseja reiniciar o programa? (s/n): ")
                    if reiniciar.lower() == "s":
                        break
                    else:
                        print("Encerrando o programa...")
                        # Salvar usuários em usuarios.txt arquivo antes de encerrar
                        with open("usuarios.txt", "w") as arquivo:
                            for usuario, dados in usuarios.items():
                                nome_completo = dados["nome_completo"]
                                telefone = dados["telefone"]
                                email = dados["email"]
                                senha = dados["senha"]
                                arquivo.write(f"{usuario}:{nome_completo}:{telefone}:{email}:{senha}\n")
                        return

# Execução do programa
main()
