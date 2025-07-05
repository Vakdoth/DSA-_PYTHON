
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,4,31,5,8,7,9,10]
res=bubblesort(arr)
print(res)                