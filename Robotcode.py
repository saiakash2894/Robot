import math
import re

North = 0
East  = 1
South = 2
West  = 3

# distance funcion to caluclate distance from starting point
def distance(input):
    if len(input)>1:
  
    # Initialize starting point for robot as (0, 0) and starting 
    # direction as North 
        x = 0
        y = 0
        dir = North 
        #Splitting the input string
        data1 = input.split(",")
        for i in data1: 

            i=i.upper()
            
            list1=['F','B','R','L']
            
            #Checking the string for character and digit format
            
            if re.match(r'(\w+?)(\d+)', i):
                
            # Splitting text and number in string
            
                command = re.findall(r'(\w+?)(\d+)', i)[0]
            else:
                return "Wrong input."
            
            
    
       # Checking the input string for allowed inputs[F,L,R,B]
            # If command is left or right, then change direction 

            if command[0] in list1:
                if command[0] == 'R':
                    
                    #Changing the direction by number of units
                    for units in range(0,int(command[1])):
                        dir = (dir + 1)%4
                        
                elif command[0] == 'L': 
                    for units1 in range(0,int(command[1])):
                        dir = (4 + dir - 1)%4
                        
          
            # If command is 'F' Or 'B', then change x or y according to 
            #current direction 
                else:    
                    if dir == North: 
                        if command[0] == 'F':
                            y += int(command[1])
                    
                        elif command[0] == 'B':
                            y -= int(command[1])
                        
                    elif dir == East: 
                        if command[0] == 'F':
                            x += int(command[1])

                        elif command[0] == 'B':
                            x -= int(command[1])

                    elif dir == South:
                        if command[0] =='F':
                            y -= int(command[1])
                            
                        elif command[0] == 'B':
                            print(y)
                            y += int(command[1])
                    else: 
                        if command[0] =='F':
                            x -= int(command[1])
                        elif command[0] == 'B':
                            x += int(command[1])
            else:
                
                return "Wrong input"

                   
        # caluclate distance
        distance = abs(x) + abs (y)
        
        
        return distance
    else:
        return "Wrong Input.Robot is at Same Position. Distance is 0"
    
  
input = "F20,b30"
# function calling
dist = distance(input)
print('Distance from the starting point:',dist)
