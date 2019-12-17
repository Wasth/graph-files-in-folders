import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('data.csv')
df.plot(kind='bar', x='tz_name', y='files_amount')
plt.show()
