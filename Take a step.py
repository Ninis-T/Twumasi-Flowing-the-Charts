#start
pace_counter=0

#Walk 20 paces
#for is a loop that repeats a block of code a certain number of times. Here it will repeat the block of code that prints "Take a step" and increments the pace_counter variable by 1,  until you get to 20 times.
for pace_counter in range(20):
    print("Take a step")
    pace_counter+=1
# This makes you turn toward target and if its not true then turn
print("Turning towards target")
#Check if target is facing you with a true false varible if statement. If the variable is true, it will print "Shoot". If the variable is false, it will print "Adjusting position", set the variable to true, and then print "Facing target". The site recommended the truth blocks to me
facing_target=True
if facing_target:
    print("Shoot")
#it says if the target is not facing you, then adjust position and turn to face the target. If the target is facing
else:
    print("Adjusting position")
    facing_target=True
    print("Facing target")
#this is what the site suggested.    
# This tells the code to Shoot if the target is facing you, and if not, it will adjust your position and turn to face the target before shooting. The code uses a boolean variable called facing_target to keep track of whether the target is facing you or not. If facing_target is true, it will print "Shoot". If facing_target is false, it will print "Adjusting position", set facing_target to true, and then print "Facing target". Finally, it will print "End" to indicate that the code has finished executing
print("Shoot!")

# End
print("End")