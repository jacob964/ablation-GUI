;(***************uWellPlate******************)
;(*** Tuesday, June 30, 2015 @ 07:30:37 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G28
G0 X417 Y340 F2000
G0 Z120.1 F300
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X4.6 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X5.4 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X4.6 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X5.4 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X4.6 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X5.4 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X4.6 Y-0.693 F1000
G4 P500
G1 X-5 S20.0 L20000 P1.25 F500 B1
G0 X5.4 Y-0.693 F1000
G4 P500

;; Cleaning

M3 S0
G90
G0 X232 Y335 F1000
G4 P250
G0 Y255 F1000
G4 P250
G0 Y335 F1000
G4 P250
G0 X417.0 Y334.456 F1000
G4 P500
G91
;; Done Cleaning


;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
