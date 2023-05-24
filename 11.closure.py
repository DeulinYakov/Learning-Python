def getdata(filename):
    with open(filename) as fn:
        for line in fn:
            yield line


names = getdata("names.txt")
cities = getdata("cities.txt")
emails = getdata("emails.txt")
