#! /usr/bin/env python3.4

#Nithin Varadharajan ECE 364 Fall 2017

import os

def getprojectcircuitdict():
    d = {}
    with open("projects.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            val, key = line.split()
            val=val.strip()
            key=key.strip()

            if key in d:
                val2=d[key]
                val2.append(val)
                d[key]=val2
            else:
                l=[]
                l.append(val)
                d[key]=l
    return d

def getcircuitprojectdict():
    d = {}
    with open("projects.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            key, val = line.split()
            val=val.strip()
            key=key.strip()

            if key in d:
                val2=d[key]
                val2.append(val)
                d[key]=val2
            else:
                l=[]
                l.append(val)
                d[key]=l
    return d


def getstudentiddict():
    d = {}
    with open("students.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            key, val = line.split("|")
            val=val.strip()
            key=key.strip()
            d[key]=val

    return d

def getstudentiddict2():
    d = {}
    with open("students.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            val, key = line.split("|")
            val=val.strip()
            key=key.strip()
            d[key]=val

    return d
def getComponentCountByProject(projectID):
    d=getprojectcircuitdict()

    if projectID not in d:
        return None
    circuit=d[projectID]

    res=set()
    ind=set()
    cap=set()
    tran=set()
    for item in circuit:
        path='Circuits/circuit_'+item+'.txt'
        with open(path, 'r') as myFile:
            next(myFile)
            next(myFile)
            next(myFile)
            next(myFile)
            content = myFile.readline()
            l=content.split(",")
            for comp in l:
                comp=comp.strip()
                if comp[0] is "R":
                    res.add(comp)
                elif comp[0] is "L":
                    ind.add(comp)
                elif comp[0] is "C":
                    cap.add(comp)
                elif comp[0] is "T":
                    tran.add(comp)
                else:
                    print("messed up somewhere")
    result=(len(res),len(ind),len(cap),len(tran))


    return result

def getComponentCountByStudent(studentName):
    d = getstudentiddict()

    if studentName not in d:
        return None
    id=d[studentName]
    test= True
    res=set()
    ind=set()
    cap=set()
    tran=set()

    for filename in os.listdir("Circuits/"):
        if filename.endswith(".txt"):
            path=os.path.join("Circuits/", filename)
            with open(path, 'r') as myFile:
                next(myFile)
                participants=myFile.readline()
                next(myFile)
                next(myFile)
                components=myFile.readline()

                l=participants.split(",")
                for x in range(len(l)):
                    l[x] = (l[x]).strip()

                if id in l:
                    test = False
                    l2=components.split(",")
                    for comp in l2:
                        comp=comp.strip()
                        if comp[0] is "R":
                            res.add(comp)
                        elif comp[0] is "L":
                            ind.add(comp)
                        elif comp[0] is "C":
                            cap.add(comp)
                        elif comp[0] is "T":
                            tran.add(comp)
                        else:
                            print("messed up somewhere")

    if test is True:
        return ()
    return (len(res),len(ind),len(cap),len(tran))

def getParticipationByStudent(studentName):
    d = getstudentiddict()

    if studentName not in d:
        return None
    id=d[studentName]
    result = set()
    for filename in os.listdir("Circuits/"):
        if filename.endswith(".txt"):
            path=os.path.join("Circuits/", filename)
            with open(path, 'r') as myFile:
                next(myFile)
                participants=myFile.readline()
                next(myFile)
                next(myFile)
                components=myFile.readline()

                l=participants.split(",")
                for x in range(len(l)):
                    l[x] = (l[x]).strip()

                if id in l:
                    trash , rest = filename.split("_")
                    cir , ext = rest.split(".")
                    cir = cir.strip()
                    d3=getcircuitprojectdict()
                    if cir in d3:
                        projects=d3[cir]
                        for pro in projects:
                            result.add(pro.strip())
    return result


def getParticipationByProject(projectID):
    d=getprojectcircuitdict()
    d2=getstudentiddict2()
    if projectID not in d:
        return None
    result = []
    circuits=d[projectID]
    for item in circuits:
        path='Circuits/circuit_'+item+'.txt'
        with open(path, 'r') as myFile:
            next(myFile)
            participants=myFile.readline()
            l=participants.split(",")
            for x in range(len(l)):
                l[x] = (l[x]).strip()

            for name in l:
                result.append(d2[name])
    return set(result)

def getProjectByComponent(components):
    d=getprojectcircuitdict()
    d2={}
    for pro in d.keys():
        circuit=d[pro]
        com=set()
        for item in circuit:
            path='Circuits/circuit_'+item+'.txt'
            with open(path, 'r') as myFile:
                next(myFile)
                next(myFile)
                next(myFile)
                next(myFile)
                content = myFile.readline()
                l=content.split(",")
                for comp in l:
                    comp=comp.strip()
                    com.add(comp)
        d2[pro]=com
    d3={}
    for comps in components:
        test2=set()
        for proj, compo in d2.items():
            if comps in compo:
                test2.add(proj)
        d3[comps]=test2
    return d3

def getStudentByComponent(components):
    d=getstudentiddict()
    d2={}
    d3={}
    for stu in d.keys():
        id=d[stu]
        val=set()
        for filename in os.listdir("Circuits/"):
            if filename.endswith(".txt"):
                path=os.path.join("Circuits/", filename)
                with open(path, 'r') as myFile:
                    next(myFile)
                    participants=myFile.readline()
                    next(myFile)
                    next(myFile)
                    component=myFile.readline()

                    l=participants.split(",")
                    for x in range(len(l)):
                        l[x] = (l[x]).strip()

                    if id in l:
                        l2=component.split(",")
                        for x in range(len(l2)):
                            l2[x] = (l2[x]).strip()
                        for y in l2:
                            val.add(y)
        d2[stu]=val
    for comp in components:
        test2=set()
        for student, compset1 in d2.items():
            if comp in compset1:
                test2.add(student)
        d3[comp]=test2
    return d3

def getComponentByStudent(studentNames):
    d=getstudentiddict()
    d2={}
    d3={}
    for stu in d.keys():
        id=d[stu]
        val=set()
        for filename in os.listdir("Circuits/"):
            if filename.endswith(".txt"):
                path=os.path.join("Circuits/", filename)
                with open(path, 'r') as myFile:
                    next(myFile)
                    participants=myFile.readline()
                    next(myFile)
                    next(myFile)
                    component=myFile.readline()

                    l=participants.split(",")
                    for x in range(len(l)):
                        l[x] = (l[x]).strip()

                    if id in l:
                        l2=component.split(",")
                        for x in range(len(l2)):
                            l2[x] = (l2[x]).strip()
                        for y in l2:
                            val.add(y)
        d2[stu]=val
    for name in studentNames:
        name=name.strip()
        d3[name]=d2[name]
    return d3
def getCommonByProject(projectID1, projectID2):
    d=getprojectcircuitdict()
    if projectID1 not in d or projectID2 not in d:
        return None
    d2={}
    for pro in d.keys():
        circuit=d[pro]
        com=set()
        for item in circuit:
            path='Circuits/circuit_'+item+'.txt'
            with open(path, 'r') as myFile:
                next(myFile)
                next(myFile)
                next(myFile)
                next(myFile)
                content = myFile.readline()
                l=content.split(",")
                for comp in l:
                    comp=comp.strip()
                    com.add(comp)
        d2[pro]=com
    test2=d2[projectID2] & d2[projectID1]
    test3=sorted(list(test2))

    return test3

def getCommonByStudent(studentName1, studentName2):
    d=getstudentiddict()
    if studentName1 not in d or studentName2 not in d:
        return None
    x=getComponentByStudent(set([studentName1, studentName2]))

    test2=x[studentName1] & x[studentName2]
    test3=sorted(list(test2))

    return test3

def getProjectByCircuit():
    d = {}
    with open("projects.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            key, val = line.split()
            val=val.strip()
            key=key.strip()

            if key in d:
                val2=d[key]
                if val not in val2:
                    val2.append(val)
                    val2=sorted(val2)
                    d[key]=val2
            else:
                l=[]
                l.append(val)
                d[key]=l
    return d

def getCircuitByStudent():
    d = getstudentiddict()
    d3={}
    for studentName in d.keys():
        id=d[studentName]
        result = set()
        for filename in os.listdir("Circuits/"):
            if filename.endswith(".txt"):
                path=os.path.join("Circuits/", filename)
                with open(path, 'r') as myFile:
                    next(myFile)
                    participants=myFile.readline()
                    next(myFile)
                    next(myFile)

                    l=participants.split(",")
                    for x in range(len(l)):
                        l[x] = (l[x]).strip()

                    if id in l:
                        trash , rest = filename.split("_")
                        cir , ext = rest.split(".")
                        cir = cir.strip()
                        result.add(cir)
        d3[studentName]=sorted(list(result))
    return d3

def getCircuitByStudentPartial(studentName):
    result={}
    d = getstudentiddict()
    d2=getCircuitByStudent()
    test = True
    for studentName1 in d.keys():
        if studentName1 == "Adams, Keith":
            pass
        last, first = studentName1.split(",")
        last=last.strip()
        first=first.strip()
        studentName=studentName.strip()
        if (studentName == last) or (studentName == first):
            test = False
            result[studentName1]=d2[studentName1]

    if test is True:
        return None

    return result











if __name__ == "__main__":
    #res=getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    #print(res)
    #res=getComponentCountByStudent("Alexander, Carlos")
    #print(res)
    #res=getParticipationByStudent('Harris, Anne')
    #print(res)
    #res=getParticipationByProject("8E56417E-0D81-4F43-8137-F1F7AA005654")
    #print(res)
    #res=getProjectByComponent({'T475.274', 'C471.636'})
    #print(res)
    #res=getStudentByComponent({'T475.274', 'C471.636'})
    #res=getComponentByStudent({'Carter, Sarah ', 'Green, Roy'})
    #print(res)
    #projectID1="082D6241-40EE-432E-A635-65EA8AA374B6"
    #projectID2="90BE0D09-1438-414A-A38B-8309A49C02EF"
    #res=getCommonByProject(projectID1, projectID2)
    #print(res)
    #res=getCommonByStudent('Carter, Sarah', 'Green, Roy')
    #print(res)
    #print(getProjectByCircuit())
    #print(getCircuitByStudentPartial("Green"))
    pass
