import matplotlib.pyplot as plt

# LINE GRAPH

decades = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

big_mac_prices = [.45, .65, 1.6, 2.5, 2.24, 4.71, 4.89]

plt.plot(decades, big_mac_prices)

plt.savefig("plots/big_mac_plot.png")

plt.clf()

# SCATTER PLOT

hours_studied = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10]

exam_scores = [55, 60, 50, 70, 65, 80, 70, 80, 80, 90, 85, 85, 100, 100]

plt.scatter(hours_studied, exam_scores)

plt.savefig("plots/exam_scores.png")

plt.clf()

# HISTOGRAM

values = [7, 3, 1, 10, 9, 4, 8, 1, 10, 5, 3, 9, 10, 2, 6, 3, 1, 7, 2, 5]

plt.hist(values)

plt.savefig("plots/numbers.png")

plt.clf()

# -------------------------------------------------------------------

plt.hist(values, bins=5, edgecolor="black")

plt.savefig("plots/five_bins.png")

plt.clf()

# CUSTOMIZATION

data1 = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]

data2 = [
    92_228_531, 106_021_568, 123_202_660, 132_165_129, 151_325_798, 179_323_175,
    203_211_926, 226_545_805, 248_709_873, 281_421_906, 308_745_538, 331_449_281
]

plt.plot(data1, data2)

plt.savefig("plots/mystery_plot.png")

plt.clf()

# -------------------------------------------------------------------

ticks = range(50_000_000, 350_000_000, 25_000_000)

plt.plot(data1, data2)

plt.yticks(ticks)

plt.savefig("plots/unnamed_ticks.png")

plt.clf()

# -------------------------------------------------------------------

labels = [f"{tick // 1_000_000}" for tick in ticks]

plt.plot(data1, data2)

plt.yticks(ticks, labels)

plt.savefig("plots/named_ticks.png")

plt.clf()

# -------------------------------------------------------------------

plt.plot(data1, data2)

plt.yticks(ticks, labels)

plt.ylim(75_000_000, 350_000_000)

plt.savefig("plots/no_white_space.png")

plt.clf()

# -------------------------------------------------------------------

plt.plot(data1, data2)

plt.yticks(ticks, labels)

plt.ylim(75_000_000, 350_000_000)

plt.title("American Population Growth (in millions)")

plt.xlabel("Census Year")

plt.ylabel("Population")

plt.savefig("plots/population_chart.png")