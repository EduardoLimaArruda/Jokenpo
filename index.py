import random

Mao = ["Pedra", "Papel", "Tesoura"]

Arm = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura\n")
Arm = int(Arm)

if Arm == 0:
    Arm = Mao[0]
elif Arm == 1:
    Arm = Mao[1]
elif Arm == 2:
    Arm = Mao[2]

IA = random.randint(0, 2)
if IA == 0:
    IA = Mao[0]
elif IA == 1:
    IA = Mao[1]
elif IA == 2:
    IA = Mao[2]

print("\nSua jogada foi", Arm)
print("Jogada adversária foi", IA ,"\n")

if Arm == Mao[0] and IA == Mao[2]: 
    print("Victory!\n")
elif Arm == Mao[1] and IA == Mao[0]: 
    print("Victory!\n")
elif Arm == Mao[2] and IA == Mao[1]: 
    print("Victory!\n")
elif Arm == IA:
    print("Draw!\n")
else:
    print("Defeat!\n")

Fechar = input("Pressione Enter para fechar!")