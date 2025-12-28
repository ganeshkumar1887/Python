n1 = int(input("Enter number1::"))
n2 = int(input("Enter number2::"))
operator = input("Enter Operator::(+,-,*,/,//,% )= ")
match operator:
    case "+":
        print("sum=",n1+n2)
    case "-":
        print("subtract=",n1-n2)
    case "*":
        print("multiply=",n1*n2)
    case "/":
        print("Div=",n1/n2)
    case "//":
        print("Floor Division=",n1//n2)
    case "%":
        print("modulo=",n1%n2)
