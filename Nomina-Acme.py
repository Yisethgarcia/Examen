import datetime as dt

regisEmple = []
regisFaltas = {}
regisBonos = {}

def regisEmpleado(regisEmple):
    iden = input("Ingresa la identificación: ")
    nom = input("Ingresa el nombre: ")
    cargo = input("Ingresa el cargo: ")
    salario = float(input("Ingresa el salario: "))

    regisEmple.append([iden, nom, cargo, salario])
    print("El registro se ingresó correctamente")

def regisInasistencia():
    iden = input("Ingresa la identificación del empleado: ")
    
    # Verificar si el empleado está registrado
    if not any(empleado[0] == iden for empleado in regisEmple):
        print(f"No se encontró ningún empleado con la identificación {iden}.")
        return
    
    fecha = dt.datetime.now().date()
    
    if iden in regisFaltas:
        regisFaltas[iden].append(fecha)
    else:
        regisFaltas[iden] = [fecha]
    
    print(f"Inasistencia registrada para el empleado {iden} en la fecha {fecha}")

def regisBono():
    iden = input("Ingresa la identificación del empleado: ")
    
    # Verifica si el empleado está registrado
    if not any(empleado[0] == iden for empleado in regisEmple):
        print(f"No se encontró ningún empleado con la identificación {iden}.")
        return
    
    fecha = dt.datetime.now().date()
    valor = float(input("Ingresa el valor del bono: "))
    concepto = input("Ingresa el concepto del bono: ")
    
    bono = {'fecha': fecha, 'valor': valor, 'concepto': concepto}
    
    if iden in regisBonos:
        regisBonos[iden].append(bono)
    else:
        regisBonos[iden] = [bono]
    
    print(f"Bono registrado para el empleado {iden}: {concepto} por un valor de {valor} en la fecha {fecha}")

def calculoNomina():
    for empleado in regisEmple:
        iden, nom, cargo, salario = empleado
        
        #Descuentos
        descuento_salud = salario * 0.04
        descuento_pension = salario * 0.04
        total_descuentos = descuento_salud + descuento_pension
        
        #Salario
        salario_neto = salario - total_descuentos
        
        #Se suman los bonos registrados
        total_bonos = sum(bono['valor'] for bono in regisBonos.get(iden, []))
        
        # alario final
        salario_final = salario_neto + total_bonos
        
        print(f"\nEmpleado: {nom} (ID: {iden})")
        print(f"Salario: {salario}")
        print(f"Descuento por salud (4%): {descuento_salud:.2f}")
        print(f"Descuento por pensión (4%): {descuento_pension:.2f}")
        print(f"Total descuentos: {total_descuentos:.2f}")
        print(f"Salario: {salario_neto:.2f}")
        print(f"Total bonos: {total_bonos:.2f}")
        print(f"Salario final: {salario_final:.2f}")

def menu():
    while True:
        print("==BIENVENIDOS A LA NOMINA-ACME==")
        print("")
        print("1. Registrar empleado")
        print("2. Registrar inasistencia")
        print("3. Registrar bono")
        print("4. Calcular nómina")
        print("0. Salir")
        print("")
        opc = input("Ingresa la opción que desees: ")

        if opc == "1":
            regisEmpleado(regisEmple)
        elif opc == "2":
            regisInasistencia()
        elif opc == "3":
            regisBono()
        elif opc == "4":
            calculoNomina()
        elif opc == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()