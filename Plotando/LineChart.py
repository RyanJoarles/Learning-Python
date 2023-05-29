
from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"Plotando/btc-usd-max.csv", index_col=0, parse_dates=True)

series["price"].plot()
pyplot.show()


