with open("../inputs/d1.txt", "r") as f:
   data = f.read()
   data = data.split('\n')
   data.append('')
   count = 0
   calories = []
   for i in data:
      if i != '':
         count += int(i)
      else:
         calories.append(count)
         count = 0

calories.sort(reverse=True)
print('sol 1: ', calories[0])
print('sol 2: ', sum(calories[:3]))
