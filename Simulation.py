from Particle import Particle
import numpy as np
import pandas as panda
import sys
import time

def runSimulation(Particles=[], runs=400):

    barWidth = 50

    sys.stdout.write("Loading Simulation:\n")
    sys.stdout.write("0 [%s] 100" % (" " * barWidth))
    sys.stdout.flush()
    sys.stdout.write("\b" * (barWidth + 5))  # return to start of line, after '['
    for i in range(runs):
        for particle in Particles:
            particle.updatePosition(particles=Particles)
            particle.updateEnergy()
            particle.updateCollisions(particles=Particles)
            particle.update(particles=Particles)

        if i % (runs // barWidth) == 0:
            sys.stdout.write("-")
            sys.stdout.flush()

    sys.stdout.write("\n")
    #print ('Final Pressure:' + pressure)

    for x in range(0, runs, 1):
        for particle in Particles:
            particle.updateEnergyPressure(particles=Particles)


    dataList = []
    secondaryDataList = []
   # pressure = 0

    for particle in Particles:
        dataList += particle.positionlog
        secondaryDataList += particle.dataLog

        #pressure += particle.getPressure()

   # print(pressure)

    DataFrame = panda.DataFrame(dataList, columns=['index', 'x', 'y', 'z'])
    SecondaryData = panda.DataFrame(secondaryDataList, columns=['index', 'energy', 'pressure'])
    return DataFrame, SecondaryData

    