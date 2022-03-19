import sys

def plus(x=0, y=0):
    return x+y

def minus(x=0, y=0):
    return x-y

def times(x=0, y=0):
    return x*y

def division(x=0, y=0):
    return x/y

def negation(x=0):
    return -x

def power(x=0, y=0):
    return x**y

def remind(x=0, y=0):
    return x%y

def inputops_or_exit():
    value = str(input("If you want to exit this program, plz type \"quit\" or \"exit\". \nPlz input operator(+,-,*,/,negation,**,%) : "))
    if value == "quit" or value == "exit":
        return sys.exit("Exit")
    else:
        return value

    
def inputvalue():
    try:
        input_operator = inputops_or_exit()
        
        x = int(input("Plz input intager x : "))
        operators = {
            "negation" : negation(x),
        }

        if(input_operator != "negation"):
            y = int(input("Plz input intager y : "))
            operators = {
                "+" : plus(x,y),
                "-" : minus(x,y),
                "*" : times(x,y),
                "/" : division(x,y),
                "negation" : negation(x),
                "**" : power(x,y),
                "%" : remind(x,y)
            }
        print(operators[input_operator])
    except ValueError:
        print("Input value error")
        print("====================")
    except SystemExit:
        print("Thank you to use")
        exit()
    except KeyboardInterrupt:
        print("Thank you to use")
        exit()
