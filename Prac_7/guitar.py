from Prac_7.guitars import Guitar
my_guitars = []
while_loop_iteration = 0
name = 'Easter Egg'
print("My Guitars!")
my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
while name != '':

    name = input("Name: ")
    year = input("Year: ")
    cost = input("Cost: $")
    my_guitars.append([name, year, cost])
    Guitar(my_guitars[while_loop_iteration])
    while_loop_iteration += 1

for i in range(0,len(my_guitars)):
    print('Guitar {}: {:>20}'.format(i, my_guitars[i]))