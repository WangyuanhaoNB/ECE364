


class Entry:
    def __init__(self, k=0, v=""):
        if ( not isinstance(k,int)):
            raise TypeError("k must be a int!!")
        if ( not isinstance(v,str)):
            raise TypeError("v must be a string!!")

        self.key = k
        self.value = v

    def __str__(self):
        return "("+str(self.key)+': "'+str(self.value)+'")'

    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:
    def __init__(self, name):
        if name is "":
            raise ValueError("Name is empty!!")
        self._name = name
        self._entrySet = set()

    def __str__(self):

        resnum = len(self._entrySet)

        if(resnum <= 9):
            resnum = "0"+str(resnum)
        return '["'+str(self._name)+'": '+resnum+' Entries]'

    def addEntry(self,entry):

        for elements in self._entrySet:
            key1 = elements.key

            if key1 == entry.key:
                raise ValueError("key of entry already exists in dict!")

        self._entrySet.add(entry)

    def removeEntry(self,entry):
        removed = False
        for elements in self._entrySet:
            key1 = elements.key

            if key1 == entry.key:
                removed = True
                self._entrySet.remove(elements)
                break
        if removed is False:
            raise KeyError("element, {} does not exist in dict!".format(str(entry)))

    def getEntry(self,key):
        found = False
        for elements in self._entrySet:
            if elements.key == key:
                found = True
                return elements
        if found is False:
            raise KeyError("entry with that key doesnt exist!")

    def getAsDictionary(self):
        d = {}
        for elements in self._entrySet:
            d[elements.key] = elements.value

        return d











if __name__ == "__main__":
    pass
    #x = Entry(42,"Answer, Everything")
    #print(x)
    #y = Lookup("Products")
    #print(y.getAsDictionary())
    #print(y)