from enum import Enum
import random

class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4

class Student:

    def __init__(self, ID, first, last, lvl):
        self.ID = ID
        self.firstName = first
        self.lastName = last
        if ( not isinstance(lvl, Level)):
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        self.level = lvl


    def __str__(self):
        return self.ID+", "+self.firstName+" "+self.lastName+", "+(self.level.name).capitalize()

class Circuit:

    def __init__(self, ID, resistors, capacitors, inductors, transistors):
        self.ID = ID
        if len(resistors) != 0:
            for items in resistors:
                if items[0] != "R":
                    raise ValueError("The resistors' list contain invalid components : {}.".format(items))
        self.resistors = resistors
        if len(capacitors) != 0:
            for items in capacitors:
                if items[0] != "C":
                    raise ValueError("The capacitors' list contain invalid components : {}.".format(items))
        self.capacitors = capacitors
        if len(inductors) != 0:
            for items in inductors:
                if items[0] != "L":
                    raise ValueError("The inductors' list contain invalid components : {}.".format(items))
        self.inductors = inductors
        if len(transistors) != 0:
            for items in transistors:
                if items[0] != "T":
                    raise ValueError("The transistors' list contain invalid components : {}.".format(items))
        self.transistors = transistors

    def __str__(self):

        resnum=len(self.resistors)
        if(resnum <= 9):
            resnum = "0"+str(resnum)
        else:
            resnum = str(resnum)

        capnum=len(self.capacitors)
        if(capnum <= 9):
            capnum = "0"+str(capnum)
        else:
            capnum = str(capnum)

        indnum=len(self.inductors)
        if(indnum <= 9):
            indnum = "0"+str(indnum)
        else:
            indnum = str(indnum)

        trannum=len(self.transistors)
        if(trannum <= 9):
            trannum = "0"+str(trannum)
        else:
            trannum = str(trannum)

        res = self.ID+": "+"(R = "+resnum+", C = "+capnum+", L = "+indnum+", T = "+trannum+")"

        return res
    def getDetails(self):
        tempr = sorted(self.resistors)
        tempc = sorted(self.capacitors)
        templ = sorted(self.inductors)
        tempt = sorted(self.transistors)
        res = self.ID+": "
        for items in tempr:
            res = res + items + ", "
        for items in tempc:
            res = res + items + ", "
        for items in templ:
            res = res + items + ", "
        for items in tempt:
            res = res + items + ", "
        res = res[:-2]

        return res

    def __contains__(self, item):
        if not isinstance(item, str):
            raise TypeError("The 'item' in 'item in Circuit' must be a string!")
        if item[0] != "R" and item[0] != "C" and item[0] != "L" and item[0] != "T":
            raise ValueError("{} must start with 'R','C','L', or 'T'".format(item))

        return (item in self.resistors) or (item in self.capacitors) or (item in self.inductors) or (item in self.transistors)

    def __add__(self, other):
        if isinstance(other, Circuit):
            for num in random.sample(range(10000,100000),1):
                new_num = str(num)
            tempr = list((set(self.resistors)).union((set(other.resistors))))
            tempc = list((set(self.capacitors)).union((set(other.capacitors))))
            templ = list((set(self.inductors)).union((set(other.inductors))))
            tempt = list((set(self.transistors)).union((set(other.transistors))))

            return Circuit(new_num,tempr,tempc,templ,tempt)

        elif isinstance(other, str):
            if other[0] != "R" and other[0] != "C" and other[0] != "L" and other[0] != "T":
                raise ValueError("{} must start with 'R','C','L', or 'T'".format(other))
            if other in self:
                return self

            if other[0] == "R":
                (self.resistors).append(other)
            elif other[0] == "C":
                (self.capacitors).append(other)
            elif other[0] == "L":
                (self.inductors).append(other)
            elif other[0] == "T":
                (self.transistors).append(other)

            return self
        else:
            raise TypeError("The 'other' in 'Circuit + other' must be a string or Circuit!")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, str):
            raise TypeError("The 'other' in 'Circuit - other' must be a string!")
        if other[0] != "R" and other[0] != "C" and other[0] != "L" and other[0] != "T":
            raise ValueError("{} must start with 'R','C','L', or 'T'".format(other))
        if other not in self:
            return self

        if other[0] == "R":
            (self.resistors).remove(other)
        elif other[0] == "C":
            (self.capacitors).remove(other)
        elif other[0] == "L":
            (self.inductors).remove(other)
        elif other[0] == "T":
            (self.transistors).remove(other)

        return self

