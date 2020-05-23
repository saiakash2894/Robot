
The Code is scripted using Python.The Robotcode.py can be opened using Python editor.

Robot Code
=================
* `F` - move forward 1 unit
* `B` - move backward 1 unit
* `R` - turn right 90 degrees.   
* `L` - turn left 90 degrees

Step 1 - Concept and Design Decision
------------------------
Assuming the start point of the  robot as (0, 0) and starting direction as North

North = 0 ,East = 1,South = 2,West = 3

The Command L OR R only changes the directions of the robot and will the not change the (x , y) co-ordinates.

If the direction of the robot is North, then command 'L' changes the direction to West and 'R' changes to East
If the direction of the robot is East, then command 'L' changes the direction to North and 'R' changes to South
If the direction of the robot is South, then command 'L' changes the direction to West and 'R' changes to West
If the direction of the robot is West, then command 'L' changes the direction to West and 'R' changes to North

The Command F OR B changes the (x , y) as per following rules.

If the direction is North  & if Command is 'F' OR ' B'
 For F : y co-ordinate is increased  by number following the F.
 For B :  y co-ordinate is decreased  by number following the F.
If the direction is East  & if Command is 'F' OR ' B'
 For F : x co-ordinate is increased  by number following the F.
 For B :  x co-ordinate is decreased  by number following the F.
If the direction is South & if Command is 'F' OR ' B'
 For F : y co-ordinate is decreased  by number following the F.
 For B :  y co-ordinate is increased  by number following the F.
If the direction is West  & if Command is 'F' OR ' B'
 For F : x co-ordinate is decreased  by number following the F.
 For B : x co-ordinate is increased  by number following the F.

Code Description
==================

Distance function  calculates the minimum distance from end point to the starting point.
This function uses the input as a parameter to calculate the distance and will return the distance when it is called.
As per code "dist = distance(input)"

Function - Distance
===============

1- Using a loop and Splitting the input string to get each command into a list 

    Example : input= 'F1,B2,R3,L1'.  command=('F', '1') for first iteration.

2- If command is 'R' Right or 'L' Left , then change direction of the robot
     For R    (dir + 1)% 4 is used to change the direction
     For  L    (4 + dir - 1)%4 is used to change the direction

3- If command is 'F' or 'B' , Based on the current direction x or y co-ordinates increases or decreases according to the information specified in the Concept and Design Decision.

4- Finally once the x and y co-ordinates are calculated , modulus is performed on both x and y co-ordinates and  both the co-ordinates are added to get the distance from the starting point.

5- Returns distance 


Test Cases
============
Test case 1 : Empty string
Input = ""
Output Distance: Wrong Input.Robot is at Same Position. Distance is 0

Test Case 2 : String containing 0 
Input "F0"
Output  Distance from the starting point: 0

Test Case 3 : String with length 1
Input = "F"
Output: Distance: Wrong Input.Robot is at Same Position. Distance is 0

Test Case 4 : String with lower alphabets 
Input = "F1,b0,r2,b2"
Output:Distance: 3

Test Case 5 : <Command><number> format is not followed
Input = "FF,BB,SA,SA" 
Output:Distance: Wrong input.

Test Case 6 : Input containing other that strings [F,L,R,B]
Input: "F1,d3"
Output: Wrong input.

Test Case 7 : Input string with digits greater than 9.
Input = "F20,b30"
Output: Distance from the starting point: 10





