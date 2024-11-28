def calcule(num1,operator,num2):
    int(num1)
    int(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return num1 % num2

print(calcule(2,"+",4))
print(calcule(20,"-",4))
print(calcule(50,"*",4))
print(calcule(60,"/",4))
print(calcule(15,"%",4))