Bois = []

maisGordo = 0
idDoMaisGordo = 0

maisMagro = 0
idDoMaisMagro = 0
while True: 
    id = int(input("Qual é o identificador do boi?0 para sair "))
    peso = float(input("Digite o peso ou 0 para sair: "))
    if peso == 0 or id == 0:
        break

    if peso > maisGordo:
        maisGordo = peso
        idDoMaisGordo = id
    if peso < Magro:
        Magro = peso
        idDoMagro = id
    boi = {"id": id, "peso": peso}
    Bois.append(boi)
print("-"*10+"Listagem"+"-"*10)
if len(Bois) == 0:
    print("Não tem boi")
else:
    for x in Bois:
        print(x)
    print(f'O id do boi mais gordo {idDoMaisGordo} e o seu peso {maisGordo:.2f}')
    print(f'O id do boi mais magro {idDoMaisMagro} e o seu peso {maisMagro:.2f}')

