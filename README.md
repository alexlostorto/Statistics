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
  * [Spearmans Rank](#spearmansrankdataset1-dataset2-roundto3-logtrue)
  * [Pascal's Triangle](#spearmansrankdataset1-dataset2-roundto3-logtrue)
  * [nCr](#spearmansrankdataset1-dataset2-roundto3-logtrue)
  * [Factorial](#spearmansrankdataset1-dataset2-roundto3-logtrue)
  * [Compound Interest](#spearmansrankdataset1-dataset2-roundto3-logtrue)
  * [Simple Interest](#spearmansrankdataset1-dataset2-roundto3-logtrue)
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

1. Skewness is calculated using the formula. The function takes a list of numbers as an input.

```python
return round((3*(mean(dataset, 5)-median(dataset, 5)))/standardDeviation(dataset, 5), roundto)
```

#### spearmansRank(dataset1=[], dataset2=[], roundto=3, log=True):

1. Spearmans rank correlation coefficient is calculated using the formula. The function takes two lists of numbers as an input. Firstly, both datasets are ranked.

```python
# CREDIT: THIS CODE WAS TAKEN FROM STACKOVERFLOW
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
```

2. Then, I iterate through one list and find the difference squared for each data pair - I add this to the sumDifSquared total.

```python
sumDifSquared = 0
for i in range(len(ranked1)):
    sumDifSquared += abs(ranked1[i]-ranked2[i])**2
```

3. I substitute the relevant values into the spearmans rank correlation coefficient formula and return the output.

```python
return round(1-((6*sumDifSquared)/(len(dataset1)*(len(dataset1)**2-1))), roundto)
```

#### pascal(rowNumber, log=True):

1. Manually creates each line of Pascal's triangle until the desired row is reached. This function takes the row numbe as an input.

```python
row = []

for i in range(rowNumber):
    newRow = []
    for l in range(len(row) - 1):
        newRow.append(row[l] + row[l+1])
    row = [1, *newRow, 1]
```

#### nCr(before, after, version=2, log=True):

**Method 1:** This method uses the pascal() function previously created and returns the relevant index of that row. This function takes the values before and after the nCr function as inputs.

```python
return pascal(before, False)[after]
```

**Method 2:** This method uses the factorial() function to substitute the values before and after into the nCr formula. This function takes the values before and after the nCr function as inputs.

```python
return int(factorial(before, False) / (factorial(after, False) * factorial(before - after, False)))
```

#### factorial(integer, log=True):

1. Multiply the input by each integer below it. Only takes a positive integer input.

```python
x = 1
while integer > 1:
    x *= integer
    integer -= 1
```

#### compoundInterest(base, multiplier, years, roundto=2, log=True):

1. Calculates the compund interest. The function takes the base value, the multiplier, and then number of years as inputs.

```python
return round(base * multiplier ** years, roundto)
```

#### simpleInterest(base, multiplier, years, roundto=2, log=True):

1. Calculates the simple interest. The function takes the base value, the multiplier, and then number of years as inputs.

```python
return round(base + base * (multiplier - 1) * years, roundto)
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
