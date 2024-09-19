from hillClimbing import*
import random




def simulatedAnnealing_reinas(n,states):
    current=make_table(n)
    cont=0

    while True:


        better=make_table(n)
        nmo_better=h_reinas(better,n)
        
        if nmo_better<=h_reinas(current,n):
            current=better
        
            

        if h_reinas(current,n)==0: break

        if cont == states:
            break
        cont+=1
    return [cont,current,h_reinas(current,n)]

resul=hillClimbing_reinas(8,10000)

print("num de iter: ",resul[0]," +++ h: ", resul[2])
for fila in resul[1]:
   print(fila)