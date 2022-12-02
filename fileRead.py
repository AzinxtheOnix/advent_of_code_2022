# Used to make input reading a bit more reusable
def readInput(fileName: str) -> list[str]:
    f = open(fileName, "r")
    array = []
    while(1):
        line = f.readline()
        if(line == ""):
            break
        array.append(line.replace("\n", ""))
    f.close()
    return array.copy()
    