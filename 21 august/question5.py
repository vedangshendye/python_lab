
data=[1,5,7,6,3,2,8,9,10,11]

def bubble(arr,size):
    for i in range(0,size):
        for j in range (0,size-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

# bubble(data,10)
# print("after bubble sort, array becomes:\n",data)

def mergesort(a, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(a, p, q)
        mergesort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    left = [a[p + i] for i in range(n1)] + [float('inf')]
    right = [a[q + 1 + i] for i in range(n2)] + [float('inf')]
    
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection(arr,size):
    
    for i in range(0,size):
        min=999999
        minindex=0
        for j in range(i,size):
            if arr[i]<min:
                min=arr[i]
                minindex=i
        
        temp=arr[i]
        arr[i]=min
        arr[minindex]=temp

inp=int(input("enter 1 for bubble sort,2for merge sort,3 for selection sort, 4 for insertion sort: "))

if inp==1:
    bubble(data,10)
elif inp==2:
    mergesort(data,0,9)

elif inp==3:
    selection(data,10)

elif inp==4:
    insertion_sort(data)

print("after sorting, array becomes:\n",data)
