import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

function_dict = {"+":add,
                 "-":subtract,
                 "*":multiply,
                 "/":divide
                 }
process="True"
print(art.logo)
num1 = float(input("Write the first number:  "))
while process:
    operation=input("What operation you would like to do?\n +   -   *   /\n")
    num2=float(input("Write the next number:  "))
    data=function_dict[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {data}")
    choice=input(f"Type 'y' to continue with {data}  ||  Type 'n' to start fresh\nYour choice:  ").lower()
    if choice == "y" :
        num1=data
    elif choice == "n" :
        print("\n"*20)
        print(art.logo)
        num1 = float(input("Write the first number:  "))
    else:
        print("\nWrong input......Restart calculator to use!!")
        break