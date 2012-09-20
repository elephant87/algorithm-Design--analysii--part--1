from __builtin__ import len, int, open

f = open('//home/artsem/Documents/Algoritms/2 weeks/QuickSort.txt','r+')
a=[]
for b in f:
    a.append(int(b))

g=0
def quicksort(list,left,right):
    if right>=left:
        add(right-left)
        pivot=partition(list,left,right)
        quicksort(list,left,pivot-1)
        quicksort(list,pivot+1,right)

def add(i):
    global g
    g+=i

def partition(list,left,right):
    middle= int(right+left)/2
    p=list[left]+list[right]+list[middle]-max(max(list[left],list[right]),list[middle])-min(min(list[left],list[right]),list[middle])
    if list[right]==p:
        swap(list,left,right)
    if list[middle]==p:
        swap(list,left,middle)
    i=left+1
    j=left+1
    while j<=right:
        if list[j]<p:
            swap(list,j,i)
            i+=1
        j+=1
    swap(list,i-1,left)
    return i-1


def swap(list,i,j):
    t=list[i]
    list[i]=list[j]
    list[j]=t



A=[6,4,5,4,1,4]
quicksort(a,0,len(a)-1)
#quicksort(A,0,len(A)-1)
print a
print g