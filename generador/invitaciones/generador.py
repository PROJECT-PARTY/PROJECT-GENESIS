
datos_correctos = False

while datos_correctos == False:    
    
    with open('../data.txt', encoding="utf8") as datatxt:
        data = datatxt.read().split("\n")
        datatxt.close()
        print("el nombre del proyecto es: "+data[0])
        print("la fecha del proyecto es: "+data[1])
        print("la hora del proyecto es: "+data[2])
        print("el lugar del proyecto es: "+ data[3])
        print("la ubicacion del lugar es: "+ data[4])
        print("la url de el lugar es: " + data[5])

    with open('../invitados.txt', encoding="utf8") as invitadostxt:
        invitados = invitadostxt.read().split("\n")
        invitadostxt.close()
        print("\n\n\nla lista de invitados es: -> " + str(invitados))
        
    print("\n\nlos datos son correctos? si=1 no=0")
    aux =  int(input("-> "))
    if aux == 0:
        datos_correctos = False
    else:
        datos_correctos = True

n=0

with open('../code.txt', encoding="utf8") as codetxt:
        code = codetxt.read()
        codetxt.close()

aux = 0
aux2 = 0
ninvitados =[]
for i in invitados:
    aux += 1
    
aux /= 2

while aux>aux2:
    aux2 += 1
    ninvitados.append(aux2)
    
print(ninvitados)

for i in ninvitados:
    print(invitados[n] + " " + invitados[n+1])
    doc_name = data[0] + "-" + invitados[n] + ".html"
    
    new_code = code.replace("?NAME?", invitados[n])
    
    n += 1
    
    new_code = new_code.replace("?PROJECT?", data[0])
    new_code = new_code.replace("?DATE?", data[1])
    new_code = new_code.replace("?TIME?", data[2])
    new_code = new_code.replace("?PLACE?", data[3])
    new_code = new_code.replace("?ADDRESS?", data[4])
    new_code = new_code.replace("?URL?", data[5])
    new_code = new_code.replace("?CSS?", invitados[n])
    

    with open(doc_name, "w", encoding="utf8") as invitacion:
        invitacion.write(new_code)
    
    n += 1