#! /usr/bin/env python3.4

#Nithin Varadharajan ECE 364 Fall 2017



#Problem 1
def find(pattern):
    with open('sequence.txt', 'r') as myFile:
        content = myFile.read()
        result = []
        for num in range(len(content)):
            test=True
            patterntest=""
            if((len(content)-num) < len(pattern)):
                break
            for x in range(len(pattern)):
                if ((pattern[x] == content[x+num]) or (pattern[x] == 'X')):
                    patterntest+=content[x+num]
                else:
                    test=False
                    break
            if(test==True):
                result.append(patterntest)
    return result

#Problem 2
def getStreakProduct(sequence, maxSize, product):
    result=[]
    for c in range(len(sequence)):
        for size in range(2,maxSize+1):
            if((len(sequence)-c) < size):
                break
            product1=1
            seq=""
            for x in range(size):
                product1*=int(sequence[x+c])
                seq+=sequence[x+c]
            if(product1 == product):
                result.append(seq)


    return result


#Problem 3
def writePyramids(filePath, baseSize, count, char):
    with open(filePath, 'w') as myFile:
        lvls=(baseSize/2)+0.5

        for x in range(int(lvls)):
            star=1+(x*2)
            space=" "*int(((baseSize-star)/2))
            stars=char*star
            content=space+stars+space
            contentres=""
            for y in range(count):
                if(y != count-1):
                    contentres+=content+" "
                else:
                    contentres+=content+"\n"
            myFile.write(contentres)


#Problem 4
def getStreaks(sequence, letters):
    result=[]
    x=0
    while (x < len(sequence)):
        seq=""
        if(sequence[x] in letters):
            seq+=sequence[x]
            x+=1
            while(sequence[x] == sequence[x-1]):
                seq+=sequence[x]
                x+=1
                if(x >= len(sequence)):
                    break
            result.append(seq)
        else:
            x+=1
    return result

def findNames(nameList, part, name):
    result=[]
    name=name.strip()
    name=name.upper()
    if(part == "L"):
        strings=[]
        for names in nameList:
            first, last = names.split()
            last=last.strip()
            last=last.upper()
            strings.append(last)
        for x in range(len(strings)):
            if( name == strings[x]):
                result.append(nameList[x])
    elif(part == "F"):
        strings=[]
        for names in nameList:
            first, last = names.split()
            first=first.strip()
            first=first.upper()
            strings.append(first)
        for x in range(len(strings)):
            if( name == strings[x]):
                result.append(nameList[x])
    elif(part == "FL"):
        stringf=[]
        stringl=[]
        resf=[]
        resl=[]
        for names in nameList:
            first, last = names.split()
            first=first.strip()
            first=first.upper()
            last=last.strip()
            last=last.upper()
            stringf.append(first)
            stringl.append(last)
        for x in range(len(stringf)):
            if( name == stringf[x]):
                resf.append(x)
        for x in range(len(stringl)):
            if( name == stringl[x]):
                resl.append(x)
        reso=resf + resl
        reso.sort()
        for x in reso:
            result.append(nameList[x])
    else:
        return []
    return result




def convertToBoolean(num, size):
    result=[]
    if(type(num) != int or type(size) != int):
        return []
    string=bin(num)
    string=string[2:]
    while(len(string) < size):
        string="0"+string
    for c in string:
        if(c == "0"):
            result.append(False)
        elif(c == "1"):
            result.append(True)
    return result

def convertToInteger(boolList):
    if type(boolList) is not list:
        return None
    if not boolList:
        return None
    res=""
    for item in boolList:
        if type(item) is not bool:
            return None
        if item is True:
            res+="1"
        else:
            res+="0"
    return int(res, 2)


if __name__ == "__main__":
    pass
    #res=find("314")
    #print(res)
    #res=getStreakProduct("14822", 5, 32)
    #print(res)
    #writePyramids('pyramid16.txt',  15, 5, '*')
    #res=getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "QT")
    #print(res)
    #res=findNames( ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield",
#"Johnson Cadence"],  "F", "Jofhnson")
    #res=convertToBoolean(135, 12)
    #print(res)
    #bList = [True, False, False, False, False, True, True, True]
    #print(convertToInteger(bList))