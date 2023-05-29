from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"Plotando/btc-usd-max.csv", index_col=0, parse_dates=True)

series2023 = series["01-01-2023":"07-04-2023"]
series2023["price"].plot(style='k.')
pyplot.show()
