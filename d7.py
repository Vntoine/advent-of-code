def part1():
    with open('data/data7.txt') as f:
        data = f.readlines()
    for index in range(len(data)):
        data[index] = data[index].replace('\n','')
    
    path = []
    directories= {"['/']":0}

    for item in data:
        item = item.replace('$ ','').split(' ')
        match item:
            case ['cd','/']:
                path = ['/']
            case ['cd','..']:
                path.pop()
            case ['cd',val]:
                path.append(val)
            case _:
                if len(item)==2:
                    if item[0]=="dir":
                        if item[1] not in directories.keys():
                            directories[str(path).replace(']',", '")+str(item[1])+"']"] = 0
                    else:
                        for i in range(1,len(path)+1):
                            directories[str(path[:i])] += int(item[0])
    # print(totalFrom(directories))
    return directories


    # Answer must be "1517599"

def totalFrom(dictionnary):
    total = 0
    for x in dictionnary:
        if dictionnary[x] < 100000:
            total += dictionnary[x]
    return total

def part2():
    directories = part1()
    space_needed = 30000000 - (70000000 - directories["['/']"])

    minimumSize = directories["['/']"]
    for x in directories:
        if directories[x] < minimumSize and directories[x] >= space_needed:
            minimumSize = directories[x]
    print("Plus proche :",minimumSize)
    

    # Answer must be "2481982"

part2()
