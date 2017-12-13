import simpleVector

def loadVectors(fileName):
    with open(fileName,"r") as myFile:
        lines = myFile.readlines()
        result = []
        for line in lines:
            try:
                x = simpleVector.Vector(line)
            except:
                result.append(None)
            else:
                result.append(x)
    return result





if __name__ == "__main__":
    pass
    #test = loadVectors("values.txt")
    #print(len(test))
    #print(test)
