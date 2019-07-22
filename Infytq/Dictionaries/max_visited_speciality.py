def max_visited_speciality(patient_medical_speciality,medical_speciality):
    result=[0]*len(medical_speciality)
    i=1
    while(i<len(patient_medical_speciality)):
        if(patient_medical_speciality[i]=="P"):result[0]=result[0]+1
        elif(patient_medical_speciality[i]=="O"):result[1]=result[1]+1
        else:result[2]=result[2]+1
        i+=2
    mv=max(result)
    pos=result.index(mv)
    if(pos==0):speciality="P"
    elif(pos==1):speciality="O"
    else:speciality="ENT"
    print(medical_speciality[speciality])
if __name__=="__main__":
    patient_medical_speciality=[101,"P",102,"O",302,"P",305,"P"]
    medical_speciality={"P":"Pediatrics","O":"Orthopedics","ENT":"ENT"}
    print(max_visited_speciality(patient_medical_speciality, medical_speciality))