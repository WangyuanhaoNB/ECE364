
import re

def parseXML(xmlnode):
    result=[]
    m = re.findall(r'([a-z]+)=\"(.+?)\"',xmlnode)

    return sorted(m)

def captureNumbers(sentence):
    m = re.findall(r'([-+]?[0-9]\.[0-9]+[eE][-+]?[0-9]+)|([-+]?[0-9]+\.[0-9]+)|([-+]?[0-9]+)',sentence) #
    result =[]
    for item in m:
        for x in item:
            if x:
                result.append(x)

    return result






if __name__ == "__main__":
    #xmlnode='<person    name="Irene Alder"     gender="female"      age="35"        blah="asdas dasdsad" />'
    #print(parseXML(xmlnode))

    #s="With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    #print(captureNumbers(s))
    pass