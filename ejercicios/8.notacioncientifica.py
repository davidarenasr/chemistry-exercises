print("Este codigo convierte un numero decimal a notacion cientifica, y viceversa, asegurese de separar su numero en noticion cientifica con e")
number = input("ingresa un numero: ")

try:
    number = float(number)
    print(number)
    

except:
  print("Ingresa un numero correcto, Ejemplo decimal 0.00045 o notacion cientifica 45e-9")



