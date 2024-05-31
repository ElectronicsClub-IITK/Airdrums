import csv

def reading_acc(acc_path):
    acc = []
    with open(acc_path, mode='r') as f:
        read = csv.reader(f)
        next(read)
        for row in read:
            acc.append([float(row[0]), float(row[1]), float(row[2])])
    return acc

def update(velocity, displacement, acc, time_elapsed):
    for i in range(3):   
        displacement[i] += (velocity[i] * time_elapsed) + 0.5 * (acc[i] * time_elapsed **2)
        velocity[i] += acc[i] * time_elapsed
    return velocity, displacement

if __name__ == "__main__":
    displacement = [0.0, 0.0, 0.0]
    velocity = [0.0, 0.0, 0.0]
    time_elapsed = 0.1
    acc_path = 'imu_data.csv'
    acc = reading_acc(acc_path)
    velocity, displacement= update(velocity, displacement, acc, time_elapsed)
    print(f"Current Velocity: {velocity}, Displacement: {displacement}")