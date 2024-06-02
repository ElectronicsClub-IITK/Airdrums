import csv

def update_vel_and_disp(disp,vel,acc,interval):
    for i in range(0,len(disp)):
        disp[i]=disp[i]+vel[i]*interval+0.5*interval*interval*acc[i]
    
    for i in range(0,len(vel)):
        vel[i]=vel[i]+interval*acc[i]
    
    print("displacement vector is =",disp)
    print("velocity vector is =",vel)
    
def read_csv_row_by_row(file_path,acc):
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Read the header row
        header = next(csvreader)
        print(f"Header: {header}")
        
        # Process each row
        for row in csvreader:
            ax, ay, az,time = row
            print(f"ax: {ax}, ay: {ay}, az: {az}")
            acc[0],acc[1],acc[2]=ax,ay,az
        
        return acc


if __name__ == "__main__":
    disp=[0.0,0.0,0.0]
    vel=[0.0,0.0,0.0]
    acc=[0.1,0.2,0.3]  #sample acceleration . In actual code, we will keep taking acceleration from the sensor and update the acc vector
    #to take values from csv file
    # file_path=C:\\Users\\ARUZ\\Desktop\\AirDrums\\data.csv
    # acc=read_csv_row_by_row(file_path,acc)
    
    update_vel_and_disp(disp,vel,acc,0.1)  #but we have to keep updating the velocity and diisp every 0.1 seconds 
    