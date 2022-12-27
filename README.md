<h1 align="center">Statistics</h1>

The program calculates the four point moving averages for a set of data and displays it on a graph using matplotlib.

## Set-up
```
pip install matplotlib
```

## How it Works 

1) The formula for calculating four point moving averages: Q1 + Q2 + Q3 + Q4 (Q for a yearly quarter). The formula is used to calculate all the moving averages and create 2 lists. One for the x values, one for the y values (the four point moving average).

``` python
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
```

2) The coordinate for each four point moving average is printed.

``` python
    for i in range(len(x2)):
        print(f"{x2[i]}, {y2[i]}")
```

## Screenshots
<p align="center"><img width="80%" src="https://github.com/alexlostorto/Statistics/raw/main/git_images/four_point_moving_averages.PNG" alt="four point moving averages displayed on a graph using matplotlib" /></p>

## Credits 

Everything is coded by Alex lo Storto

Licensed under the MIT License.
