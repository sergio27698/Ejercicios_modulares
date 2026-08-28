
from operaciones import resta,multiplicacion
from geometria import area_triangulo,area_circulo
from validador import es_positivo,es_par,contraseña_valida
from logica import mayor
from evaluador import evaluacion
from texto_utils import nombre_completo,contar_caracteres,primera_mayuscula,empieza_con_a
from conversor import dolares_a_bolivianos,temperatura
from finanzas import precio_con_descuento,calcular_iva
from tiempo import  horas_a_minutos
from auth import verificar_acceso

opcion=input("Que ejercicio quieres hacer?").strip()
match opcion:   
#ejercicio1
    case "1":
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese otro numero: "))
        resultado=resta(num1,num2)
        print(resultado)

#ejercicio2
    case "2":
        num1=float(input("Ingrese un numero: "))
        num2=float(input("Ingrese otro numero: "))
        resultado=multiplicacion(num1,num2)
        print(resultado)

#ejercicio3
    case "3":
        radio=(float(input("Ingrese el radio del circulo: ")))
        resultado=area_circulo(radio)
        print(f"el area del {radio} es {resultado}")


#ejercicio4
    case "4":
        base=float(input("Ingrese la base: "))
        altura=float(input("Ingrese la altura: "))
        resultado=area_triangulo(base,altura)
        print(f"el area del triangulos es {resultado:.2f}")

#ejercico5
    case "5":
        numero=int(input("Ingrese un numero: "))
        resultado=es_par(numero)
        print(f"es un {numero} par?:{resultado}")


#ejercicio6
    case "6":
        numero=int(input("Ingrese un numero: "))
        resultado=es_positivo(numero)
        print(f"el {numero} es positivo?:{resultado}")


#ejercico7
    case "7":
        a=int(input("Ingrese el numero: "))
        b=int(input("ingrese el numero: "))
        c=int(input("Ingrese el numero: "))
        resultado=logica.mayor(a,b,c)
        print(f"el numero mayor es {resultado}")

#ejercicio8
    case "8":
        nota=float(input("Ingrese la nota: "))
        resultado=evaluacion(nota)
        print(f"Con {nota} esta {resultado}")

#ejercicio9
    case "9":
        contraseña=input("Ingrese una contraseña: ")
        resultado=contraseña_valida(contraseña)
        print(f"la contraseña es valida? {resultado}")

#ejercicio10
    case "10":

        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        resultado=nombre_completo(nombre,apellido)
        print(f"Nombre completo: {resultado}")
#ejercicio11
    case "11":
        from texto_utils import contar_caracteres
        texto=input("Ingrese un texto: ")
        resultado=contar_caracteres(texto)
        print(f"La cantidad de caracteres es {resultado}")
#ejercicio12
    case"12":
        from texto_utils import primera_mayuscula
        palabra=input("Ingrese una palabra: ")
        resultado=primera_mayuscula(palabra)
        print(f"La primera letra en mayuscula es {resultado}")
#ejercicio13
    case"13":
        from texto_utils import empieza_con_a
        palabra=input("Ingrese una palabra: ")
        resultado=empieza_con_a(palabra)
        print(f"la palabra empieza con A?: {resultado}")
#ejercicio14
    case"14":
        from conversor import dolares_a_bolivianos
        dolares=float(input("Ingrese cuantos doalres: "))
        resultado=dolares_a_bolivianos(dolares)
        print(f"Los {dolares} $ son igual a {resultado}.2f bs")
#ejercicio15
    case"15":
        from conversor import temperatura
        celsius=float(input("Ingrwese la temperatura en  grados celsius: "))
        resultado=temperatura(celsius)
        print(f"{celsius} °C son igual a {resultado:.2f}°F")
#ejercicio16
    case"16":
        from finanzas import precio_con_descuento
        precio=float(input("Ingrese el precio: "))
        descuento=float(input("Ingrese el porcentaje de descuento"))
        resultado=precio_con_descuento(precio,descuento)
        print(f"El precio con descuento es {resultado:.2f}")
#ejercicio17
    case"17":
        from finanzas import calcular_iva
        precio=float(input("Ingrese el precio"))
        resultado=calcular_iva(precio)
        print(f"El IVA del producto es {resultado:.2f}")
#ejercicio18
    case"18":
        from tiempo import horas_a_minutos
        horas=float(input("Ingrese cuantas horas: "))
        resultado=horas_a_minutos(horas)
        print(f"{horas} son igual a {resultado} minutos")
#ejercicio19
    case"19":
        from auth import verificar_acceso
        usuario=input("Ingrese el usuario")
        clave=input("Imgrese su clave")
        if verificar_acceso(usuario,clave):
            print("Acceso concedido")
        else:
            print("Acceso denegado")    