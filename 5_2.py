

"""
Afghanistan,Asia,31.8,251772
Albania,Europe,3.0,11100
Algeria,Africa,38.3,919595
"""

continent = input("Enter a name of continent: ")
# continent = continent.title()
if continent != "Antarctica":
    infile = open("UN.txt", "r")
    found = False
    for line in infile:
        data = line.split(",")
        if data[1] == continent:
            print("Found: ", data[0])
            found = True
    print("Found?: ", found)
    if not found:
        print(continent + " is not in the dataset.")
else:
    print("There are no countries in Antartica")
