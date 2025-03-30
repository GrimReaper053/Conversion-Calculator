def mathematics():
    def add(x, y):
        return x + y 

    def subtract(x, y):
        return x - y 

    def multiply(x, y):
        return x * y 

    def divide(x, y): 
        return x / y
        
    stopTheProgram = ""

    operator = ["+","-","*","/"]
        
    while stopTheProgram.lower() != "n":
        
        whatOperatorToUse = str(input("""What operator do you want to use 
[1]: +
[2]: -
[3]: *
[4]: /
Please enter your choice here: """))
        
        if whatOperatorToUse in operator:
            try:
                x = int(input("\nPlease input your first number: "))
                y = int(input("Please input your second number: "))
            except ValueError:
                    print("\nInvalid input you have to put a number!")
            if whatOperatorToUse == "+":
                print(f"\nHere is your answer: {add(x, y)}")
            elif whatOperatorToUse == "-":
                print(f"\nHere is your answer: {subtract(x, y)}")
            elif whatOperatorToUse == "*":
                print(f"\nHere is your answer: {multiply(x, y)}")
            elif whatOperatorToUse == "/":
                try:
                    print(f"\nHere is your answer: {divide(x, y)}")
                except ZeroDivisionError:
                    print("\nYou can not divided by zero!")
            else:
                print("Invalid input!")
            
            stopTheProgram = input("\nDo you want to continue? (y/n): ")
            
        elif whatOperatorToUse not in operator:
            print("\nInvalid operator! Please choose from (+ - * /).")