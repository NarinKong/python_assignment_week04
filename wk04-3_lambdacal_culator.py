add = lambda x,y: x+y
subtract = lambda x,y:x-y
multiply = lambda x,y:x*y
divide = lambda x,y: x/y

action = int(input("1.add\n2.subtract\n3.multiply\n4.divide\n"))
no1 = int(input("No.1:"))
no2 = int(input("No.2:"))
match action:
    case 1:
        print(add(no1,no2))
    case 2:
        print(subtract(no1,no2))
    case 3:
        print(multiply(no1,no2))
    case 4:
        print(divide(no1,no2))
