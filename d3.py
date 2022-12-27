def part1():
   with open('data/data3.txt') as f:
      data = f.readlines()
   total = 0
   for item in data:
      common = ''
      item = item.replace('\n','')
      firstHalf = item[:len(item)//2]
      for i in range(len(firstHalf),len(item)):
         if item[i] in firstHalf and item[i] not in common:
            common += item[i]
            total += letterValue(item[i])
   print(total)


   # Answer must be "7795"

def letterValue(letter):
   return ord(letter)-96 if ord(letter)>90 else ord(letter)-38

def part2():
   with open('data/data3.txt') as f:
      data = f.readlines()
   total = 0
   for index in range(0,len(data),3):
      common = ''
      data[index] = data[index].replace('\n','')
      data[index+1] = data[index+1].replace('\n','')
      data[index+2] = data[index+2].replace('\n','')
      for letter in data[index]:
         if letter in data[index+1] and letter in data[index+2] and letter not in common:
            common += letter
            total += letterValue(letter)
   print(total)


   # Answer must be "2703"
part2()
