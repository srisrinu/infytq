def common_characters(str1,str2):
    l=[]
    for stri in str1[0:]:
        if(stri in str2  ) :
            l.append(stri)
    return("".join(l))
if __name__=="__main__":
    str1=input()
    str2=input()
    print(common_characters(str1, str2))