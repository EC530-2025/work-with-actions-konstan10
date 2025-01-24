from closestLocationGPS import closestLocationGPS

def testOutOfBounds():
    arr1 = [(-90.53306, -108.09832), (37.7749, -122.4194), (79.75216, 97.65512)]
    arr2 = [(-5.62852, -184.59028), (34.052235, -118.243683)]
    closestLocationGPS(arr1, arr2)

if __name__ == "__main__":
    testOutOfBounds()

