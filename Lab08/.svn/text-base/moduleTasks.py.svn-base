
from exModule import runNetworkCode
import re
from pathlib import Path

#Part I

def checkNetwork(**kwargs):

    try:
        runNetworkCode(**kwargs)
    except ConnectionError:
        raise
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is: {}".format(type(e).__name__)
    except:
        return False
    else:
        return True

#Part II

def isOK(signalName):
    m = re.search(r"^[A-Z]{3}\-[0-9]{3}$",signalName)
    if m:
        return True
    else:
        return False


def loadDataFrom(signalName, folderName):

    if not isOK(signalName):
        raise ValueError("{} is invalid.".format(signalName))
    else:
        new_filename = signalName + ".txt"
        path_string = folderName + "/" + new_filename
        my_path = Path(path_string)
        if not (my_path.exists() and my_path.is_file()):
            raise OSError("{} does not exist or may not be a valid file.".format(new_filename))
        else:
            with open(path_string,"r") as myFile:
                lines = myFile.readlines()
                num_non_floats = 0
                list_floats = []
                for line in lines:
                    m = re.search(r"^(([-+]?([0-9]+\.[0-9]*)|(\.[0-9]+))([Ee][+-]?[0-9]+)?)$",line)
                    if m:
                        list_floats.append(float(line))
                    else:
                        num_non_floats += 1
                return (list_floats, num_non_floats)

def isBounded(signalValues, bounds, threshold):

    if not signalValues:
        raise ValueError("Signal contains no data.")

    min_val , max_val = bounds

    num_out = 0

    for val in signalValues:
        if not (min_val <= val <= max_val):
            num_out += 1

    if num_out <= threshold:
        return True
    else:
        return False












if __name__ == "__main__":
    pass
    #print(checkNetwork(a="bar", val=[1,2,3], bar="hello"))
    #print(isOK("SWE-314"))
    #list1 , num1 = loadDataFrom("AFW-481", "Signals")
    #print(list1)
    #print(num1)
    #print(isBounded([3.00,1.51,.435,-1.00,5.00], (0.00,5.00), 0))
