
def uniqueCount(arr,n):
    c=0
    for i in arr[0:]:
        
        arr.remove(i)
        
        c+=1
        if(c==n):
            break
    return(len(set(arr)))
if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=int(input())
    print(uniqueCount(arr, n))