import config
import writefile


## Parameters

#File
f = config.f

#Laser Parameters
laserPower 		= config.laserPower
dwellTime     	= config.dwellTime
x_start			= config.x_start
y_start			= config.y_start
z_start			= config.z_start
pauseTime 		= config.pauseTime
feedRate        = config.feedRate

# Rectangle size properties
rectLength 	= config.rectLength
rectWidth   = config.rectWidth
spaceSmall 	= config.spaceSmall
hex_pack	= config.hexLength

# Other Parameters
relative   	= config.relative

def hex_pattern(hex_pack):
	global x_dist
	x_dist = float("{:.3f}".format(hex_pack))
	global y_dist
	y_dist = float("{:.3f}".format(hex_pack * (3**0.5) / 2))
	return

def guiGlobVars(kvarg):
	#File
	filename = kvarg['gcodeNameStr']
	global f
	f.close()
	f = open(filename,'w')
	
	#Laser Parameters
	global laserPower
	laserPower 		= float(kvarg['laserStr'])
	global dwellTime
	dwellTime     	= int(kvarg['dwellStr'])
	global x_start
	x_start			= int(kvarg['xStr'])
	global y_start
	y_start			= int(kvarg['yStr'])
	global z_start
	z_start			= float(kvarg['zStr'])
	global pauseTime
	pauseTime 		= int(kvarg['pauseStr'])
	global feedRate
	feedRate        = int(kvarg['speedStr'])
	
	# Rectangle size properties
	global rectLength
	rectLength 	= int(kvarg['lengthStr'])
	global rectWidth
	rectWidth   = int(kvarg['widthStr'])
	global spaceSmall
	spaceSmall 	= int(kvarg['spaceStr'])
	global hex_pack
	hex_pack	= float(kvarg['hexPackStr'])
	
	hex_pattern(hex_pack)
	
	# Other Parameters
	global relative
	relative   	= int(kvarg['relStr'])	

def gcode_move(x_move, y_move):
	f.writelines("G0 X" + str(x_move) + " Y" + str(y_move) + " F1000\n")
	f.writelines("G4 P" + str(pauseTime) + "\n")

def gcode_rectangle(dwellTime, laserPower):
	x_total = 0
	y_total = 0
	flag = -1
	
	while y_total < rectWidth:
		f.writelines("G1 X" + str(-1*rectLength) + " S" + str(laserPower) + " L" + str(dwellTime*1000) + " P" + str(1/x_dist) + " F" + str(feedRate) + " B1\n") 
		#f.writelines("M3 S0\n")
		x_total -= rectLength
		
		x_overhang = flag * x_dist/2
		gcode_move(rectLength + x_overhang, -1*y_dist)
		x_total += rectLength + x_overhang
		
		y_total += y_dist
		flag *= -1
		
		
	totals = [x_total, y_total]
	return totals
	

def writeGCODE(kvarg):
	
	if (kvarg): guiGlobVars(kvarg)
	
	## Write GCODE file
	writefile.header(f)
	
	f.writelines("M3 S0\n") ## Laser Off
	
	if relative == 0: 
		f.writelines("G28\n") ## Home axes.
	else:
		f.writelines("G90\n")
		f.writelines("M3 S0\n") ## Laser Off
	f.writelines("G0 X" + str(x_start) + " Y" + str(y_start) + " F2000\n") # Move to x and y-axis start
	f.writelines("G0 Z" + str(z_start) + " F300\n") ##Move to z-axis position
	if relative == 1: f.writelines("G91\n")
	
	## Print Squares
	x_grid = 0
	y_grid = 0
		
	x_move = 0
	y_move = 0
	
	gcode_move(x_move, y_move)
	
	totals = gcode_rectangle(dwellTime, laserPower)
	x_move = totals[0] - rectLength - spaceSmall 
	y_move = totals[1]
	
	x_grid += rectLength + spaceSmall
	
	gcode_move(x_move + x_grid, y_move - rectWidth - spaceSmall)
	x_grid = 0
	y_grid += rectWidth + spaceSmall
	
	writefile.closefile(f)

def main():
	writeGCODE()

if __name__ == '__main__': main()
	
	
	
	




