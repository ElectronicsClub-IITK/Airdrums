import numpy as np
import pandas as pd

def update_displacement_velocity(displacement, velocity, acceleration, time_interval):
    # Calculate the updated velocity using the formula: v = u + at
    updated_velocity = velocity + acceleration * time_interval
    
    # Calculate the updated displacement using the formula: s = ut + 0.5 * a * t^2
    updated_displacement = displacement + velocity * time_interval + 0.5 * acceleration * (time_interval ** 2)
    
    return updated_displacement, updated_velocity

def calculate_displacements_from_csv(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Initialize displacement and velocity vectors
    displacement = np.array([0.0, 0.0, 0.0])
    velocity = np.array([0.0, 0.0, 0.0])
    
    # Create lists to store results
    displacements = [displacement]
    velocities = [velocity]

    # Iterate over each row in the data
    for i in range(1, len(data)):
        # Get the time interval (assuming time is in seconds)
        time_interval = data['time'][i] - data['time'][i-1]
        
        # Get the acceleration vector
        acceleration = np.array([data['accX'][i], data['accY'][i], data['accZ'][i]])
        
        # Update displacement and velocity
        displacement, velocity = update_displacement_velocity(displacement, velocity, acceleration, time_interval)
        
        # Append the results to the lists
        displacements.append(displacement)
        velocities.append(velocity)

    # Convert lists to DataFrame
    results_df = pd.DataFrame({
        'time': data['time'],
        'displacementX': [d[0] for d in displacements],
        'displacementY': [d[1] for d in displacements],
        'displacementZ': [d[2] for d in displacements],
        'velocityX': [v[0] for v in velocities],
        'velocityY': [v[1] for v in velocities],
        'velocityZ': [v[2] for v in velocities],
    })

    return results_df


file_path = 'imu_data.csv'
results_df = calculate_displacements_from_csv(file_path)
print(results_df)
