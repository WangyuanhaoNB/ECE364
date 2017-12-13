



def getFreeByName(names):
    d = {}
    with open("Availability.txt", 'r') as f:
        next(f)
        dates = f.readline()
        date = dates.split()
        date1 = []
        for x in range(2,len(date)):
            temp = date[x].strip()
            date1.append(temp)

        next(f)
        for line in f:
            worker = line.split("|")
            person = worker[0]
            person = person.strip()
            worker2=worker[1:]
            for x in range(len(worker2)):
                temp = worker2[x].strip()
                if temp is "1":
                    if person in d:
                        val2=d[person]
                        val2.append(date1[x])
                        d[person]=val2
                    else:
                        l=[]
                        l.append(date1[x])
                        d[person]=l

        res={}
        for name1 in names:
            res[name1]=d[name1]

            #print("test")
        return res

def getFreeByRange(date1, date2):
    trash, test1 = date1.split("/")
    trash, test2 = date2.split("/")
    test1 = int(test1)
    test2 = int(test2)
    if (test2 < test1):
        return None
    res = set()

    d = {}
    with open("Availability.txt", 'r') as f:
        next(f)
        dates = f.readline()
        date = dates.split()
        date1 = []
        for x in range(2,len(date)):
            temp = date[x].strip()
            date1.append(temp)

        next(f)
        for line in f:
            worker = line.split("|")
            person = worker[0]
            person = person.strip()
            worker2=worker[1:]
            for x in range(len(worker2)):
                temp = worker2[x].strip()
                if temp is "1":
                    if person in d:
                        val2=d[person]
                        val2.append(date1[x])
                        d[person]=val2
                    else:
                        l=[]
                        l.append(date1[x])
                        d[person]=l

    for names,values in d.items():
        free=True
        if (names == "Alcock, Frederica"):
            pass
        test6=[]
        for dates2 in values:
            trash, test3 = dates2.split("/")
            test3 = int(test3)
            test6.append(test3)
        for dates in range(test1,test2+1):
            if(dates not in test6):
                free=False

        if (free is True):
            res.add(names)





    return res


def getStateByCounty(county):
    d = {}
    with open("ZipCodes.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            temp1= line.split()
            if (len(temp1) > 3):
                state=temp1[0]+" "+temp1[1]
                state=state.strip()
                abbv=temp1[2].strip()
                zip1 =temp1[3].strip()
            else:
                state=temp1[0].strip()
                abbv=temp1[1].strip()
                zip1 =temp1[2].strip()

            if zip1 in d:
                val2=d[zip1]
                val2.append(zip1)
                d[zip1]=val2
            else:
                l=[]
                l.append(state)
                d[zip1]=l
    d2 = {}

    with open("LatLong.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            temp1= line.split()
            lat= temp1[0].strip()
            long= temp1[1].strip()
            zip2 =temp1[2].strip()
            temp5 = (lat, long)
            if temp5 in d2:
                val2=d2[temp5]
                val2.append(temp5)
                d2[temp5]=val2
            else:
                l=[]
                l.append(zip2)
                d2[zip1]=l
    return



def getCountByState(state):
    pass










if __name__ == "__main__":
    #names = {'Sang, Chanell', "Chock, Velvet"}
    #print(getFreeByName(names))
    #print(getFreeByRange("08/01", "08/05"))
    #print(getStateByCounty("Warren"))
    pass