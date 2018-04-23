from Prac_7.guitars import Guitar
my_guitars = []
name = 'Easter Egg'
print("My Guitars!")
my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
while name != '':

    name = input("Name: ")
    if name != '':
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        my_guitars.append(Guitar(name, year, cost))

for i in range(0,len(my_guitars)):
    print('Guitar {}: {!s:}'.format(i + 1, my_guitars[i]))