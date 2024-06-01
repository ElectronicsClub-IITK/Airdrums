import math
def displ(curr_displ, curr_vel, given_acc,t) :
    t= 100

    for i in given_acc:
        d[i] = curr_displ[i] + curr_vel[i]*t + ((given_acc[i]*t*t)/2)
        curr_vel[i]= math.sqrt(curr_vel[i]+ 2*given_acc * d[i])

