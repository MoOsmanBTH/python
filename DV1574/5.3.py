import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dts

fig, ax = plt.subplots()
ax.set_title("Övning 3")
ax.set_ylabel("Dagsnotering (SEK)")
ax.set_xlabel("Datum")
x = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']

datetime_x = [datetime.datetime.strptime(item, '%Y-%m-%d') for item in x]

dates_x = [dts.date2num(item) for item in datetime_x]    

y = [772.56, 776.43, 776.48, 776.86, 775.08]

days = dts.DayLocator()
ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(dts.DateFormatter("%Y-%m-%d"))
ax.plot(dates_x, y)
ax.set_xlim(dates_x[0], dates_x[-1])
fig.autofmt_xdate()
plt.show()