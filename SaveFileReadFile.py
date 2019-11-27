path = "database.txt"

def SaveFile(line):
    try:
        file = open(path, 'a', encoding='utf-8')
        file.writelines(line)
        file.writelines("\n")
        file.close()
    except:
        pass
def ReadFile():
    arrBooks = []
    try:
        file = open(path, 'r', encoding='utf-8')
        for line in file:
            data = line.strip()
            arr = data.split(";")
            arrBooks.append(arr)
        file.close()
    except:
        pass
    return arrBooks