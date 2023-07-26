quero_ler = 5
c= 0
maior = 0
while c < quero_ler:
    n = int(input('Digite 5 números:'))
    if c == 0:
        maior = n
    if n > maior:
        maior = n
    c += 1
print(f"O maior número é: {maior}")
print("Fim!")