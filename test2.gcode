;(***************uWellPlate******************)
;(*** Monday, October 20, 2014 @ 01:39:23 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G28
G0 X4 Y5 F2000
G0 Z6.1 F300
G0 X0 Y0 F2000
G4 P7
G1 X-9 S2 L3000 P0.08333333333333333 F8 B1
G0 X3.0 Y-10.392 F2000
G4 P7
G0 X-6.0 Y-10.608 F2000
G4 P7

;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
