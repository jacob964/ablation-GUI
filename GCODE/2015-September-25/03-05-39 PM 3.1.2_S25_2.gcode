;(***************uWellPlate******************)
;(*** Friday, September 25, 2015 @ 03:05:39 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G90
M3 S0
G0 X399 Y325 F2000
G0 Z122.1 F300
G91
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X9.5 Y-0.866 F1000
G4 P500
G1 X-10 S25.0 L20000 P1.0 F500 B1
G0 X10.5 Y-0.866 F1000
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
G0 X399.0 Y314.608 F1000
G4 P500
G91
;; Done Cleaning


;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
