#functions with outputs

def my_funciton():
    
    return 3*2

def format_name(f_name, l_name):
    formated_f_name=f_name.title()
    formatted_l_name=l_name.title()
    #print(f"{formated_f_name} {formatted_l_name}")
    return f"{formated_f_name} {formatted_l_name}"


print(format_name(f_name="AnGeLa", l_name="yu"))

def is_leap_year(year):
    if year %4 ==0:
        if year%100 ==0:
            if year %400 ==0:
                return True
                
            else:
                return False
        else:
            return True
    else:
        return False
   
is_leap_year(2024)

#docstrings: write nuktiline double quotes

"""lalalal
alalalal
lalala"""
#crtk +/

#calculator project
def calculator():
    print(""" _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")
    def add(n1,n2):
        return n1+n2
    def subtract (n1,n2):
        return n1-n2
    def multiply(n1, n2):
        return n1*n2
    def divide(n1,n2):
        return n1/n2

    operations={
        "+": add,
        "-": subtract,
        "*": multiply, 
        "/": divide }


    num1=float(input("what is the first number: "))
    should_accumulate= True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation=input("pick an operation: ")
        num2=float(input("what is the next number: "))
        answer=operations[operation](num1,num2)
        print(f"{num1} {operation} {num2}= {answer}")
        choice=input(f"type 'y' to calculating with the {answer}, type 'n to start a new calculation. ")
        if choice =="y":
            num1=answer
        else:
            should_accumulate=False
            print("\n"*50)
            calculator()

calculator()




