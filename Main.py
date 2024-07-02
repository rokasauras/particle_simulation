from InitalPositions import InitalPositions
from Simulation import runSimulation
from Graphics3D import Graphics3D
import matplotlib.pyplot as plt

StartingXYZ = InitalPositions(numberOfParticles= 30)
Data, Data2= runSimulation(Particles= StartingXYZ)
print(Data2[['pressure']])
print(Data2[['energy']])

Data2[['energy']].plot.line(
    color='black',
    linewidth=2,
    xlabel='Time',
    ylabel='Energy',
)
plt.xlim([0, 100])
plt.ylim([0, 2000])

plt.plot()

Data2[['pressure']].plot.line(
    color='black',
    linewidth=2,
    xlabel='Time',
    ylabel='Pressure',
)
plt.xlim([0, 100])
plt.plot()

Graphics3D(df=Data)