from closestLocationGPS import closestLocationGPS

def testEmptyArrays():
    try:
        arr1 = []
        arr2 = [(-5.62852, -184.59028), (34.052235, -118.243683)]
        closestLocationGPS(arr1, arr2)
        print("Pass")
    except Exception as e:
        print("Fail")

if __name__ == "__main__":
    testEmptyArrays()
