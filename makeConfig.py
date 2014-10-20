from tkinter import *
from tkinter import ttk

from time import strftime, localtime
import os

# Functions

def dateName():
    dateStr = strftime("%Y-%B-%d", localtime())
    return dateStr

def timeName():
    timeStr = strftime("%I-%M-%S %p", localtime())
    return timeStr

def initConfigDir(filename):
    dateStr = dateName()
    timeStr = timeName()
    
    dirPath = "./CONFIG/{0}".format(dateStr)
    if not os.path.exists(dirPath): os.makedirs(dirPath)
    
    filePath = "{0}/{1} {2}".format(dirPath,timeStr,filename)
    return filePath

def initGcodeDir(filename):
    dateStr = dateName()
    timeStr = timeName()
    
    dirPath = "./GCODE/{0}".format(dateStr)
    if not os.path.exists(dirPath): os.makedirs(dirPath)
    
    filePath = "{0}/{1} {2}".format(dirPath,timeStr,filename)
    return filePath

def configure(*args):
    
    #File 
    filenameStr = str(filename.get())
    laserStr    = str(laserPower.get())
    dwellStr    = str(dwellTime.get())
    xStr        = str(x_start.get())
    yStr        = str(y_start.get())
    zStr        = "{:.1f}".format(110.4 - int(z_dist.get()))
    pauseStr    = str(500)
    speedStr    = str(feedRate.get())
    lengthStr   = str(rectLength.get())
    widthStr    = str(rectWidth.get())
    spaceStr    = str(3)
    hexPackStr  = "{:.3f}".format(float(hexPack.get()))
    relStr      = str(0)
    
    try:
        f = open("config.py",'w')
    except:
        print("Error-open")
        error.set("Cannot open config.py")
    
    gcodeNameStr = filenameStr + ".gcode"
    
    filetext = ("#File\n"
                "fname = '{0}'\n"
                "f=open(fname,'w')\n\n"
                "#Laser Parameters\n"
                "laserPower     = {1} #% max power\n"
                "dwellTime      = {2} #ms\n"
                "x_start        = {3}\n"
                "y_start        = {4}\n"
                "z_start        = {5} #mm above home\n"
                "pauseTime      = {6} #ms; time paused after movement before ablation\n"
                "feedRate       = {7} #movement speed\n\n"
                "# Rectangle size properties\n"
                "rectLength     = {8} #mm; x-direction\n"
                "rectWidth      = {9} #mm; y-direction\n"
                "spaceSmall     = {10} #mm; space between rectangles\n"
                "hexLength      = {11} #mm\n\n"
                "#Other\n"
                "relative       = {12} #1 for no starting x,y; 0 for using starting co-ordinates"
                ).format(gcodeNameStr,laserStr,dwellStr,xStr,yStr,zStr,pauseStr,speedStr,lengthStr,widthStr,spaceStr,hexPackStr,relStr)
    f.writelines(filetext)
    f.close()

#     gcodeNameStr,laserStr,dwellStr,xStr,yStr,zStr,pauseStr,speedStr,lengthStr,widthStr,spaceStr,hexPackStr,relStr
#     "test.gcode",2,3,4,5,6.1,7,8,9,10,11,12,0
    
    import pulse
    pulse.writeGCODE(gcodeNameStr,laserStr,dwellStr,xStr,yStr,zStr,pauseStr,speedStr,lengthStr,widthStr,spaceStr,hexPackStr,relStr)
    
    configPath      = initConfigDir(filenameStr)
    f = open("config.py",'r')
    g = open(configPath + "-CONFIG.py",'w')
    for line in f:
        g.writelines(line)
    f.close()
    g.close()
    
    gcodePath       = initGcodeDir(filenameStr)
    h = open(gcodeNameStr,'r')
    i = open(gcodePath+".gcode",'w')
    for line in h:
        i.writelines(line)
     
    h.close()
    i.close()
    
    os.remove("config.py")
    os.remove(gcodeNameStr)


    return


# Initialize Root Tk Interface
root = Tk()
root.title("Pulsed Ablation - Make GCODE")



### Parameter Frame
# Initialize and configure the Parameter Frame
paramFrame = ttk.Frame(root, padding=10)
paramFrame.grid(column=1,row=1,sticky=(N,W))
paramFrame.columnconfigure(0, weight=4)
paramFrame.rowconfigure(0, weight=4)

# Initialize Variables to be used in the parameter frame
laserPower  = StringVar()   # Laser Power
dwellTime   = StringVar()   # Residence Time    
z_dist      = StringVar()   # Focal Distance
feedRate    = StringVar()   # Movement Speed
hexPack     = StringVar()   # Hexagonal Packing

# Create parameter Frame Title
ttk.Label(paramFrame, text="Parameters").grid(column=1, row=1, sticky=(W))

# Create Parameter Labels
ttk.Label(paramFrame, text="Laser Power:").grid(column=1, row=2, sticky=(W,E))
ttk.Label(paramFrame, text="Residence Time:").grid(column=1, row=3, sticky=(W,E))
ttk.Label(paramFrame, text="Focal Distance:").grid(column=1, row=4, sticky=(W,E))
ttk.Label(paramFrame, text="Movement Speed:").grid(column=1, row=5, sticky=(W,E))
ttk.Label(paramFrame, text="Hexagonal Packing:").grid(column=1, row=6, sticky=(W,E))

