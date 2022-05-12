import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

ftr = pd.read_csv("data_dsf=0.txt",delim_whitespace=True,usecols = [4,6,10],names = ['col1','col2','col3'])

y1 = ftr['col1']

y2 = ftr['col2']/1000

y3 = ftr['col3']

fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()

# ax1.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

ax1.set_xlabel('Elapsed Days')
ax1.set_ylabel('Atmospheric Density - MSIS-2000 (g/cm$^{3}$)')
# ax1.set_yscale('log')
# ax2.set_ylabel("In Shadow")

ax1.use_sticky_edges = False
# ax2.use_sticky_edges = False

ax1.xaxis.get_ticklocs(minor=True)
ax1.yaxis.get_ticklocs(minor=True)

# ax2.xaxis.get_ticklocs(minor=True)
# ax2.yaxis.get_ticklocs(minor=True)

ax1.set_ylim(0,0.015)
# ax2.set_ylim([0, 1])
ax1.set_xlim([0, 7])
ax1.minorticks_on()
# ax2.minorticks_on()

plt.title('Satellite, Rho1 = 0')

ax1.plot(y1,y2,linewidth=1)
# ax2.plot(y1,y3,c='r',linewidth=0.5)

# plt.legend()
# ax2.legend()

# plt.tight_layout()
# plt.grid()
plt.show()
