import csv
import time
import accelerations

def update_displacement_velocity(displacement, velocity, acceleration, delta_t):
    
    # Updating velocity : v = u + a*t
    velocity_new = []
    for i in range(len(velocity)):
        velocity_new.append(velocity[i] + acceleration[i] * delta_t)
    
    # Updating displacement : s = s_0 + u*t + (1/2)*a*t^2
    displacement_new = []
    for i in range(len(displacement)):
        displacement_new.append(displacement[i] + velocity[i] * delta_t + 0.5 * acceleration[i] * (delta_t ** 2))
    
    return displacement_new, velocity_new

def main():
    # Setting initial conditions
    displacement = [0.0, 0.0, 0.0]
    velocity = [0.0, 0.0, 0.0]
    delta_t = 0.1  # Time interval
    
    # Initialise the CSV file for writing
    with open('displacements_velocities.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Time (s)', 'Displacement X', 'Displacement Y', 'Displacement Z', 
                         'Velocity X', 'Velocity Y', 'Velocity Z'])
        
        time_elapsed = 0.0
        acceleration_index = 0
        
        try:
            while True:
                # Get the current acceleration reading
                acceleration = accelerations.acceleration_readings[acceleration_index]
                
                # Updating displacement and velocity
                displacement, velocity = update_displacement_velocity(displacement, velocity, acceleration, delta_t)
                
                # Write the current displacement and velocity to the CSV file
                # First concatenated the two tuples of diplacement and velocity for ease of writing
                writer.writerow([time_elapsed] + displacement + velocity)
                
                # Increment time elapsed
                time_elapsed += delta_t
                
                # Move to the next acceleration reading
                acceleration_index += 1
                if acceleration_index >= len(accelerations.acceleration_readings):
                    # Loop back to the first acceleration reading if we reach the end
                    acceleration_index = 0
                
                # Wait for the next interval
                time.sleep(delta_t)
        
        # Stop the process when user wants to
        except KeyboardInterrupt:
            print("Stopped by user")

if __name__ == "__main__":
    main()
