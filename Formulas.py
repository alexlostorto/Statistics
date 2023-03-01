def parseList(item, log=True):
    if isinstance(item, list):
        if log:
            print(item)
        return item
    elif isinstance(item, str):
        item = item.replace('  ', ' ')
        if (', ' in item):
            item = item.split(', ')
        else:
            item = item.split(' ')
        if log:
            print(item)
        return item


def standardDeviation(dataset=[], log=False):
    dataset = parseList(dataset)

    n = len(dataset)
    xSum = 0
    xSumSquared = 0

    for x in dataset:
        xSum += int(x)
        xSumSquared += int(x)**2

    if log:
        print(((xSumSquared/n)-((xSum/n)**2))**(1/2))

    return ((xSumSquared/n)-((xSum/n)**2))**(1/2)


def skewness(mean, median, standardDeviation, log=True):
    if log:
        print((3 * (mean - median)) / standardDeviation)

    return (3 * (mean - median)) / standardDeviation


__all__ = [
    parseList,
    standardDeviation,
    skewness
]
