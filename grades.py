


def grades(name, hw, assign, test):
    name1 = name
    avg1 = ((hw/100) * 25)
    avg2 = ((assign/100) * 50)
    avg3 = ((test/100) * 100)

    newAvg1 = (avg1 + avg2 + avg3) / 3

    newAvg = format(newAvg1, '.2f')

    return f"{name1} {newAvg}%"

print(grades("hen", 13, 45, 69))