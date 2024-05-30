import csv
import time

def update_displacement_velocity(displacement, velocity, acceleration, delta_t):
    
    # Updating velocity: v = u + a * t
    velocity_new = [v + a * delta_t for v, a in zip(velocity, acceleration)]

    # Updating displacement: s = s_0 + u * t + 0.5 * a * t^2
    displacement_new = [
        s + v * delta_t + 0.5 * a * delta_t**2
        for s, v, a in zip(displacement, velocity, acceleration)
    ]

    return displacement_new, velocity_new

def read_accelerations_from_csv(file_path):
    
    accelerations = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            accelerations.append([float(row[0]), float(row[1]), float(row[2])])
    return accelerations

def main():
    # Setting initial conditions
    displacement = [0.0, 0.0, 0.0]
    velocity = [0.0, 0.0, 0.0]
    delta_t = 0.1  # Time interval in seconds

    # Read accelerations from CSV file
    acceleration_file_path = 'imu_data.csv'
    acceleration_readings = read_accelerations_from_csv(acceleration_file_path)

    # Initialize the CSV file for writing results
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
                acceleration = acceleration_readings[acceleration_index]

                # Update displacement and velocity
                displacement, velocity = update_displacement_velocity(displacement, velocity, acceleration, delta_t)

                # Write the current displacement and velocity to the CSV file
                writer.writerow([time_elapsed] + displacement + velocity)

                # Increment time elapsed
                time_elapsed += delta_t

                # Move to the next acceleration reading
                acceleration_index = (acceleration_index + 1) % len(acceleration_readings)

                # Wait for the next interval
                time.sleep(delta_t)

        except KeyboardInterrupt:
            print("Process stopped by user.")

if __name__ == "__main__":
    main()
