import itertools
from unittest import result

literals = {}
valores=[]
temp = []

op1="{{p},{p'}}"
op2="{{q,p,p'}}"
op3="{{p',r',s'}, {q',p',s'}}"
op4="{{p,r',s'}, {q',p',s'}}"
op5="{{p',q',r'},{q,r',p},{p',q,r}}"
op6="{{p',q',r'},{q,r',p},{p',q,r}}"

def parse_input(input):
    count = 0
    acu = ""
    for element in input:
        if element == '{':
            count += 1
        elif count == 2:
            if element == "," or element == "}":
                if not(acu in literals):
                    if acu[0:1] in literals:
                        literals[acu] = literals[acu[0:1]]
                    else:
                        valores.append(False)
                        literals[acu] = len(valores)-1
                        temp.append([True, False])
                    
                acu = ""
            elif element != " ":
                acu += element
        if element == "}":
            count -= 1
        

def eliminateKeys(op):
    temp = op[1:(len(op)-1)]
    arreglo= temp.split("}")
    for i in range (len(arreglo)):
        arreglo[i]=arreglo[i].replace("{","")
        arreglo[i]=arreglo[i].replace(" ","")
        arreglo[i]=arreglo[i].split(",")
    arreglo.pop()
    for i in arreglo:
        j=0
        while(j < len(i)):
            if(i[j]==""):
                i.pop(j)
            j+=1
    return arreglo
            
            
def evaluate(formulab):
    cartesian = [element for element in itertools.product(*temp)]
    for ordered_element in cartesian:
        outer_res = True
        for arrays in formulab:
            res = False
            for elements in arrays:
                value = ordered_element[literals[elements]]
                if "'" in elements:
                    value = not value
                res = res or value
            outer_res = outer_res and res
        if outer_res:
            return True
    return False

def fuerzaBruta(expresionB):
    parse_input(expresionB)
    Result = evaluate(eliminateKeys(expresionB))
    print(Result)
    if (Result):
        print(valores)
    print("---------------------")

def opDeterminadas():
    print("Evaluar si la formula booleana es satisfacible")
    print("A) "+op1)
    print("B) "+op2)
    print("C) "+op3)
    print("D) "+op4)
    print("E) "+op5)
    print("F) "+op6)
    print("G) Salir")
    return input("\nOpcion: ").lower()
    
def menu():
    opcion=0
    while(opcion!="3"):
        print("1) Fuerza bruta")
        print("2) Algoritmo DPLL")
        print("3) Salir")
        opcion=input("\nOpcion: ")
        if (opcion == "1"):
            while(opcion!="g"):
                opcion=opDeterminadas()
                if (opcion == "a"):
                    fuerzaBruta(op1)
                if (opcion == "b"):
                    fuerzaBruta(op2)
                if (opcion == "c"):
                    fuerzaBruta(op3)
                if (opcion == "d"):
                    fuerzaBruta(op4)
                if (opcion == "e"):
                    fuerzaBruta(op5)
                if (opcion == "f"):
                    fuerzaBruta(op6)
                                
menu()