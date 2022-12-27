############# Partie 1

def part1():
    with open('data/data1.txt') as f:
        data = f.readlines()

    maxInventory = 0
    currentInventory = 0
    
    for i in data:
        if i != '\n' :
            currentInventory += int(i.replace('\n',''))
            if currentInventory > maxInventory:
                maxInventory = currentInventory
        else:
            currentInventory = 0
    print("Total de calories du lutin N°1: ",maxInventory)

    # Answer must be "68442"
    
##############

############## Partie 2

def part2():
    with open('data/data1.txt') as f:
        data = f.readlines()
    
    firstInventory = 0
    secondInventory = 0
    thirdInventory = 0
    currentInventory = 0

    for i in data:
        if i != '\n':
            currentInventory += int(i.replace('\n',''))
            if currentInventory > firstInventory:
                thirdInventory = secondInventory
                secondInventory = firstInventory
                firstInventory = currentInventory
            elif currentInventory > secondInventory:
                thirdInventory = secondInventory
                secondInventory = currentInventory
            elif currentInventory > thirdInventory:
                thirdInventory = currentInventory
        else:
            number = 0
            currentInventory = 0
        
    total = firstInventory + secondInventory + thirdInventory
    print('1: ',firstInventory,'\n2: ',secondInventory,'\n3: ',thirdInventory)
    print("Total de calories des trois lutins :",total)


    # Answer must be "204837"

##############
