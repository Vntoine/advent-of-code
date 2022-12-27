def part1():
    with open('data/data6.txt') as f:
        data = f.read().replace('\n','')
    marker = ''
    markerIndex = 0
    for index,letter in enumerate(data,start=1):
        if letter not in marker:
            marker+=str(letter)
            markerIndex = index
        else:
            marker+=str(letter)
            for i in range(marker.index(letter)+1):
                marker = marker.replace(marker[0],'',1)
                
        if len(marker)==4:
            break
    print("Marker :",marker,"- Index de marker : ",markerIndex)

    
    # Answer must be "1909"

def part2():
    with open('data/data6.txt') as f:
        data = f.read().replace('\n','')
    marker = ''
    markerIndex = 0
    for index,letter in enumerate(data,start=1):
        if letter not in marker:
            marker+=str(letter)
            markerIndex = index
        else:
            marker+=str(letter)
            for i in range(marker.index(letter)+1):
                marker = marker.replace(marker[0],'',1)
                
        if len(marker)==14:
            break
    print("Marker :",marker,"- Index de marker : ",markerIndex)

    
    # Answer must be "3380"
    
part2()
