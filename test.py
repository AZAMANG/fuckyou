what =input("что делаем +; -; *; /; **; % ")
a =float(input("введите первое чило") )
b =float(input("введите второе чило") )
if what == "+":
    c = a + b
    print("результат" + str(c) )
elif what == "-":
    c = a - b
    print("результат" + str(c) )
elif what == "*":
    c = a * b
    print("результат" + str(c) )
elif what == "/":
    c = a / b
    print("результат" + str(c) )
elif what == "**":
    c = a ** b
    print("результат" + str(c) )
elif what == "%":
    c = a % b
    print("результат" + str(c) )
else:
    print("да ты заебал нету у меня такого,иди нахуй")
input()
