import itertools
from unittest import result

literals = {}

temp = []
valores = []

op1 = "{{p},{p'}}"
op2 = "{{q,p,p'}}"
op3 = "{{p',r',s'}, {q',p',s'}}"
op4 = "{{p,r',s'}, {q',p',s'}}"
op5 = "{{p',q',r'},{q,r',p},{p',q,r}}"
op6 = "{{p',q',r'},{q,r',p},{p',q,r}}"


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
                        temp.append([True, False])
                        literals[acu] = len(temp)-1

                acu = ""
            elif element != " ":
                acu += element
        if element == "}":
            count -= 1


def eliminateKeys(op):
    temp = op[1:(len(op)-1)]
    arreglo = temp.split("}")
    for i in range(len(arreglo)):
        arreglo[i] = arreglo[i].replace("{", "")
        arreglo[i] = arreglo[i].replace(" ", "")
        arreglo[i] = arreglo[i].split(",")
    arreglo.pop()
    for i in arreglo:
        j = 0
        while(j < len(i)):
            if(i[j] == ""):
                i.pop(j)
            j += 1
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
            valores.append(ordered_element)
            return True
    return False


def fuerzaBruta(expresionB):
    parse_input(expresionB)
    valores.clear()
    Result = evaluate(eliminateKeys(expresionB))
    print(Result)
    if (Result):
        for keys in literals.keys():
            if "'" in keys:
                print(keys, not valores[0][literals[keys]])
            else:
                print(keys, valores[0][literals[keys]])
    print("---------------------")


def select_literal(expresionB):
    for c in expresionB:
        for literal in c:
            return literal[0]


def parse_dpll(cnf):
    list = []
    a = cnf.split("{")
    tete = []
    for i in range(len(a)):
        if(a[i] != ""):
            f = a[i].replace("}", "")
            g = f.split(",")
            if (g[len(g)-1] == ""):
                g.remove("")
            elif (g[len(g)-1] == " "):
                g.remove(" ")
            tete.append(g)
    for i in tete:
        conj = set()
        for j in i:
            if("'" in j):
                conj.add((j[0:len(j)-1], False))
            else:
                conj.add((j, True))
        list.append(conj)
    return list


def dpll(cnf, assignments={}):

    if len(cnf) == 0:
        return True, assignments

    if any([len(c) == 0 for c in cnf]):
        return False, None

    l = select_literal(cnf)

    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals

    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals

    return False, None


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
    opcion = 0
    while(opcion != "3"):
        print("1) Fuerza bruta")
        print("2) Algoritmo DPLL")
        print("3) Salir")
        opcion = input("\nOpcion: ")
        if (opcion == "1"):
            while(opcion != "g"):
                opcion = opDeterminadas()
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
        elif opcion == "2":
            while(opcion != "g"):
                opcion = opDeterminadas()
                if (opcion == "a"):
                    final = parse_dpll(op1)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                if (opcion == "b"):
                    final = parse_dpll(op2)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                if (opcion == "c"):
                    final = parse_dpll(op3)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                if (opcion == "d"):
                    final = parse_dpll(op4)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                if (opcion == "e"):
                    final = parse_dpll(op5)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                if (opcion == "f"):
                    final = parse_dpll(op6)
                    bol, cnf = dpll(final)
                    print(bol)
                    if (bol):
                        print(cnf)
                print("---------------------\n")


menu()
