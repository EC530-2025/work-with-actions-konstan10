from closestLocationGPS import closestLocationGPS

def testEmptyArrays():
    arr1 = []
    arr2 = [(-5.62852, -184.59028), (34.052235, -118.243683)]
    closestLocationGPS(arr1, arr2)

if __name__ == "__main__":
    testEmptyArrays()
