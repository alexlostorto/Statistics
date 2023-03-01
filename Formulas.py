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
    elif isinstance(item, str):
        item = item.replace('  ', ' ')
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


def mean(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)

    if log:
        print(f"Mean: {round(sum(dataset) / len(dataset), roundto)}")

    return round(sum(dataset) / len(dataset), roundto)


def median(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset, log=False)
    dataset.sort()

    middle = (len(dataset) + 1) / 2
    if type(middle) == int or middle.is_integer():
        median = dataset[int(middle-1)]
    else:
        median = (dataset[math.ceil(middle)-1] +
                  dataset[math.floor(middle)-1]) / 2

    if log:
        print(f"Median: {round(median, roundto)}")

    return round(median, roundto)


def standardDeviation(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset)

    n = len(dataset, log=False)
    xSum = 0
    xSumSquared = 0

    for x in dataset:
        xSum += int(x)
        xSumSquared += int(x)**2

    if log:
        print(f"Standard deviation: {((xSumSquared/n)-((xSum/n)**2))**(1/2)}")

    return ((xSumSquared/n)-((xSum/n)**2))**(1/2)


def skewness(dataset=[], roundto=3, log=True):
    dataset = parseList(dataset)

    if log:
        print(f"Skewness: {round((3 * (mean(dataset, 5) - median(dataset, 5))) / standardDeviation(dataset, 5), roundto)}")

    return round((3 * (mean(dataset, 5) - median(dataset, 5))) / standardDeviation(dataset, 5), roundto)


__all__ = [
    parseList,
    mean,
    median,
    standardDeviation,
    skewness
]
