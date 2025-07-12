from math import floor

def get_string():
    lista = [int(x) for x in input().split()]
    target = lista[0]
    arr = lista[1:]
    return target, arr

target, arr = get_string()

def binSearchRecursive(arr: list, target: int, l:int, r:int, count: int = 0) -> int:
    # Verifica se existe o número
    if l > r:
        return count

    count += 1

    # Tamanho do array atual
    if (r - l + 1) % 2  == 0:
        m = floor((l+r) / 2) + 1
    else:
        m = floor((l+r) / 2 )

    # Retorna o caso base
    if arr[m] == target: 
        return count
    
    # Verifica se o meio é maior ou menor que o target
    elif arr[m] > target:
        return binSearchRecursive(arr, target, l,m-1, count)
    elif arr[m] < target:
        return binSearchRecursive(arr,target, m+1,r,count) 

print(binSearchRecursive(arr, target,0,len(arr)-1))