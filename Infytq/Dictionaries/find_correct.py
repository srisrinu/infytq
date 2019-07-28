def find_correct(dictionary):
    result={"CORRECT":0,"ALMOST CORRECT":0,"WRONG":0}
    for (key,value) in dictionary.items():
          c=0
          if(key==value):
              result["CORRECT"]+=1
          elif(key!=value):
              for i in range(len(key)):
                  for i1 in range(i,i+1):
                      if(key[i]!=value[i1]):
                          c+=1
              if(c>0 and c<=2):
                  result["ALMOST CORRECT"]+=1
              elif(c>=3):
                  result["WRONG"]+=1
    return(list(result.values()))
if __name__=="__main__":
    dictionary={"THEIR":"THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
    print(find_correct(dictionary))
    
    