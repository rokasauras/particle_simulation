<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Particle Simulation and Visualisation</h1>

  <h2>Description</h2>
    <p>This project simulates the behavior of particles in a three-dimensional space and visualises the results. It uses custom modules to initialise particle positions, run the simulation, and display 3D graphics. Additionally, it plots the energy and pressure of the particles over time using Matplotlib.</p>

  <h2>Main Features</h2>
    <ul>
        <li><strong>Initialise Particle Positions:</strong> Set up initial positions for a specified number of particles.</li>
        <li><strong>Run Simulation:</strong> Execute the simulation and capture data on particle behavior.</li>
        <li><strong>Visualise Results:</strong> Plot energy and pressure over time, and generate a 3D visualisation of the particle system.</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <p>Ensure you have Python installed. Install the required packages using pip:</p>
            <pre><code>pip install matplotlib</code></pre>
        </li>
        <li><strong>Ensure Custom Modules are Accessible:</strong>
            <ul>
                <li>InitialPositions</li>
                <li>Simulation</li>
                <li>Graphics3D</li>
            </ul>
        </li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li><strong>Import Required Modules:</strong>
            <pre><code>from InitialPositions import InitialPositions
from Simulation import runSimulation
from Graphics3D import Graphics3D
import matplotlib.pyplot as plt</code></pre>
        </li>
        <li><strong>Initialise Particle Positions:</strong>
            <pre><code>StartingXYs = InitialPositions(numberOfParticles=30)</code></pre>
        </li>
        <li><strong>Run the Simulation:</strong>
            <pre><code>Data, Data2 = runSimulation(Particles=StartingXYs)</code></pre>
        </li>
        <li><strong>Print Pressure and Energy Data:</strong>
            <pre><code>print(Data2[['pressure']])
print(Data2[['energy']])</code></pre>
        </li>
        <li><strong>Plot Energy Over Time:</strong>
            <pre><code>Data2[['energy']].plot.line(
    color='black',
    linewidth=2,
    xlabel='Time',
    ylabel='Energy',
)
plt.xlim([0, 100])
plt.ylim([0, 2000])
plt.plot()</code></pre>
        </li>
        <li><strong>Plot Pressure Over Time:</strong>
            <pre><code>Data2[['pressure']].plot.line(
    color='black',
    linewidth=2,
    xlabel='Time',
    ylabel='Pressure',
)
plt.xlim([0, 100])
plt.plot()</code></pre>
        </li>
        <li><strong>Generate 3D Visualisation:</strong>
            <pre><code>Graphics3D(df=Data)</code></pre>
        </li>
    </ol>

  <h2>Example Output</h2>
    <ul>
        <li><strong>Pressure Data:</strong> Prints the pressure data of particles over time.</li>
        <li><strong>Energy Data:</strong> Prints the energy data of particles over time.</li>
        <li><strong>Energy Plot:</strong> A line graph showing the energy of particles over time.</li>
        <li><strong>Pressure Plot:</strong> A line graph showing the pressure of particles over time.</li>
        <li><strong>3D Visualisation:</strong> A graphical representation of particles in 3D space.</li>
    </ul>

  <h2>Customisation</h2>
    <ul>
        <li><strong>Number of Particles:</strong> Adjust the number of particles by changing the <code>numberOfParticles</code> parameter in <code>InitialPositions</code>.</li>
        <li><strong>Simulation Parameters:</strong> Modify the simulation behavior by changing parameters in the <code>runSimulation</code> function.</li>
    </ul>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.</p>
</body>
</html>
