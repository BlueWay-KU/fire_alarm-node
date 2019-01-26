import serial
import sensor
import sys
sys.path.insert(0, '/home/pi/iBeacon-Scanner-')
import sort
import environment
import requests
import json

    
def alarm():
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = environment.node()
    for i in beacon:
        judge = [0]*50
        for key, value in mapping.items():
            for k, v in value.items():
                if k==i:
                    value[k]=1
        for key, value in mapping.items():
            for k, v in value.items():
                if v==1:
                    judge[key] = judge[key]+1
                if judge[key]==len(mapping[key]):
                    return key

port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

while True:
    fire_sensor = int(sensor.alarm())
    print("sensor status: "+str(fire_sensor))
    if(fire_sensor==1):
        print("fire detected")
        break

for i in range(0, 11):
    node = alarm()
    print("fire at node: "+str(node))

ID = 2

if node != 0:
    DATA = node
    data = {"ID":ID,"DATA":DATA}
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/saveData.php",params = data)
    print(r.text)
    
"""
while True:
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = environment.node()
    for i in beacon:
        judge = [0]*50
        for key, value in mapping.items():
            for k, v in value.items():
                if k==i:
                    value[k]=1
        print mapping
        for key, value in mapping.items():
            for k, v in value.items():
                if v==1:
                    judge[key] = judge[key]+1
        for j in judge:
            if judge[j] == len(mapping[j]):
                break
        print j
"""           
"""

while True:
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = environment.node()
    for i in beacon:
        judge = [0]*50
        for key, value in mapping.items():
            for k, v in value.items():
                if k==i:
                    value[k]=1
        print mapping
        for key, value in mapping.items():
            for k, v in value.items():
                if v==1:
                    judge[key] = judge[key]+1
        for j in judge:
            if judge[j] == 4:
                print j
                br
        
"""
                

        

                    
                    

"""
possible = []


def decision():
    print("beacon on: "+str(sort.sorting()))
    mapping = environment.node()
    
    for key, value in mapping.items():
        for k, v in value.items():
            count = 0
            possible = []
            for i in sort.sorting():
                if i==k:
                    value[k] = 1
                    count = count+1
                    
            if count==len(mapping[key]):
                return key
                break


while True:
    print decision()
"""
"""

possible = []

while True:
    beacon = []
    beacon = sort.sorting()
    print("beacon on: "+str(beacon))

    mapping = environment.node()
    
    for key, value in mapping.items():       
        for k in value.items():
            for i in beacon:
                if i==k:
                    value[k] = 1

            
"""                    


"""
possible = []


while True:
    print("beacon on: "+str(sort.sorting()))
    mapping = environment.node()
    
    for key, value in mapping.items():
        for k, v in value.items():
            count = 0
            possible = []
            for i in sort.sorting():
                if i==k:
                    value[k] = 1
                    count = count+1
                    
            if count==len(mapping[key]):
                possible.apeend(key)
                break
            
    print possible       
  """                  

            
"""
def place():
    print("beacon on: "+str(sort.sorting()))
    mapping = environment.node()

    for key, value in mapping.items():       
        for k, v in value.items():
            for i in sort.sorting():
                if i==k:
                    value[k] = 1
"""                    


"""


while True:
    print("beacon on: "+str(sort.sorting()))
    mapping = environment.node()

    possible = []
    for key, value in mapping.items():       
        count = 0
        for k, v in value.items():
            for i in sort.sorting():
                if i==k:
                    value[k] = 1
                    count = count + 1

                value[k] = 0

                if count == len(mapping[key]):
                    possible.append(key)
                    break

    print possible
"""    
"""

    for key, value in mapping.items():
        count = 0
        for k, v in value.items():
            if v == 1:
                count = count+1
            if count == len(val
"""
                    
    

"""

def alarm():
    while True:
        input_s = serialFromArduino.readline()
        ipt = int(input_s)
        print "fire : "+str(ipt)

        if ipt == 1:
            fire = environment.witch()
        else:
            fire = 0

        return fire
"""


"""
def alarm():
    beacon = []
    while True:
        input_s = serialFromArduino.readline()
        ipt = int(input_s)
        print ipt
        
        if ipt == 1:
            fire = environment.witch()
        else:
            fire = 0
        return fire
"""        

"""


import serial
import environment

port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()


def fire():
    beacon = []
    while True:
        input_s = serialFromArduino.readline()
        input = int(input_s)
        
        if input == 1:
            node = environment.witch()
            print node
            
            fire = 8
        else:
            fire = 0

        return fire
"""
