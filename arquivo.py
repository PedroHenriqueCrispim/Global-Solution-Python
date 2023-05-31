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
    print("2. Desafio")
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
    print("O produto inovador de gerenciamento de temperatura para armazenamento de grãos foi concebido como resultado de extensivas pesquisas científicas e tecnológicas, com o objetivo primordial de fornecer uma solução altamente avançada para controlar e otimizar a temperatura durante o armazenamento de grãos.")
    print("Essa solução de vanguarda foi meticulosamente desenvolvida para atender às demandas complexas de agricultores e empresas agrícolas, oferecendo um controle preciso e sofisticado da temperatura para evitar o desperdício e a deterioração dos grãos.")
    print("Ao utilizar essa tecnologia de ponta, os usuários são capacitados a monitorar e ajustar de forma eficiente a temperatura do ambiente de armazenamento, garantindo a preservação da qualidade dos grãos e a maximização do seu valor comercial.")

# Função para exibir o problema
def exibir_problema():
    print()
    print("Desafio:")
    print()
    print("A manutenção adequada da temperatura durante o armazenamento de grãos é um desafio complexo enfrentado por agricultores e empresas agrícolas.")
    print("Sem uma solução eficiente, é difícil controlar e regular a temperatura ambiente, o que pode resultar em perdas significativas de grãos devido a deterioração, germinação, proliferação de pragas e outras condições indesejáveis.")
    print("Além disso, a falta de controle preciso da temperatura pode levar à redução da qualidade dos grãos e à desvalorização do produto final, resultando em prejuízos financeiros consideráveis.")

# Função para exibir a solução
def exibir_solucao():
    print()
    print("Solução:")
    print()
    print("A solução revolucionária oferecida pelo nosso produto de gerenciamento de temperatura para armazenamento de grãos é um sistema avançado e inteligente que permite o monitoramento contínuo e o controle preciso da temperatura ambiente.")
    print("Com sensores de última geração e algoritmos sofisticados, os usuários têm acesso a um sistema automatizado que ajusta a temperatura de forma otimizada, evitando o desperdício e a deterioração dos grãos.")
    print("Além disso, nossa solução fornece alertas em tempo real sobre condições anormais, permitindo uma intervenção rápida e efetiva para evitar danos aos grãos.")
    print("Com recursos de análise avançada e relatórios detalhados, os usuários podem tomar decisões informadas para otimizar o ambiente de armazenamento e garantir a máxima qualidade e valor dos grãos.")
    print("Nosso produto também é altamente personalizável e adaptável às necessidades específicas de cada usuário, garantindo uma solução completa e eficiente para o controle da temperatura no armazenamento de grãos.")

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
