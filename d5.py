def part1():
    with open('data/data5.txt') as f:
        data = f.readlines()
    data = data[10:] # Only keep what matters
    crates = [
        ['W','B','D','N','C','F','J'],
        ['P','Z','V','Q','L','S','T'],
        ['P','Z','B','G','J','T'],
        ['D','T','L','J','Z','B','H','C'],
        ['G','V','B','J','S'],
        ['P','S','Q'],
        ['B','V','D','F','L','M','P','N'],
        ['P','S','M','F','B','D','L','R'],
        ['V','D','T','R']
    ]
    for index,item in enumerate(data):
        data[index] = item.replace('\n','').split(' ')
        data[index] = {
         'Crate' : int(data[index][1]),
         'From' : int(data[index][3])-1,
         'To' : int(data[index][5])-1
        }
        
    for instruction in data:
        for i in range(instruction["Crate"]):
            crates[instruction["To"]].append(crates[instruction["From"]].pop())

    for col in crates:
        print(col[len(col)-1],end='')


    # Answer must be "LBLVVTVLP"

def part2():
    with open('data/data5.txt') as f:
        data = f.readlines()
    data = data[10:] # Only keep what matters
    crates = [
        ['W','B','D','N','C','F','J'],
        ['P','Z','V','Q','L','S','T'],
        ['P','Z','B','G','J','T'],
        ['D','T','L','J','Z','B','H','C'],
        ['G','V','B','J','S'],
        ['P','S','Q'],
        ['B','V','D','F','L','M','P','N'],
        ['P','S','M','F','B','D','L','R'],
        ['V','D','T','R']
    ]
    for index,item in enumerate(data):
        data[index] = item.replace('\n','').split(' ')
        data[index] = {
         'Crate' : int(data[index][1]),
         'From' : int(data[index][3])-1,
         'To' : int(data[index][5])-1
        }

    for instruction in data:
        for i in range(instruction["Crate"]):
            movingsIndex = len(crates[instruction["From"]])-instruction["Crate"]+i
            crates[instruction["To"]].append(crates[instruction["From"]].pop(movingsIndex))  

    for col in crates:
        print(col[len(col)-1],end='')


    # Answer must be "TPFFBDRJD"
part2()
