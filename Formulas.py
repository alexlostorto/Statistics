import math


def parseList(item, toNumber=True, log=True):
    def convert(item):
        for index, im in enumerate(item):
            if im.lstrip('-').isdigit():
                item[index] = int(im)
            elif im.isnumeric():
                item[index] = float(im)
        return item
    if isinstance(item, list):
        item = convert(item)
        if log:
            print(item)
        return item
    elif isinstance(item, str) or isinstance(item, int) or isinstance(item, float):
        item = str(item).replace('  ', ' ')
        item = item.replace(', ', ',')
        if item.startswith('[') and item.endswith(']'):
            item = item[1:-1]
        if (',' in item):
            item = item.split(',')
        else:
            item = item.split(' ')
        item = convert(item)
        if log:
            print(item)
        return item
    else:
        raise ValueError("Input is not a list")


def mean(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)

    if log:
        print(f"Mean: {round(sum(dataset)/ len(dataset),roundto)}")

    return round(sum(dataset)/len(dataset), roundto)


def geometricMean(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)

    product = 1
    for data in dataset:
        product *= data

    if log:
        print(f"Geometric mean: {round(product ** (1 / len(dataset)), roundto)}")

    return round(product ** (1 / len(dataset)), roundto)


def median(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)
    dataset.sort()

    middle = (len(dataset) + 1) / 2
    if type(middle) == int or middle.is_integer():
        median = dataset[int(middle-1)]
    else:
        median = (dataset[math.ceil(middle)-1]+dataset[math.floor(middle)-1])/2

    if log:
        print(f"Median: {round(median, roundto)}")

    return round(median, roundto)


def standardDeviation(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)

    n = len(dataset)
    xSum = 0
    xSumSquared = 0

    for x in dataset:
        xSum += int(x)
        xSumSquared += int(x)**2

    if log:
        print(f"Standard deviation: {((xSumSquared/n)-((xSum/n)**2))**(1/2)}")

    return ((xSumSquared/n)-((xSum/n)**2))**(1/2)


def skewness(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)

    if log:
        print(f"Skewness: {round((3*(mean(dataset, 5)-median(dataset, 5)))/standardDeviation(dataset, 5),roundto)}")

    return round((3*(mean(dataset, 5)-median(dataset, 5)))/standardDeviation(dataset, 5), roundto)


def spearmansRank(dataset1=[], dataset2=[], roundto=3, log=True):
    dataset1, dataset2 = parseList(dataset1, log=False), parseList(dataset2, log=False)

    def rank_simple(vector):
        return sorted(range(len(vector)), key=vector.__getitem__)

    def rankdata(a):
        n = len(a)
        ivec = rank_simple(a)
        svec = [a[rank] for rank in ivec]
        sumranks = 0
        dupcount = 0
        newarray = [0]*n
        for i in range(n):
            sumranks += i
            dupcount += 1
            if i == n-1 or svec[i] != svec[i+1]:
                averank = sumranks / float(dupcount) + 1
                for j in range(i-dupcount+1, i+1):
                    newarray[ivec[j]] = averank
                sumranks = 0
                dupcount = 0
        return newarray

    if len(dataset1) != len(dataset2):
        raise ValueError("Both lists must be the same length")

    ranked1 = rankdata(dataset1)
    ranked2 = rankdata(dataset2)

    sumDifSquared = 0
    for i in range(len(ranked1)):
        sumDifSquared += abs(ranked1[i]-ranked2[i])**2

    if log:
        print(f"Spearmans rank: {round(1-((6*sumDifSquared)/(len(dataset1)*(len(dataset1)**2-1))), roundto)}")

    return round(1-((6*sumDifSquared)/(len(dataset1)*(len(dataset1)**2-1))), roundto)


def pascal(rowNumber, log=True):
    row = []

    for i in range(rowNumber):
        newRow = []
        for l in range(len(row) - 1):
            newRow.append(row[l] + row[l+1])
        row = [1, *newRow, 1]

    if log:
        print(f"Row {rowNumber}: {' '.join(str(i) for i in row)}")

    return row


def nCr(before, after, version=2, log=True):
    if version == 1:
        if log:
            print(f"Coefficient: {pascal(before, False)[after]}")

        return pascal(before, False)[after]

    else:
        if log:
            print(f"Coefficient: {int(factorial(before, False) / (factorial(after, False) * factorial(before - after, False)))}")

        return int(factorial(before, False) / (factorial(after, False) * factorial(before - after, False)))


def factorial(integer, log=True):
    x = 1
    while integer > 1:
        x *= integer
        integer -= 1

    if log:
        print(f"Value: {x}")

    return x


def compoundInterest(base, multiplier, years, roundto=2, log=True):
    if log:
        print(f"Value after {years} years: {round(base * multiplier ** years, roundto):,}")

    return round(base * multiplier ** years, roundto)


def simpleInterest(base, multiplier, years, roundto=2, log=True):
    if log:
        print(f"Value after {years} years: {round(base + base * (multiplier - 1) * years, roundto):,}")

    return round(base + base * (multiplier - 1) * years, roundto)


__all__ = [
    parseList,
    mean,
    geometricMean,
    median,
    standardDeviation,
    skewness,
    spearmansRank,
    pascal,
    nCr,
    factorial,
    compoundInterest,
    simpleInterest
]
