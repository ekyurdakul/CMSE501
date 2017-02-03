import tkinter as tk
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from simulation import *
mpl.use("TkAgg")

class GUI:
    def __init__(self):
        #Main window
        self.__wnd = tk.Tk()
        self.__wnd.title("Term Project")
        self.__wnd.geometry("900x800")
        #InputFrame
        self.__iFrame = tk.Frame(self.__wnd)
        self.__iFrame.pack(side=tk.TOP)
        #Simulation parameters
        self.__people = tk.IntVar(value=100)
        self.__crowded = tk.IntVar(value=60)
        self.__time = tk.IntVar(value=100)
        self.__predpa = tk.IntVar(value=3)
        self.__updateEvery = tk.IntVar(value=1)
        #GUI elements for simulation parameters
        #Number of people
        self.__scalePeople = tk.Scale(self.__iFrame,variable=self.__people,label="Number of People",orient=tk.HORIZONTAL,length=300,from_=1,to=100)
        self.__scalePeople.pack(side=tk.TOP)
        #Crowded threshold
        self.__scaleCrowded = tk.Scale(self.__iFrame,variable=self.__crowded,label="Crowded Threshold",orient=tk.HORIZONTAL,length=300,from_=1,to=100)
        self.__scaleCrowded.pack(side=tk.TOP)
        #Number of predictors per agent
        self.__scalePredictors = tk.Scale(self.__iFrame,variable=self.__predpa,label="Predictors per Agent",orient=tk.HORIZONTAL,length=300,from_=1,to=24)
        self.__scalePredictors.pack(side=tk.TOP)
        #Time
        self.__scaleTime = tk.Scale(self.__iFrame,variable=self.__time,label="Time",orient=tk.HORIZONTAL,length=300,from_=1,to=100)
        self.__scaleTime.pack(side=tk.TOP)
        #Active agent predictors are updated every T weeks
        self.__scaleUpdate = tk.Scale(self.__iFrame,variable=self.__updateEvery,label="Predictor Update Interval",orient=tk.HORIZONTAL,length=300,from_=1,to=100)
        self.__scaleUpdate.pack(side=tk.TOP)
        #Run simulation when clicked on this button
        self.__runButton = tk.Button(self.__iFrame,text="Run Simulation",command=self.__plot)
        self.__runButton.pack(side=tk.TOP,pady=20)
        #OutputFrame
        self.__oFrame = tk.Frame(self.__wnd)
        self.__oFrame.pack(side=tk.BOTTOM,expand=1,fill=tk.BOTH)
        #Plot
        self.__fig = Figure()
        self.__plotCanvas = FigureCanvasTkAgg(self.__fig, master=self.__oFrame)
        self.__plotNavigation = NavigationToolbar2TkAgg(self.__plotCanvas,self.__oFrame)
        self.__plotCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    #Show the GUI
    def show(self):
        self.__plot()
        self.__wnd.mainloop()

    #Simulate and plot
    def __plot(self):
        #New simulation with paramaters from the GUI
        sim = Simulation(self.__people.get(),self.__time.get(),self.__predpa.get(),self.__crowded.get(),self.__updateEvery.get())
        x = range(1,self.__time.get()+1)
        y = sim.simulate()
        ymean = [np.mean(y)] * len(y)
        #New figure
        self.__fig.clear()
        f = self.__fig.add_subplot(111)
        #Plot the simulation
        f.plot(x,y,"g-o")
        #Plot the mean attendance
        f.plot(x,ymean,"r")
        f.set_xticks(range(0,self.__time.get()+1,5))
        f.set_yticks(range(0,101,5))
        f.set_title("El Farol Simulation")
        f.set_xlabel("Week")
        f.set_ylabel("People",rotation="horizontal",horizontalalignment="right")
        f.set_xlim(1,self.__time.get())
        f.set_ylim(0,100)
        f.legend(["Attendance","Mean Attendance"],loc="upper right")
        f.grid(b=True,which="both",axis="both")
        self.__plotCanvas.show()

#Run a GUI instance
g = GUI()
g.show()