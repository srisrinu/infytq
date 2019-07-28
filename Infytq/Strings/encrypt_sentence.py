def encrypt_sentence(sentence):
    vowel_set = set("aeiouAEIOU")
    final_list=[]
    word=sentence.split()
    for i in range(0,len(word)):
        if((i%2)==0):
            final_list.append(word[i][::-1])
        else:
           vowels=list()
           consonants=list()
           for letter in word[i]:
               if letter in vowel_set:
                   vowels.append(letter)
               else:
                    consonants.append(letter)
           newstring="".join(consonants)+"".join(vowels)
           final_list.append(newstring)
    return(final_list)
if __name__=="__main__":
    sentence="the sun rises in the east"
    print(encrypt_sentence(sentence))