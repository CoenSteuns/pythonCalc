import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        print "add"
    elif sys.argv[1] == "subtract":
        print "subtract"
    elif sys.argv[1] == "multiply":
        print "multiply"
    elif sys.argv[1] == "divide":
        print "divide"
    else:
        print "possible arguments: add subtract multiply divide"
        sys.exit();


def TryParse(x, Type = float):
    try:
        val = Type(x)
    except ValueError:
        return False
        pass
    return True
    pass

def GetNumInput(inputmsg):
    while True:
        num = raw_input(inputmsg)
        if not TryParse(num, int):
            if not TryParse(num, float):
                print "input is a string!"
            else:
                print "no floats allowed!"
        else:
            return int(num)

    pass

def Main():

    num1 = GetNumInput("number one: ")
    num2 = GetNumInput("number two: ")

    if len(sys.argv) > 1:
        if sys.argv[1] == "add":
            print num1 + num2
        elif sys.argv[1] == "subtract":
            print num1 - num2
        elif sys.argv[1] == "multiply":
            print num1 * num2
        elif sys.argv[1] == "divide":
            while num2 == 0:
                print "not dividing by 0"
                num2 = GetNumInput("Number two: ")
            print num1 / num2
        else:
            print "possible argument: add subtract multiply divide"
            sys.exit();
    pass

    again = raw_input("Try again? (Y)")
    if again is not "Y" and again is not "y":
        print "OK bye :D"
        sys.exit()
    else:
        Main()

Main()