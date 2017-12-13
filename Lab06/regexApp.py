

import re
from uuid import UUID



def getUrlParts(url):
    m = re.search(r"^http://([a-zA-Z0-9_.-]*)/([a-zA-Z0-9_.-]*)/([a-zA-Z0-9_.-]*)?.*$",url)
    x = (m.group(1),m.group(2),m.group(3))

    return x

def getQueryParameters(url):
    m = re.findall(r"([a-zA-Z0-9_.-]*)=([a-zA-Z0-9_.-]*)&?",url)

    return m

def getSpecial(sentence, letter):
    my_regex = r'\b({0}[a-zA-Z0-9_]*[^{0}\W]|[^{0}\W][a-zA-Z0-9_]*{0})\b'.format(letter)
    m = re.findall(my_regex,sentence,re.IGNORECASE)

    return m

def getRealMAC(sentence):
    m = re.search(r"([a-fA-F0-9]{2}(:|-)){5}[a-fA-F0-9]{2}", sentence, re.IGNORECASE)

    if m:
        return m.group(0)
    else:
        return None

def getRejectedEntries():
    result=[]
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+))[,; ]*$", line)
            if match:
                x=match.groups()
                test = x[0]
                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))
                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                    result.append(name)
                else:
                    result.append(str(test))


    return sorted(result)

def getEmployeesWithIDs():
    result={}
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+))[,; ]*(?P<id>\{?[0-9A-Fa-f]{8}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{12}\}?).*$", line)
            if match:
                x=match.groups()
                test = x[0]
                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))

                i = str(match.group("id"))
                value = str(UUID(i))

                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                    result[name] = value

                else:
                    name =str(test)
                    result[name] = value
    return result

def getEmployeesWithoutIDs():
    result = []
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+))[,; ]*((((\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})|([0-9]{3}\-[0-9]{3}\-[0-9]{4})|([0-9]{3}[0-9]{3}[0-9]{4}))[,; ]*([A-Za-z ]*))|(((\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})|([0-9]{3}\-[0-9]{3}\-[0-9]{4})|([0-9]{3}[0-9]{3}[0-9]{4}))[,; ]*)|([A-Za-z ]*))$", line)
            match3 = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+))[,; ]*$", line)
            if match and not match3:
                x=match.groups()
                test = x[0]

                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))

                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                else:
                    name =str(test)
                result.append(name)
    return sorted(result)


def getEmployeesWithPhones():
    result={}
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+)).*((\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})|([0-9]{3}\-[0-9]{3}\-[0-9]{4})|([0-9]{3}[0-9]{3}[0-9]{4})).*$", line)
            if match:
                x=match.groups()
                test = x[0]
                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))
                value2 = x[3]
                match4 = re.search(r"(?P<paren>\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})", str(value2))
                match5 = re.search(r"(?P<hyp>(?P<res1>[0-9]{3})\-(?P<res2>[0-9]{3})\-(?P<res3>[0-9]{4}))", str(value2))
                match6 = re.search(r"(?P<none>(?P<res1>[0-9]{3})(?P<res2>[0-9]{3})(?P<res3>[0-9]{4}))", str(value2))

                if match4 :
                    final = value2
                elif match5:
                    res1 = match5.group("res1")
                    res2 = match5.group("res2")
                    res3 = match5.group("res3")
                    final = "(" + res1 + ")" + " " + res2 + "-"+ res3
                elif match6:
                    res1 = match6.group("res1")
                    res2 = match6.group("res2")
                    res3 = match6.group("res3")
                    final = "(" + res1 + ")" + " " + res2 + "-"+ res3


                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                else:
                    name =str(test)

                result[name] = final
    return result

def getEmployeesWithStates():
    result={}
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+)).*?([a-zA-Z ]+)$", line)
            if match:
                x=match.groups()
                test = x[0]
                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))
                value2 = x[3]

                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                else:
                    name =str(test)

                result[name] = value2
    return result


def getCompleteEntries():
    result={}
    with open("Employees.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^(([a-zA-z]+\s[a-zA-z]+)|([a-zA-z]+,\s[a-zA-z]+))[,; ]*(?P<id>\{?[0-9A-Fa-f]{8}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{4}-?[0-9A-Fa-f]{12}\}?)[,; ]*(?P<phone>(\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})|([0-9]{3}\-[0-9]{3}\-[0-9]{4})|([0-9]{3}[0-9]{3}[0-9]{4}))[,; ]*(?P<state>[A-Za-z ]+)$", line)
            if match:
                x=match.groups()
                test = x[0]
                match2 = re.search(r"(?P<last>[A-Za-z]+),\s(?P<first>[A-Za-z]+)", str(test))

                i = str(match.group("id"))
                value = str(UUID(i))


                value2 = match.group("phone")
                match4 = re.search(r"(?P<paren>\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})", str(value2))
                match5 = re.search(r"(?P<hyp>(?P<res1>[0-9]{3})\-(?P<res2>[0-9]{3})\-(?P<res3>[0-9]{4}))", str(value2))
                match6 = re.search(r"(?P<none>(?P<res1>[0-9]{3})(?P<res2>[0-9]{3})(?P<res3>[0-9]{4}))", str(value2))


                if match4 :
                    final = value2
                elif match5:
                    res1 = match5.group("res1")
                    res2 = match5.group("res2")
                    res3 = match5.group("res3")
                    final = "(" + res1 + ")" + " " + res2 + "-"+ res3
                elif match6:
                    res1 = match6.group("res1")
                    res2 = match6.group("res2")
                    res3 = match6.group("res3")
                    final = "(" + res1 + ")" + " " + res2 + "-"+ res3

                if match2:
                    last = match2.group("last")
                    first = match2.group("first")
                    name = first + " " + last
                else:
                    name =str(test)

                result[name] = (value, final, match.group("state"))
    return result









if __name__ == "__main__":
     #url = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
     #print(getUrlParts(url))
     #url = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
     #print(getQueryParameters(url))
     #s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
     #print(getSpecial(s, "t"))
     #test="hdgh_dfgd---fg\ndfg58:1c:0A:6e:39:4Ddfgdfg5.6_756756"
     #print(getRealMAC(test))
     #print(getRejectedEntries())
     #print(getEmployeesWithIDs())
     #print(getEmployeesWithoutIDs())
     #print(getEmployeesWithPhones())
     #print(getEmployeesWithStates())
     #print(getCompleteEntries())
     pass

