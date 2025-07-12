def divisivel7(n):
    if n == 7 or n == 49: # Caso Base, 49 dá um loop infiníto
        return 's'
    if n < 7: # Qualquer valor abaixo de 7 n é divisível por ele mesmo
        return 'n'
    return divisivel7(5*(n%10) + (n//10)) # Caso Recursivo

i = int(input())
print(divisivel7(i))