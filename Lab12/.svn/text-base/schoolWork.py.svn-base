



def getStudentInfo():
    d = {}
    with open("university.txt", 'r') as f:
        next(f)
        coursenames = f.readline()
        courselist = coursenames.split()
        courselist = courselist[2:]
        next(f)
        for line in f:
            linelist = line.split("|")
            personlist = linelist[1:]
            name = linelist[0]
            name = name.strip()

            if name not in d:
                l=[]
                d[name]=l

            for index in range(len(courselist)):
                grade = personlist[index]
                grade = grade.strip()

                if grade != "-":
                    testtuple = (courselist[index], float(grade))
                    val2=d[name]
                    val2.append(testtuple)
                    d[name]=val2
    return d


def getClassInfo():
    x = {}
    d = getStudentInfo()

    for key, value in d.items():
        for classes in value:
            course,grade = classes

            if course not in x:
                l=[]
                x[course]=l

            testtuple = (key, grade)
            val2=x[course]
            val2.append(testtuple)
            x[course]=val2

    for key,value in x.items():
        val3=x[key]
        val3= sorted(val3)
        x[key]=val3

    return x

def getBestInCourse(course):
    y = getClassInfo()
    courseinfo = y[course]

    max1 = 0
    maxname= ""

    for vals in courseinfo:
        name, grade = vals
        if grade > max1:
            max1 = grade
            maxname = name

    return (maxname,max1)

def getCourseAverage(course):
    y = getClassInfo()
    courseinfo = y[course]

    sum = 0.0
    count = 0.0
    for vals in courseinfo:
        name, grade = vals
        sum += grade
        count += 1.0
    average1 = float(sum/count)
    average1 = round(average1,2)



    return average1

def getStudentGPA(name):
    y = getStudentInfo()
    studentinfo = y[name]

    sum = 0.0
    numhrs= 0
    d2 = {}
    with open("courses.txt", 'r') as f:
        next(f)
        next(f)
        for line in f:
            course, hour = line.split()
            course = course.strip()
            hour = hour.strip()

            d2[course]=int(hour)

    for classes in studentinfo:
        coursename1,grade1 = classes
        hours1 = d2[coursename1]
        numhrs += hours1
        temp1 = grade1 * hours1

        sum+=temp1
    temp2 = float(sum/numhrs)
    temp2 = round(temp2, 2)

    return temp2






















if __name__ == "__main__":
    pass
    #d = getStudentInfo()
    #print(d["Sadie Farkas"])
    #d1 = getClassInfo()
    #z=d1["ECE136"]
    #z1=d1["ECE139"]
    #print(getBestInCourse('ECE388'))
    #print(getCourseAverage("ECE475"))
    #print(getStudentGPA("Melba Gist"))
    #print("Asd")