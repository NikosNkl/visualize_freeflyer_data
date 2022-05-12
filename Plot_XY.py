import pandas as pd
import matplotlib.pyplot as plt
import dateutil.parser
from matplotlib.ticker import FormatStrFormatter

df = pd.read_csv("data.txt", usecols=[0, 1, 2, 3, 4, 6, 8], names=['col1', 'col2', 'col3', 'col4','col5','col6','col7'],delim_whitespace=True)  # read exported FreeFlyer epoch text, specify columns picked from .txt, no headers

timestamp = []

a = df['col1']
b = df['col2']
c = df['col3']
d = df['col4']

for i in range (a.size):

    s = "{} 0{} {} {}".format(a.iloc[i], b.iloc[i], c.iloc[i], d.iloc[i]) #read FreeFlyer epoch text as string
    #s = dateutil.parser.parse(s) #optional : convert to datetime object
    timestamp.append(s)

print(timestamp[0])

y1 = df['col5']

y2 = df['col6']/1000 #manipulate data as needed

y3 = df['col7']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx() #in case a second y-axis needs to be used

# ax1.yaxis.set_major_formatter(FormatStrFormatter('%.3f')) # define how many decimals appear in values displayed in each axis
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

ax1.set_xlabel('Elapsed Days')
ax1.set_ylabel('Atmospheric Density - MSIS-2000 (g/cm$^{3}$)')
# ax1.set_yscale('log')
ax2.set_ylabel("Latitude")

ax1.xaxis.get_ticklocs(minor=True) #get minor tick locations
ax1.yaxis.get_ticklocs(minor=True)

ax2.yaxis.get_ticklocs(minor=True)

# ax1.set_ylim(0,0.015) #set axis limits
# ax1.set_xlim([0, 7])

# ax2.set_ylim([0, 1])

ax1.minorticks_on() #activate minor ticks
ax2.minorticks_on()

plt.title('Satellite, Rho1 = 0')

ax1.plot(y1,y2,linewidth=1)

ax2.plot(y1,y3,c='r',linewidth=0.5)

# plt.grid()
plt.show()
