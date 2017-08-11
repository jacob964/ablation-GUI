#File
fname = 'Kim2-1_41x44mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 35 #% max power
dwellTime      = 40 #ms
x_start        = 414
y_start        = 340
z_start        = 117.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 41 #mm; x-direction
rectWidth      = 44 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.300 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 20 #number of rows between laser head cleanings