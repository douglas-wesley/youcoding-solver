def casa(string): # Recebe uma lista fatiada com os ({[]})
    stack = []
    for char in string:
        if len(stack) >0:
            if char == ')' and stack[-1] == '(':
                stack.pop(-1)
            elif char == ']' and stack[-1] == '[':
                stack.pop(-1)
            elif char == '}' and stack[-1] == '{':
                stack.pop(-1)
            else:
                stack.append(char)
        else:
            stack.append(char)
    if len(stack) == 0:
        return 'casamento perfeito'
    else:
        return 'casamento imperfeito'

def filtrar_lim(stack): # Filtra apenas os parenteses
    return [c for c in stack if c in '()[]{}']

def main():
    i = input()
    i_fatiado = filtrar_lim(i)
    print(casa(i_fatiado))

main()