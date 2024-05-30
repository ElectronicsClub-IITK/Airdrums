import csv

def displace(velocity, disp, acc, time_interval=0.1):
    #usning s=ut+1/2(at^2)
    for i in range(3):   
        disp[i] += (velocity[i] * time_interval) + 0.5 * (acc[i] * time_interval * time_interval)
        velocity[i] += acc[i] * time_interval
    return velocity, disp

if __name__ == "__main__":
    disp = [0.0, 0.0, 0.0]
    curr_velocity = [0.0, 0.0, 0.0]
    time_interval = 0.1  

    
    with open('acceleration_data.csv', mode='r') as fi:  #reading csv file from which we get the acceleration
        values = csv.reader(fi)        
        next(values)        # skiping the header 
        for row in values:
            acceleration = list(map(float, row))
            curr_velocity, disp = displace(curr_velocity, disp, acceleration, time_interval) #updating curr velocity and displacement
            print(f"Current Velocity: {curr_velocity}, Displacement: {disp}")
