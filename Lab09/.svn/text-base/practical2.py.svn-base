import re


def parseSimple(fileName):
    d={}
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*\"(.+?)\"\s*\,?$", line)
            if match:
                key=match.group(1)
                val=match.group(2)
                d[key]=val
    return d


def parseLine(fileName):
    d={}
    with open(fileName, 'r') as f:
        line = f.read()
        match = re.findall(r"\s*\"([a-zA-z0-9]+?)\"\s*\:\s*\"(.+?)\"\s*", line)
        for elements in match:
            key,val = elements
            d[key]=val

    return d


def parseComplex(fileName):
    d={}
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*\"(.+?)\"\s*\,?$", line)

            if match:
                x=match.groups()
                key = x[0]
                val = x[1]
                d[key]=val
            else:
                match2 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*((true)|(false))\s*\,?$", line)
                if match2:
                    x=match2.groups()
                    if x[1] == "true":
                        val = True
                    else:
                        val = False
                    key = x[0]
                    d[key]=val
                    pass
                else:
                    match3 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))\s*\,?$", line)

                    if match3:
                        x=match3.groups()
                        key = x[0]
                        val = float(x[1])
                        d[key]=val
                    else:
                        match4 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*([-+]?[0-9]+)\s*\,?$", line)
                        if match4:
                            x=match4.groups()
                            key = x[0]
                            val = int(x[1])
                            d[key]=val
    return d



def parseComposite(fileName):
    d={}
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*\"(.+?)\"\s*\,?$", line)

            if match:
                x=match.groups()
                key = x[0]
                val = x[1]
                d[key]=val
            else:
                match2 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*((true)|(false))\s*\,?$", line)
                if match2:
                    x=match2.groups()
                    if x[1] == "true":
                        val = True
                    else:
                        val = False
                    key = x[0]
                    d[key]=val
                    pass
                else:
                    match3 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))\s*\,?$", line)

                    if match3:
                        x=match3.groups()
                        key = x[0]
                        val = float(x[1])
                        d[key]=val
                    else:
                        match4 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*([-+]?[0-9]+)\s*\,?$", line)
                        if match4:
                            x=match4.groups()
                            key = x[0]
                            val = int(x[1])
                            d[key]=val
                        else:
                            match5 = re.search(r"^\s*\"([a-zA-z0-9]+?)\"\s*\:\s*(\[(\s*\"(.+?)\"\s*\,?)+\])\s*\,?$", line)

                            if match5:
                                x=match5.groups()
                                key = x[0]
                                test = x[1]
                                test2 = re.findall(r"\"(.+?)\"", test)
                                d[key] = test2

    return d


if __name__ == "__main__":
    print(parseSimple("simple.json"))
    print(parseLine("simple2.json"))
    print(parseComplex("complex.json"))
    print(parseComposite("composite.json"))