# Create Parameter Entry boxes
power_entry = ttk.Entry(paramFrame, width=5, textvariable=laserPower)
power_entry.grid(column=2, row=2, sticky=(W,E))

dwell_entry = ttk.Entry(paramFrame, width=5, textvariable=dwellTime)
dwell_entry.grid(column=2, row=3, sticky=(W,E))

z_entry = ttk.Entry(paramFrame, width=5, textvariable=z_dist)
z_entry.grid(column=2, row=4, sticky=(W,E))

speed_entry = ttk.Entry(paramFrame, width=5, textvariable=feedRate)
speed_entry.grid(column=2, row=5, sticky=(W,E))

hex_entry = ttk.Entry(paramFrame, width=5, textvariable=hexPack)
hex_entry.grid(column=2, row=6, sticky=(W,E))

# Create Unit Labels
ttk.Label(paramFrame, text="%").grid(column=3, row=2, sticky=(W,E))
ttk.Label(paramFrame, text="ms").grid(column=3, row=3, sticky=(W,E))
ttk.Label(paramFrame, text="mm").grid(column=3, row=4, sticky=(W,E))
ttk.Label(paramFrame, text="mm/s").grid(column=3, row=5, sticky=(W,E))
ttk.Label(paramFrame, text="mm").grid(column=3, row=6, sticky=(W,E))



### Position Frame
positionFrame = ttk.Frame(root, padding=10)
positionFrame.grid(column=2,row=1,sticky=(N,W))
positionFrame.columnconfigure(0, weight=4)
positionFrame.rowconfigure(0, weight=4)

# Initialize Variables to be used in the Position Frame
x_start = StringVar()       # Initial X position
y_start = StringVar()       # Initial Y position   
rectLength = StringVar()    # Length of grid in x
rectWidth = StringVar()     # Length of grid in y

# Create Position Frame Titles
ttk.Label(positionFrame, text="Initial Position").grid(column=1, row=1, sticky=(W))
ttk.Label(positionFrame, text="Grid Size").grid(column=1, row=4, stick=(W))

# Create Position Labels
ttk.Label(positionFrame, text="X:").grid(column=1, row=2, sticky=(W,E))
ttk.Label(positionFrame, text="Y:").grid(column=1, row=3, sticky=(W,E))
ttk.Label(positionFrame, text="Length:").grid(column=1, row=5, sticky=(W,E))
ttk.Label(positionFrame, text="Width:").grid(column=1, row=6, sticky=(W,E))

# Create Position Entries
x_entry = ttk.Entry(positionFrame, width=5, textvariable=x_start)
x_entry.grid(column=2, row=2, sticky=(W,E))

y_entry = ttk.Entry(positionFrame, width=5, textvariable=y_start)
y_entry.grid(column=2, row=3, sticky=(W,E))

length_entry = ttk.Entry(positionFrame, width=5, textvariable=rectLength)
length_entry.grid(column=2, row=5, sticky=(W,E))

width_entry = ttk.Entry(positionFrame, width=5, textvariable=rectWidth)
width_entry.grid(column=2, row=6, sticky=(W,E))

# Create Unit Lables
ttk.Label(positionFrame, text="mm").grid(column=3, row=5, sticky=(W,E))
ttk.Label(positionFrame, text="mm").grid(column=3, row=6, sticky=(W,E))



### Filename Frame
# Initialize and configure the Filename Frame
fileFrame = ttk.Frame(root, padding=10)
fileFrame.grid(column=1,row=2,sticky=(N,W))
fileFrame.columnconfigure(0, weight=4)
fileFrame.rowconfigure(0, weight=10)

# Initialize Variables to be used in the Filename Frame
filename = StringVar()

# Label
ttk.Label(fileFrame, text="Filename: ").grid(column=1, row=1, sticky=(W))

# Entry for fileFrame
file_entry = ttk.Entry(fileFrame, width=25, textvariable=filename)
file_entry.grid(column=2, row=1, sticky=(W))


### Make GCODE Button Frame
# Initialize Frame
makeFrame = ttk.Frame(root, padding=10)
makeFrame.grid(column=2,row=2,sticky=(W,E))
makeFrame.columnconfigure(0,weight=4)
makeFrame.rowconfigure(0,weight=10)

# Make GCODE Button
ttk.Button(makeFrame, text="Make GCODE", command=configure).grid(column=1, row=1, sticky=(W, E))



### Make Error Frame
# Initialize Frame
errorFrame = ttk.Frame(root, padding=10)
errorFrame.grid(column=1, row=3, sticky=(W))
errorFrame.columnconfigure(0,weight=4)
errorFrame.rowconfigure(0,weight=4)

# Variable for error
error = StringVar()
error.set(" ")

# Label for error frame
ttk.Label(errorFrame, textvariable=error).grid(column=1,row=1,sticky=W)

root.bind('<Return>', configure)
root.mainloop()