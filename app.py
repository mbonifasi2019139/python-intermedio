print("--------------Bienvenido------------")
number = int(input("Ingrese un numero de 1 a 10: "))

path = "./myfiles/"
myfile = open("./myfiles/tabla-n.txt", "wt")
result = 0

if number >= 1 and number <= 10:
    for iterator in range(1,11):
        result = iterator * number
        line = f"{number} x {iterator} = {result} \n"
        myfile.write(line )
else:
    print("no es un numero valido")
    exit(1)


myfile.close()
