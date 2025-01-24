from closestLocationGPS import closestLocationGPS

def testFormat():
    try:
        arr1 = [(-90.53306, -108.09832, 103.02323), (37.7749, -122.4194, 44.9123), (79.75216, 97.65512, 28.9432)]
        arr2 = [("-5.62852", "-184.59028"), ("34.052235", "-118.243683")]
        closestLocationGPS(1, arr2)
        print("Pass")
    except Exception as e:
        print("Fail")


if __name__ == "__main__":
    testFormat()
