import pandas as pd
import numpy as np

class Vector:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

def subtract(v1,v2):
    return Vector(v1.x-v2.x,v1.y-v2.y,v1.z-v2.z)
def add(v1,v2):
    return Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)


d=Vector(0,0,0)
u = Vector(0,0,0)
t=0.1


while True:
    file_path=r"C:\Users\rohna\Music\eclub\Airdrums\Week_3\csv.csv"
    data = pd.read_csv(file_path,header=None)
    accx=np.array(data.iloc[:,0])
    accy=np.array(data.iloc[:,1])
    accz=np.array(data.iloc[:,2])
    accx1=accx[-1]
    accy1=accy[-1]
    accz1=accz[-1]
    u.x=u.x + accx1*t
    u.y=u.y + accy1*t
    u.z=u.z + accz1*t
    print(u.x,u.y,u.z)

    d.x=d.x + ((u.x*t)+1/2*(accx1*t*t))
    d.y=d.y + ((u.y*t)+1/2*(accy1*t*t))
    d.z=d.z + ((u.z*t)+1/2*(accz1*t*t))
    print(d.x,d.y,d.z)

  
   
    
    
