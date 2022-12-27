import matplotlib.pyplot as plt


# Input any x or y coordinates here
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [18, 22, 18, 26, 22, 26, 24, 28, 26, 34]


def main():
    def getAverages():
        if len(x) == len(y) and len(x) >= 4:
            counter = 4
            x2 = []
            y2 = []
            while counter <= len(x):
                average = (y[counter-4] + y[counter-3] + y[counter-2] + y[counter-1]) / 4
                xValue = (x[counter-3] + x[counter-2]) / 2
                x2.append(xValue)
                y2.append(average)

                counter += 1
        else:
            print("Not enough values or amount isn't equal")

        return x2, y2

    x2, y2 = getAverages()

    for i in range(len(x2)):
        print(f"{x2[i]}, {y2[i]}")

    plt.plot(x, y, color='orange', linestyle='dashed', label='Original')
    plt.plot(x, y, color='black', linestyle='none', marker='x')
    plt.plot(x2, y2, color='black', linestyle='none', label='Averages', marker='o')
    plt.xlabel('Year')
    plt.ylabel('New houses')
    plt.title('Time series graph')

    plt.show()


if __name__ == '__main__':
    main()
