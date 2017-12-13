import moduleTasks

#Part III

def loadMultiple(signalNames, folderName, maxCount):
    d ={}

    for signalName in signalNames:
        try:
            list_vals , num_non_vals = moduleTasks.loadDataFrom(signalName, folderName)
        except (OSError,ValueError):
            d[signalName] = None
        else:
            if num_non_vals <= maxCount:
                d[signalName] = list_vals
            else:
                d[signalName] = []

    return d


def saveData(signalsDictionary, targetFolder, bounds, threshold):

    for k,v in signalsDictionary.items():
        try:
            bound = moduleTasks.isBounded(v, bounds, threshold)
        except ValueError:
            pass
        else:
            if bound:
                new_filename = k + ".txt"
                path_string = targetFolder + "/" + new_filename
                with open(path_string,"w") as myFile:

                    for val in v[:-1]:
                        final_str = "{:.3f}\n".format(val)
                        myFile.write(final_str)

                    final_str = "{:.3f}".format(v[-1])
                    myFile.write(final_str)
            else:
                pass



if __name__ == "__main__":
    pass
    #d = loadMultiple(["AFW-481","CIG-308","FPT-701"], "Signals", 10)
    #for k in d.keys():
    #    print(len(d[k]))

    #d["CIG-308"] = []

    #for k in d.keys():
    #    print(len(d[k]))

    #list1 , num1 = moduleTasks.loadDataFrom("FPT-701", "Signals")
    #print(num1)

    #saveData(d, "Signals2", (0.00,100.00), 1000)