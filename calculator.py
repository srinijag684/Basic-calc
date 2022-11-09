#add
def add(x,y):
    answer = int(x) + int(y)
    print("The answer is" + " " + str(answer) + "\n")

#subtract
def sub(x,y):
    answer = int(x) - int(y)
    print("The answer is" + " " + str(answer)+ "\n")

#divide
def div(x,y):
    answer = int(x) // int(y)
    print("The answer is" + " " + str(answer)+ "\n")

#multiply
def mul(x,y):
    answer = int(x) * int(y)
    print("The answer is" + " " + str(answer)+ "\n")

while True:

    print("A. Addition")
    print("B. Subtraction")
    print("C. Division")
    print("D. Multiplication")
    print("E. Exit")

    options = input("Enter your choice: ")

    if options == "a" or options == "A" :
        print("Addition")
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        add(x,y)

    elif options == "b" or options == "B" :
        print("Subtraction")
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        sub(x,y)

    elif options == "c" or options == "C" :
        print("Division")
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        div(x,y)

    elif options == "d" or options == "D" :
        print("Multiplication")
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        mul(x,y)

    elif options == "e" or options == "E" :
        print("Program ended")
        break
        
