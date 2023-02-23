def parseList(item):
    if isinstance(item, list):
        return item
    elif isinstance(item, str):
        item = item.replace('  ', ' ')
        if (', ' in item):
            item = item.split(', ')
        else:
            item = item.split(' ')
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


if __name__ == '__main__':
    standardDeviation("2 3 3 4 5 6", True)
