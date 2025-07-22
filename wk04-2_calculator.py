def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return(x/y)

action = str(input("1.add\n2.subtract\n3.multiply\n4.divide\n"))
no1 = int(input("No.1:\n"))
no2 = int(input("No.2:\n"))
match action:
    case "add":
        add(no1,no2)
    case "subtract":
        subtract(no1,no2)
    case "multiply":
        multiply(no1,no2)
    case "divide":
        divide(no1,no2)
