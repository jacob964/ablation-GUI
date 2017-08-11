#File
fname = 'Kim1-2_20x20.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 35 #% max power
dwellTime      = 30 #ms
x_start        = 414
y_start        = 335
z_start        = 117.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 20 #mm; x-direction
rectWidth      = 20 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.400 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 50 #number of rows between laser head cleanings