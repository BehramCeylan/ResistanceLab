from scipy.optimize import fsolve
#Takes the measured voltage values as input

V_list=(
0.167
,0.408
,0.631
,0.842
,1.066
,1.293
,1.555
,1.853
,2.217
,2.692
,2.885)

#Finds the zeros of the following difference function between 0 and 1
#Which are the actual values based on the measrued voltages

for V in V_list:
    f = lambda k:k/((1000/1000)+k-(k*k))-(V*1000)/(2.886*1000)
    print(fsolve(f,[0,1])[0])
    
    
    
    
    
    
    
    
    
    