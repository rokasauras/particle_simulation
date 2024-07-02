import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Graphics3D(object):
    """
    A class that creates a 3D scatter plot animation from a dataframe containing positions and time.

    Attributes:
    -----------
    data : pandas.DataFrame
        The dataframe containing the particle data.
    interval : int
        The delay between frames in milliseconds.
    hide : bool
        Toggles hiding the axis.
    save : bool
        Controls saving the animation.
    pltfig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes._subplots.Axes3DSubplot
        The 3D subplot object.
    graphics : matplotlib.animation.FuncAnimation
        The animation object.

    Methods:
    --------
    update(i)
        Update function called at each frame of the animation.
    createGraphics()
        Initialisation function called before the animation starts to set the 3D Plot Graphic variables.
    """

    def __init__(self, df, interval = 4, hide = False, save = False):
        """
        Constructs a Graphics3D object.

        Parameters:
        -----------
        df : pandas.DataFrame
            The dataframe containing the positions and time.
        interval : int
            The delay between frames in milliseconds.
        hide : bool
            Whether to hide the axis or not.
        save : bool
            Whether to save the animation as an mp4 file or not.
        """
        self.data = df #df containing positions and time 
        self.interval = interval
        self.hide = hide
        self.pltfig = plt.figure()
        self.ax = self.pltfig.add_subplot( projection='3d')
        self.graphics = animation.FuncAnimation(self.pltfig, 
        self.update, interval= interval, 
        init_func=self.createGraphics,
        blit= False,
        frames= int(self.data['index'].max()),
        repeat = (not save))
        
        if save:
            writer = animation.FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=1800000)
            self.graphics.save('Graphics3D.mp4', writer = writer)

        plt.show()

    def update(self, i):
        """
        Update function called at each frame of the animation.

        Parameters:
        -----------
        i : int
            The current frame number.
        """
        Positions = self.data[self.data['index'] == i]
        self.graph._offsets3d = (Positions.x, Positions.y, Positions.z)
        self.title.set_text('Simulation Model of Argon Particles \n Time = {} \n '.format(i))
        return self.graph

    def createGraphics(self):
        """
        Initialisation function called before the animation starts to set the 3D Plot Graphic variables.
        """ 
        self.ax.clear()
        self.title = self.ax.set_title('Simulation Model of Argon Particles')
        initialPos = self.data[self.data['index']==0]
        
        l = len(initialPos)
        colours = np.arange(l)

        self.graph = self.ax.scatter(initialPos.x, initialPos.y, initialPos.z
                                     , depthshade = True, c = colours)

        maximumDistance = float(self.data[['x','y','z']].min(axis =1).min())
        minimumDistance = float(self.data[['x','y','z']].max(axis = 1).max())

        self.ax.set_xlim(minimumDistance, maximumDistance)
        self.ax.set_ylim(minimumDistance, maximumDistance)
        self.ax.set_zlim(minimumDistance, maximumDistance)

        if self.hide:
            self.ax.set_axis_off()

        return self.graph,
