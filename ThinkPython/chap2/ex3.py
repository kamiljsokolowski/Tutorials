# problem #1
pi = 3.14
r = 5
volume = (4 / 3) * pi * (r ** 3)
print volume

# problem #2
price = 24.95
disc = 0.4
ship_first = 3
ship_next = 0.75
total = ((price * disc) + ship_first) + 59 * ((price * disc) + ship_next)
print total

# problem #3
start_h = 6
start_m = 52
start_s = 0 
print "Start time is: %i : %i : %i" % (start_h, start_m, start_s) 
### need to add conditions for values > 60 ###
run_h = 0
run_m = (2 * 8) + (3 * 7)
run_s = (2 * 15) + (3 * 12)
print "Run time is: %i : %i : %i" % (run_h, run_m, run_s) 
stop_h = start_h + run_h
stop_m = start_m + run_m
stop_s = start_s + run_s
print "Stop time is: %i : %i : %i" % (stop_h, stop_m, stop_s) 

