
def main():
    test_lista_eliminarea_duplicatelor()
    test_verificare_ordine_crescatoare()
    l=[]
    optiune = input("""
        Alegeti una dintre urmatoarele variante:
        1. Citirea unei liste de numere intregi.
        2. Afisarea listei dupa eliminarea duplicatelor.
        3. Afisarea sumei primelor n elemente din lista.
        4. Verificarea daca toate numerele pozitive din lista sunt in ordine crescatoare.
        5. Afisarea listei obtinute prin inlocuirea nr. care apar o singura data cu numarul lor de divizori
        6. Iesire.
        """)
    while True:
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(lista_eliminarea_duplicatelor(l))
        elif optiune == "3":
            print(suma_primelor_n_elemente_pozitive_din_lista(l))
        elif optiune == "4":
            print(verificare_ordine_crescatoare(l))
        elif optiune == "5":
            pass
        elif optiune == "6":
            break
        else:
            print("Optiune gresita. Va rugam sa realegeti optiunea:")
        optiune = input("""
                Alegeti una dintre urmatoarele variante:
                1. Citirea unei liste de numere intregi.
                2. Afisarea listei dupa eliminarea duplicatelor.
                3. Afisarea sumei primelor n elemente din lista.
                4. Verificarea daca toate numerele pozitive din lista sunt in ordine crescatoare.
                5. Afisarea listei obtinute prin inlocuirea nr. care apar o singura data cu numarul lor de divizori
                6. Iesire.
                """)


def citire_lista():
    l=[]
    sir = input("Introduceti numerele rationale din lista, separate prin virgula: ")
    lista = sir.split(",")
    for x in lista:
        l.append(int(x))
    return l

def lista_eliminarea_duplicatelor(l):
    '''
    Eliminarea duplicatelor din lista
    :param l: lista de numere intregi
    :return: lista fara elemente duplicate
    '''
    list=[]
    for x in l:
        if x not in list:
            list.append(x)
    l = list

    return l

def test_lista_eliminarea_duplicatelor():
    assert lista_eliminarea_duplicatelor([1,1,2,3,4]) == [1,2,3,4]
    assert lista_eliminarea_duplicatelor([2,3,4,5,5]) == [2,3,4,5]
    assert lista_eliminarea_duplicatelor([1,2,3]) == [1,2,3]

def suma_primelor_n_elemente_pozitive_din_lista(l):
    '''
    Suma primelor n elemente pozitive din lista
    :param l: lista de numere intregi
    :return:
    '''
    n = input("Introduceti numarul n: ")
    sum = 0
    q = 0
    for x in l:
        if x >= 0 and q < int(n):
            sum = sum + x
            q = q + 1
    return sum

def verificare_ordine_crescatoare(l):
    '''
    Verificam daca elementele pozitive sunt scrise in ordine crescatoare
    :param l: lista de numere intregi
    :return: "DA", in caz afirmativ; "NU", in caz alternativ.
    '''
    q = 0
    for i in range (0, len(l)-1):
        if l[i] >= 0 and l[i+1] >= 0:
            if l[i] >= l[i+1]:
                q=q+1
    if q == 0:
        return("DA")
    else:
        return("NU")

def test_verificare_ordine_crescatoare():
    assert verificare_ordine_crescatoare([1,2,-3,4]) == "DA"
    assert verificare_ordine_crescatoare([2,1,-5,6]) == "NU"
    assert verificare_ordine_crescatoare([1,-2,3,-4,5]) == "DA"

main()
