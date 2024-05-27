def update_displacement_velocity(current_displacement, current_velocity, acceleration, time_interval):
    time_interval_seconds = time_interval / 1000.0

    new_velocity = [
        current_velocity[0] + acceleration[0] * time_interval_seconds,
        current_velocity[1] + acceleration[1] * time_interval_seconds,
        current_velocity[2] + acceleration[2] * time_interval_seconds
    ]

    new_displacement = [
        current_displacement[0] + current_velocity[0] * time_interval_seconds + 0.5 * acceleration[0] * time_interval_seconds**2,
        current_displacement[1] + current_velocity[1] * time_interval_seconds + 0.5 * acceleration[1] * time_interval_seconds**2,
        current_displacement[2] + current_velocity[2] * time_interval_seconds + 0.5 * acceleration[2] * time_interval_seconds**2
    ]

    return new_displacement, new_velocity

disp, vel = update_displacement_velocity(current_displacement, current_velocity, acceleration, time_interval)

print("New Displacement = ", disp)
print("New Velocity = ", vel)