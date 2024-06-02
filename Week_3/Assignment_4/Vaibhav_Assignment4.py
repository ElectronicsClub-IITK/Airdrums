import numpy as np

def calculate_displacement(accelerations, time_interval):
    n = len(accelerations)
    velocity = np.array([0.0, 0.0, 0.0])
    displacement = np.array([0.0, 0.0, 0.0])
    for i in range(n):
        acceleration = np.array(accelerations[i])
        displacement += velocity * time_interval + 0.5 * acceleration * (time_interval ** 2)
        velocity += acceleration * time_interval
    return displacement

def calculate_velocity(accelerations, time_interval):
    n = len(accelerations)
    velocity = np.array([0.0, 0.0, 0.0])
    displacement = np.array([0.0, 0.0, 0.0])
    for i in range(n):
        acceleration = np.array(accelerations[i])
        displacement += velocity * time_interval + 0.5 * acceleration * (time_interval ** 2)
        velocity += acceleration * time_interval
    return velocity

input_string = input("Enter a list of tuples of three floats each, separated by semicolons (e.g., (1.0, 2.0, 3.0); (4.0, 5.0, 6.0)): ")
accelerations = [tuple(map(float, t.strip('() ').split(','))) for t in input_string.split(';')]
time_interval = float(input("Enter time interval: ")) 

displacement = calculate_displacement(accelerations, time_interval)
velocity = calculate_velocity(accelerations, time_interval)

print(f"Current displacement vector: {displacement}")
print(f"Current velocity vector: {velocity}")

def update_motion(current_displacement, current_velocity, acceleration, time_interval):
    current_displacement = np.array(displacement)
    current_velocity = np.array(velocity)
    acceleration = np.array(acceleration)

    new_displacement = current_displacement + current_velocity * time_interval + 0.5 * acceleration * (time_interval ** 2)

    new_velocity = current_velocity + acceleration * time_interval

    return new_displacement, new_velocity
    
input_string2 = input("Enter a tuple of three floats separated by commas (e.g., 1.0, 2.0, 3.0): ")
acceleration = tuple(map(float, input_string.split(',')))   
time_interval = float(input("Enter time interval: "))                      

new_displacement, new_velocity = update_motion(displacement, velocity, acceleration, time_interval)
print(f"Updated displacement vector: {new_displacement}")
print(f"Updated velocity vector: {new_velocity}")
