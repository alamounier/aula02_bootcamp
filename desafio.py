CONSTANTE_BONUS = 1000
#1) solicitar ao usuário que digite seu nome

nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Você incluiu número em seu nome")
    exit() #abortar
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou espaço")
    exit()

#2) solicitar ao usuário que digite o valor do seu usuário
salario_usuario = float(input("Digite o seu salário: "))
#3) solicitar ao usuário que digite o valor do seu bônus
bonus_usuario = float(input("Digite o valor do seu bônus: "))
#4) calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
#5) imprimir mensagem personalizada incluindo nome do usuário e valor do bonus
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")