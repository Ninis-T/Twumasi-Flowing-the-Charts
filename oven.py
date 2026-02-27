# start

# first we turn on the oven
print("Turn on oven")

# we place the turkey inside the oven
print("Place turkey inside")

# now we start the timer and the oven
print("Start timer and oven")

# these variables represent the conditions in the flowchart
turkey_reached_180 = False
four_hours_passed = False

# this loop keeps checking the turkey status until one of the ending conditions is met
# it will continue until one of the ending conditions becomes true
while True:

    # this checks if the turkey reached 180 degrees
    # the break blocks means that if this condition is true, we end the program immediately and do not check any other conditions. This is because if the turkey has reached 180 degrees, we want to stop cooking and end the program right away. We do not need to check if 4 hours have passed in this case, because the turkey being done is the more important condition for ending the program. If this condition is true, we remove the turkey and end the program without checking any further conditions.
    if turkey_reached_180:
        print("Remove turkey")
        break   # this stops the loop and ends the program

    # if the turkey has NOT reached 180,
    # then we check if it has been 4 hours
    # the elif blocks means that this condition will only be checked if the first condition is false. This is becaise there are two different ending conditions and we only want to end the program if one of them is true. If the first condition is true, then we end the program and do not need to check the second condition. If the first condition is false, then we check the second condition to see if we should end the program based on that condition.
    elif four_hours_passed:
        print("4 hours passed")
        break   # this also ends the program

    # if neither condition is true,
    # we continue the loop and keep cooking
    else:
        print("Continue cooking and checking")
        
        # these would normally change over time we see if its done
        turkey_reached_180 = True

# end
print("End")