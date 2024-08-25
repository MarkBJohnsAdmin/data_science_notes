# Basic Plots

> *Note - be sure to import the pyplot module in order to use these methods*

```py
import matplotlib.pyplot as plt
```

When you open this repository, if you want to code along or start your own project, make sure you open a `virtual environment` in your terminal:

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install matplotlib
```

If you clone this repository instead, you can just copy `requirements.txt`:

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Be sure to check your current version of Python, as if you have a newer version of Python you may need to replace "python" and "pip" with "python3" and "pip3". You can check you current version of Python with "python --version".

## Line Plots

With pyplot, you can visualize various plots and graphs by plugging in Python data into its library. The simplest plot you can make is the `line plot`, a simple graph that draws a line from point to point across and x and y axis. This is often used to track a simple data trend, for example, prices over time.

```py
decades = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

big_mac_prices = [.45, .65, 1.6, 2.5, 2.24, 4.71, 4.89]
```

To show this trend, use the "plot()" method on your `plt` option. There are a few parameters that plot can take, but for now let's just focus on x and y values:

```py
# plt.plot(x_vals, y_vals)

plt.plot(decades, big_mac_prices)

plt.savefig("plots/big_mac_plot.png")
```

This will create an image of your plot and place it in your specified directory, or the current directory if none in specified. In this case, I created a "plots" folder ahead of time and placed `big_mac_plot.png` inside it.

![big mac plot](basic_plots/plots/big_mac_plot.png)

The plt object only keeps track of one plot at a time, so when you're ready to start working on a new one, make sure to use the "clear figure" method to start over:

```py
plt.clf()
```

## Scatter Plots

Line graphs help to search for simple trends, but if you want to look for correlations between different types of data, it can be more useful to put the data into a `scatter plot`. These puts dots for each data point on the figure instead of drawing a line, so you can look for clusters to tell if data correlates.

```py
hours_studied = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10]

exam_scores = [55, 60, 50, 70, 65, 80, 70, 80, 80, 90, 85, 85, 100, 100]
```

This functions mostly the same, except you use the  `scatter` method instead of plot.

```py
plt.scatter(hours_studied, exam_scores)

plt.savefig("plots/exam_scores.png")

plt.clf()
```

![exam scores](basic_plots/plots/exam_scores.png)

Even without a clear trajectory, you can still see that a very clear relationship between more hours studied and a higher exam score.

## Histograms

If you're less worried about trajectories or relationships and instead want to check for how certain values are distributed, you can instead use a `histogram`. Histograms take in a set of values, and place them into "bins", or containers that hold values within a range. For example, say you have a collection of random numbers between 1 and 10, and want to see how the values are distributed. 

```py
values = [7, 3, 1, 10, 9, 4, 8, 1, 10, 5, 3, 9, 10, 2, 6, 3, 1, 7, 2, 5]

plt.hist(values)

plt.savefig("plots/numbers.png")

plt.clf()
```

![numbers](basic_plots/plots/numbers.png)

Now you can see there are three 1s, 3s, and 10s, two 2s, 5s, 7s, and 9s, and one 4, 6, and 8.

The `hist` method also takes in "bins" as a parameter if you want a custom bin value, but the default value is 10. If you want to get a more general idea of the data ranges, especially if there's a large amount of very different data values.

```py
plt.hist(values, bins=5, edgecolor="black") # added borders for readability

plt.savefig("plots/five_bins.png")

plt.clf()
```

![five bins](basic_plots/plots/five_bins.png)

So now each bin encapsulates two numbers instead of just one.

## Customization

It's not always obvious what a graph is for based on only the numbers, so there are various ways we can customize the figure we create. For starters, we have a new line graph tracking growth over time:

![mystery plot](basic_plots/plots/mystery_plot.png)

There's not a lot you can tell about this data just from the numbers, so we'll have to add some extra details in order to convey what it represents.

```py
data1 = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]

data2 = [
    92_228_531, 106_021_568, 123_202_660, 132_165_129, 151_325_798, 179_323_175,
    203_211_926, 226_545_805, 248_709_873, 281_421_906, 308_745_538, 331_449_281
]

plt.plot(data1, data2)

plt.savefig("plots/mystery_plot.png")
```

First, we need to fix the y axis. Our data includes hundreds of millions, but we're representing that with single digits and decimals. In order to actually represent the values, we can customize the "ticks". Ticks are the lines poking out of the axes with the labels, and pyplot typically places them automatically, but you can override the locations and values at the ticks. The first step is to think about how exactly we want to format it.

Let's start at 75 million and go to 350 million, in order to capture the whole range. We also want to illustrate any dramatic jumps properly, so let's have each of the ticks jump by 25 million. We can set this up pretty easily by using two Python concepts, the `range` function and `list comprehension`.

First, the range function is a built in Python utility that lets us quickly create an ordered list by specifying the beginning, ending, and increments of that list.

```py
range(start, end, step=1)
```

If no value is given for "step", it will default to 1, meaning that each subsequent value in the list will be one more than the previous value. Note that the "stop" value is not the last value in the list, it's the number that indicates when the range should stop. So `range(1, 5)` will return 1, 2, 3, 4, not 1, 2, 3, 4, 5. So to get a range of 50 million to 350 million, incrementing by 25 million, we can just plug those values into a range function, and use that range in our `yticks` method:

```py
ticks = range(50_000_000, 350_000_001, 25_000_000)

plt.yticks(ticks)
```

![unnamed ticks](basic_plots/plots/unnamed_ticks.png)

The numbers on the side still aren't a good indication of how big the numbers are, so we can create new display values with the next Python concept, list comprehension. This looks a bit more confusing but is still pretty simple, it's just an easy way to create a new list by manipulating an existing one, following this format:

```py
[function for item in list]
```

To execute this, take the list you want to start with and come up with a variable name that can apply to every item in that list. It's not uncommon to use a placeholder value like *i* or *_*, but it's best practice to pick something that's clearly connected to the list. Then determine what you want to do to each item in that list. As a quick example, say you have a list of numbers and you want to triple each of them.

```py
nums = [1, 2, 3, 4, 5]

print([num * 3 for num in nums]) # [3, 6, 9, 12, 15]
```

For our plot, we want to display our values by the millions, which we can do by simply dividing each value by 1 million. The fastest way to do this is to make a list comprehension for our "ticks" list, dividing every value by 1 million and converting it to a string. From there, just add that second list to the yticks method.

```py
labels = [f"{tick // 1_000_000}" for tick in ticks]

plt.yticks(ticks, labels)
```

![named ticks](basic_plots/plots/named_ticks.png)

> Here, "//" is for integer division. By default, Python uses floats - or decimals - for division, so 10 / 5 == 2.0, while 10 // 5 == 2.

Next, it's good practice to remove all the white space you can, by setting a "limit" to the axis. This lets you specify the starting and adding point of the specified axis, so we can cut off most of the empty space:

```py
plt.ylim(75_000_000, 350_000_000)
```

![no white space](basic_plots/plots/no_white_space.png)

And finally, we can add labels to everything.

```py
plt.title("American Population Growth (in millions)")

plt.xlabel("Census Year")

plt.ylabel("Population")
```

![population](basic_plots/plots/population_chart.png)

Compared to the completely unformatted plot:

![mystery plot](basic_plots/plots/mystery_plot.png)
