def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {"+":add,"-":subtract,"*":multiply,"/":divide}

def calculator():
    num_1 = float(input("Enter the first number: "))
    comulative_flag = True
    while comulative_flag:
        for symbol in operations:
            print(symbol,"\n")
        chosed_op= input("Please choose the operation you want to:")
        num_2 = float(input("Enter the second number: "))
        result = operations[chosed_op](num_1,num_2)
        print(f"{num_1} + {num_2} = {result}")
        choice = input(f"Type 'y' if you want to continue with {result} or 'n' if you want to reset the calculator: ").lower()
        if choice == "y":
            num_1 = result
        else:
            print("\n" * 20)
            calculator()
calculator()






