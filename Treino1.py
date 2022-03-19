
def ordem(pont):
    return pont(2)


def lista(list):
    index=0

    result = []
    list=sorted(list)
    while index<(len(list)-1):
        first=list[index]
        second=list[index+1]
        dif=abs(first-second)
        pont=[dif, first, second]
        result.append(pont)
        index=index+1

    #result.sort(ordem)
    #print(type(result[0]))
    #print(type(result))
    #print(result)
    listaOrdenada = sorted(result)
    #print(listaOrdenada)
    imprime_list(listaOrdenada)


def imprime_list(listaOrdenada):
    i=0
    while i<len(listaOrdenada):
        print("({}, {})".format(listaOrdenada[i][1], listaOrdenada[i][2]))
        i=i+1



def exe():
    list = [2, 5, 15, 17, 20, 31, 6, 26]
    lista(list)



exe()