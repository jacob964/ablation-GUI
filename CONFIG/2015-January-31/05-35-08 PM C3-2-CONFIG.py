#File
fname = 'C3-2.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 15 #% max power
dwellTime      = 15 #ms
x_start        = 405
y_start        = 343
z_start        = 121.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 8 #mm; x-direction
rectWidth      = 8 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.700 #mm

#Other
relative       = 1 #0 for homing before beginning.  1 if machine has already been homed