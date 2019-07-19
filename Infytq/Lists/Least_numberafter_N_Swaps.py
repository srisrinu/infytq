def minswap(arr,n,k):
    count=0
    for i in range(n):
        count+=1
    bad=0
    for i in range(count):
        if(arr[i]>k):
           bad+=1
    ans=bad
    j=count
    for i in range(n):
        if(j==n):
            break
        if(arr[i]>k):
            bad-=1
        if(arr[j]>k):
            bad+=1
            
        ans=min(ans,bad)
        j+=1
    return(ans)
if __name__=="__main__":
    arr=list(map(int,input().split()))
    n,k=map(int,input().split())
    print( minswap(arr,n,k))
