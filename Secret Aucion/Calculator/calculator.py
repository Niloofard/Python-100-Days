def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
n1=0
is_set_n1=False
while 1:
    reset= True
    while reset == True:
        if is_set_n1 == False:
            n1= int(input ("What is the first number?"))
        op= input ("pich an Operation? \n 1. +\n 2. -\n 3. *\n 4. /\n")
        n2=int(input ("What is the second number?"))
        if op== "+":
            result=add(n1,n2)
            print(result)
            dec = input(f"Type y to continue with {result} or Type n to start a new calculation:").lower()
            if dec== "n":
                reset= False
            elif dec== "y":
                n1=result
                is_set_n1=True
                reset = False

        if op== "-":
            result=subtract(n1,n2)
            print(result)
            dec = input(f"Type y to continue with {result} or Type n to start a new calculation:").lower()
            if dec== "n":
                reset= False
            elif dec== "y":
                n1=result
                is_set_n1=True
                reset = False
        if op== "/":
            result=divide(n1,n2)
            print(result)
            dec = input(f"Type y to continue with {result} or Type n to start a new calculation:").lower()
            if dec== "n":
                reset= False
            elif dec== "y":
                n1=result
                is_set_n1=True
                reset = False
        if op== "*":
            result=multiply(n1,n2)
            print(result)
            dec = input(f"Type y to continue with {result} or Type n to start a new calculation:").lower()
            if dec== "n":
                reset= False
            elif dec== "y":
                n1=result
                is_set_n1=True
                reset = False







