def part1():
    with open('data2.txt') as f:
        data = f.readlines()
    total = 0
    for i in data:
        i = i.replace('\n','')
        total += resultatShifumi(i)
    print(total)

    # Answer must be "8933"

def resultatShifumi(game):
    # Schéma de game : "a x" -> longueur de 3 avec [0] pour a et [2] pour x
    result = 0
    
    if game[2] == 'X':
        result+=1
        if game[0] == 'A':
            result+=3
        elif game[0] == 'C':
            result += 6
    elif game[2] == 'Y':
        result+=2
        if game[0] == 'B':
            result+=3
        elif game[0] == 'A':
            result += 6
    else:
        result+=3
        if game[0] == 'C':
            result+=3
        elif game[0] == 'B':
            result += 6
    return result

def choixShifumi(game):
    result = 0

    if game[2] == 'X':
        if game[0] == 'A':
            result+=3
        elif game[0] == 'B':
            result+=1
        else:
            result+=2
    elif game[2] == 'Y':
        result+=3
        if game[0] == 'A':
            result+=1
        elif game[0] == 'B':
            result+=2
        else:
            result+=3
    else:
        result+=6
        if game[0] == 'A':
            result+=2
        elif game[0] == 'B':
            result+=3
        else:
            result+=1
    return result

def part2():
    with open('data/data2.txt') as f:
        data = f.readlines()
    total = 0
    for i in data:
        i = i.replace('\n','')
        total += choixShifumi(i)
    print(total)


    # Answer must be "11998"
    
part2()
