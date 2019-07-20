INT_MIN = -1000000
def MaxOfMin(arr,n):
    for k in range(1,n+1):
        maxOfmin=INT_MIN
        for i in range(n-k+1):
            min=arr[i]
            for j in range(k):
                if(arr[i+j]<min):
                    min=arr[i+j]
            if(min>maxOfmin):
                maxOfmin=min
        print(maxOfmin)
if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    MaxOfMin(arr, n)
    
        