def KSwapPermutation(arr,n,k):
    pos={}
    for i in range(n):
        pos[arr[i]]=i+1
    for i in range(n):
        if(k==0):
            break
        if(arr[i]==n-i):
            continue
        temp=pos[n-i]
        pos[arr[i]]=pos[n-i]
        pos[n-i]=i
        arr[temp],arr[i]=arr[i],arr[temp]
        k-=1
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    k=int(input())
    KSwapPermutation(arr,n,k)
    printArray(arr)