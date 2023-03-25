<h1 align="center">Statistics</h1>

This repository contains different **statistics** programs and **Formulas.py** which holds all types of **statistical formulae**.

## Table of Contents

<details>
  <summary>Click to expand</summary>
  
- [Moving Averages](#moving-averages)
  * [Set-up](#set-up)
  * [How it Works](#how-it-works)
  * [Screenshots](#screenshots)
- [Formulas](#formulas)
  * [Mean](#meandataset-roundto3-logtrue)
  * [Geometric Mean](#geometricmeandataset-roundto3-logtrue)
  * [Median](#mediandataset-roundto3-logtrue)
  * [Standard Deviation](#standarddeviationdataset-roundto3-logtrue)
  * [Skewness](#skewnessdataset-roundto3-logtrue)
- [Credits](#credits)
</details>

## Moving Averages

#### Set-up

```
pip install matplotlib
```

#### How it Works

1. The formula for calculating four point moving averages: Q1 + Q2 + Q3 + Q4 (Q for a yearly quarter). The formula is used to calculate all the moving averages and create 2 lists. One for the x values, one for the y values (the four point moving average).

```python
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

2. The coordinate for each four point moving average is printed.

```python
    for i in range(len(x2)):
        print(f"{x2[i]}, {y2[i]}")
```

#### Screenshots

<p align="center"><img width="50%" src="https://github.com/alexlostorto/Statistics/raw/main/git_images/four_point_moving_averages.png" alt="four point moving averages displayed on a graph using matplotlib" /></p>

## Formulas

#### mean(dataset=[], roundto=3, log=True):

1. The mean average is calculated by using sum() to add all values and then dividing by the number of values. The function takes a list of numbers as an input.

```python
return round(sum(dataset)/len(dataset), roundto)
```

#### geometricMean(dataset=[], roundto=3, log=True):

1. The geometric mean is calculated by multiplying all the values and then rooting by the number of values. The function takes a list of numbers as an input.

```python
product = 1
for data in dataset:
    product *= data

return round(product ** (1 / len(dataset)), roundto)
```

#### median(dataset=[], roundto=3, log=True):

1. The median is calculated by finding the middle index ((length + 1) / 2) and then returning that value if it is singular or the mean if the median is between two values. The function takes a list of numbers as an input.

```python
dataset.sort()

middle = (len(dataset) + 1) / 2
if type(middle) == int or middle.is_integer():
    median = dataset[int(middle-1)]
else:
    median = (dataset[math.ceil(middle)-1]+dataset[math.floor(middle)-1])/2
```

#### standardDeviation(dataset=[], roundto=3, log=True):

1. The standard deviation is calculated using the formula. The function takes a list of numbers as an input.

```python
n = len(dataset)
xSum = 0
xSumSquared = 0

for x in dataset:
    xSum += int(x)
    xSumSquared += int(x)**2

return ((xSumSquared/n)-((xSum/n)**2))**(1/2)
```

#### skewness(dataset=[], roundto=3, log=True):

1. The skewness is calculated using the formula. The function takes a list of numbers as an input.

```python
return round((3*(mean(dataset, 5)-median(dataset, 5)))/standardDeviation(dataset, 5), roundto)
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
