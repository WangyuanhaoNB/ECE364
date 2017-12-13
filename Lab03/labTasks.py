#! /usr/bin/env python3.4

#Nithin Varadharajan ECE 364 Fall 2017


def getTotal(accounts):
    result = []
    for person in accounts:
        x = person.split(":")
        z=x[1]
        u=z.split()
        reso=0.0
        for index in range(len(u)):
            y = u[index].strip()
            y = u[index][1:]
            y = float(y)
            reso += y

        result.append(round(reso,2))
    return result

def getDoublePalindromes():
    result=[]
    palin=True
    for test in range(10,1000001):
        if(test == 1001):
            pass
        palin=True
        test = str(test)

        listtest=[]
        for c in test:
            listtest.append(c)
        listtestrev=listtest[:]
        listtestrev.reverse()
        strrevlist="".join(listtestrev)
        if(strrevlist != test):
            palin=False

        bintest=bin(int(test))
        bintest=bintest[2:]
        bintest = str(bintest)

        blisttest=[]
        for c in bintest:
            blisttest.append(c)
        blisttestrev=blisttest[:]
        blisttestrev.reverse()
        bstrrevlist="".join(blisttestrev)
        if(bstrrevlist != bintest):
            palin=False

        if(palin is True):
            result.append(int(test))


    return result




if __name__ == "__main__":
    pass
    #accounts = ["Nithin Vara: $1.00     $2.00   $3.00   $4.01  ", "Chris G:    $10.51    $22.49 $12.00   $5.33 $100.00"]
    #print(getTotal(accounts))
    #print(getDoublePalindromes())