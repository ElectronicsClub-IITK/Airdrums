import csv

def update(velocity, displacement, acc, time_elapsed):
    #using v=u+a*t and s=u*t+0.5*a*t^2
    for i in range(3):   
        displacement[i] += (velocity[i] * time_elapsed) + 0.5 * (acc[i] * time_elapsed **2)
        velocity[i] += acc[i] * time_elapsed
    return velocity, displacement

if __name__ == "__main__":
    #setting up initial conditions
    displacement = [0.0, 0.0, 0.0]
    velocity = [0.0, 0.0, 0.0]
    time_elapsed = 0.1
    file_path = 'imu_data.csv'
    #opening the csv file in read mode
    with open(file_path, mode='r') as f:
        read = csv.reader(f)
        next(read) #skipping the header
        #reading the accelerations and printing the updated velocity and displacement vector
        for row in read:
            acc = []
            acc.append([float(row[0]), float(row[1]), float(row[2])])
            velocity, displacement= update(velocity, displacement, acc, time_elapsed)
            print(f"Current Velocity: {velocity}, Displacement: {displacement}") 
