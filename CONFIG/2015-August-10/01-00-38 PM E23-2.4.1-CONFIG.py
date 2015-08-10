#File
fname = 'E23-2.4.1.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 30 #% max power
dwellTime      = 25 #ms
x_start        = 417
y_start        = 333
z_start        = 119.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 200 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.860 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed