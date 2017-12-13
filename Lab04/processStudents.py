import glob

def getCommonClasses(studentName1, studentName2):
    d2=getRegistration()
    if studentName1 not in d2 or studentName2 not in d2:
        return None
    test2=set(d2[studentName1]) & set(d2[studentName2])


    return test2

def getRegistration():
    names=glob.glob('Classes/ECE*')
    students=[]
    d={}
    for name in names:
        path=name
        with open(path, 'r') as myFile:
            for line in myFile:

                x=line.strip()
                trash, rest = name.split("/")
                classname, blah = rest.split(".")
                if x in d.keys():
                    if classname not in d[x]:
                        val2=d[x]
                        val2.append(classname)
                        d[x]=val2
                else:
                    l=[]
                    l.append(classname)
                    d[x]=l


    return d







if __name__ == "__main__":
    pass
    d=getRegistration()
    print(d)

    #print(getCommonClasses('Candie Frisbee', 'Neomi Flournoy'))
    #print(getCommonClasses('Marget Nagler', 'Eldridge Wiegand'))
    #print(getCommonClasses('Floria Uribe', 'Merideth Kind'))