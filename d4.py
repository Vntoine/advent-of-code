def part1():
   with open('data/data4.txt') as f:
      data = f.readlines()
   total = 0
   for pair in data:
      pair = pair.replace('\n','').split(',')
      pair = [pair[0].split('-'),pair[1].split('-')]
      if int(pair[0][0])<=int(pair[1][0]) and int(pair[0][1])>=int(pair[1][1]) or int(pair[1][0])<=int(pair[0][0]) and int(pair[1][1])>=int(pair[0][1]):
         total+=1
   print(total)


   # Answer must be "595"

def part2():
   with open('data/data4.txt') as f:
      data = f.readlines()
   total = 0
   for pair in data:
      pair = pair.replace('\n','').split(',')
      pair = [pair[0].split('-'),pair[1].split('-')]
      if int(pair[0][1])>=int(pair[1][0]) and int(pair[0][0])<=int(pair[1][0]) or int(pair[1][1])>=int(pair[0][0]) and int(pair[1][0])<=int(pair[0][0]):
         total+=1
   print(total)


   # Answer must be "952"
part2()