class Project:
    def __init__(self, ID, participants,circuits):
        self.ID = ID
        if not participants:
            raise ValueError("participants list is empty!")
        for items in participants:
                if not isinstance(items,Student):
                    raise ValueError("Participants has an invalid element : {}!".format(items))

        self.participants = participants
        if not circuits:
            raise ValueError("circuits list is empty!")
        for items in circuits:
                if not isinstance(items,Circuit):
                    raise ValueError("circuits has an invalid element : {}!".format(items))
        self.circuits = circuits

    def __str__(self):
        circuitnum = len(self.circuits)
        if(circuitnum <= 9):
            circuitnum = "0"+str(circuitnum)
        else:
            circuitnum = str(circuitnum)

        parttnum = len(self.participants)
        if(parttnum <= 9):
            parttnum = "0"+str(parttnum)
        else:
            parttnum = str(parttnum)

        res=self.ID+": "+circuitnum+" Circuits, "+parttnum+" Participants"
        return res

    def getDetails(self):
        res = self.ID + "\n" + "\n"
        y = []
        for items in self.participants:
            y.append(str(items))
        partstr = "\n".join(sorted(y))
        f_partstr = "Participants:\n"+partstr + "\n" + "\n"
        x=[]
        for items in self.circuits:
            x.append(items.getDetails())
        circuitstr = "\n".join(sorted(x))
        f_circuitstr = "Circuits:\n" + circuitstr



        return res + f_partstr + f_circuitstr

    def __contains__(self, item):
        if isinstance(item,Circuit):
            idlist = []
            for circuit in self.circuits:
                idlist.append(circuit.ID)
            return item.ID in idlist
        elif isinstance(item,Student):
            sidlist = []
            for student in self.participants:
                sidlist.append(student.ID)
            return item.ID in sidlist

        elif isinstance(item, str):
            if item[0] != "R" and item[0] != "C" and item[0] != "L" and item[0] != "T":
                    raise ValueError("{} must start with 'R','C','L', or 'T'".format(item))

            res = False
            for circuit in self.circuits:
                if (item in circuit.resistors) or (item in circuit.capacitors) or (item in circuit.inductors) or (item in circuit.transistors):
                    res = True
            return res
        else:
            raise TypeError("The 'item' in 'item in Project' must be a Circuit, Student, or string!")


    def __add__(self, other):
        if isinstance(other,Circuit):
            if other in self.circuits:
                return self
            (self.circuits).append(other)
            return self
        elif isinstance(other, Student):
            if other in self.participants:
                return self
            (self.participants).append(other)
            return self
        else:
            raise TypeError("The 'other' in 'Project + other' must be a Circuit or Student!")

    def __sub__(self, other):
        if isinstance(other,Circuit):
            if other not in self.circuits:
                return self
            (self.circuits).remove(other)
            return self
        elif isinstance(other, Student):
            if other not in self.participants:
                return self
            (self.participants).remove(other)
            return self
        else:
            raise TypeError("The 'other' in 'Project - other' must be a Circuit or Student!")

class Capstone(Project):

    def __init__(self, ID, participants,circuits):
        for items in participants:
                if items.level.name != "senior":
                    raise ValueError("Student {} is not a senior!".format(str(items)))

        Project.__init__(self, ID, participants,circuits)

    def __add__(self, other):
        if isinstance(other, Student):
            if other.level.name != "senior":
                raise ValueError("Student {} is not a senior!".format(str(other)))
        Project.__add__(self,other)




if __name__ == "__main__":
    pass
    #x=Student("15487-79431", "John", "Smith", Level.freshman )
    #u = Student("25484-49431", "Jo", "Smi", Level.senior )
    #r = Student("55484-59451", "J", "S", Level.senior )
    #print(x)
    #y=Circuit("99887",['R436.943','R206.298'],[  'C261.054','C194.315', 'C668.027'],[],[])
    #print(y)
    #print(y.getDetails())
    #print('C261.054' in y)
    #print(('R200.000' + y).getDetails())
    #print(y.getDetails())
    #print((y -'R200.000' ).getDetails())
    #z = Circuit("99886",['R436.943','R'],[  'C45','C', 'C34.56'],["L"],["T663.350"])
    #print((z + y).getDetails())

    #v = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e",[x],[y])
    #print(v)
    #print(v.getDetails())
    #print(u in v)

    #v + x
    #print(v.getDetails())
    #v - u
    #print(v.getDetails())

    #d=Capstone("38753067-e3a8-4c9e-bbde-cd13165fa21e",[u],[y])
    #d+r
    #print(d.getDetails())
