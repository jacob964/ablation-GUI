#File
fname = '5D11-100_17x17mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 4 #ms
x_start        = 414
y_start        = 340
z_start        = 122.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 17 #mm; x-direction
rectWidth      = 17 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.250 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 100 #number of rows between laser head cleanings