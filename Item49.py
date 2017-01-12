list_a = [67,45,2,13,1,998]
list_b = [89,23,33,45,10,12,45,45,45]

def selectionSort(list_a):
   for fillslot in range(len(list_a)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if list_a[location]>list_a[positionOfMax]:
               positionOfMax = location

       temp = list_a[fillslot]
       list_a[fillslot] = list_a[positionOfMax]
       list_a[positionOfMax] = temp

selectionSort(list_a)
selectionSort(list_b)
print('List A: ' + str(list_a))
print('List B: ' + str(list_b))
