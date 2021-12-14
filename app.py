n = int(input("Digite um número inteiro:"))
n_primo = True

for i in range (2, n//2):
    if n % i == 0:
        n_primo =  False
        break
        
if n_primo:
    print("É um número primo")
else:
    print("Não é um número primo")
