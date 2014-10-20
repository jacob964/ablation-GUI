#File
fname = '2.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 1 #% max power
dwellTime      = 1 #ms
x_start        = 1
y_start        = 1
z_start        = 99.4 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 1 #movement speed

# Rectangle size properties
rectLength     = 11 #mm; x-direction
rectWidth      = 1 #mm; y-direction
spaceSmall     = 1 #mm; space between rectangles
hexLength      = 1.000 #mm

#Other
relative       = 0 #1 for no starting x,y; 0 for using starting co-ordinates