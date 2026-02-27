# start

# first you walk to the crosswalk. This prints the first action in the flowchart.
print("Walk to crosswalk")

# then you press the crosswalk button. This represents the next step in the flowchart.
print("Press crosswalk button")


# this variable represents whether the walk signal is on or not.
# it is a boolean variable which means it can only be True or False.
# if it is True, that means the walk sign is on.
# if it is False, that means you must wait.
walk_signal_on = True


# this if statement checks if the walk signal is on.
# if the variable is True, it will move forward to the next steps.
# if the variable is False, it will print that you need to wait.
if walk_signal_on:
    
    # this runs only if the walk signal is True.
    # this matches the flowchart step that says look left and right.
    print("Look LEFT and RIGHT")
    
    
    # this variable checks if the cars are stopped.
    # again this is a boolean variable.
    # True means cars are stopped.
    # False means cars are still moving.
    cars_stopped = True
    
    
    # this if statement checks if cars are stopped.
    # if True, you can begin walking.
    # if False, you must wait.
    if cars_stopped:
        
        print("Begin Walking")
        print("Walk across street")
        
        
        # this variable checks if the crossing signal changes while you are walking.
        # True means the signal changed.
        # False means it stayed the same.
        signal_changed = False
        
        
        # this if statement checks if the signal changed during crossing.
        # if it changed, you go back to the sidewalk.
        # if it did not change, you continue normally.
        if signal_changed:
            print("Go back to the sidewalk")
        
        else:
            print("Continue normally")
            print("Go to other side of the street")
    
    
    # this else belongs to the cars_stopped check.
    # if cars are not stopped, you wait.
    else:
        print("Wait for cars to stop")


# this else belongs to the walk_signal_on check.
# if the walk signal is not on, you wait.
else:
    print("Wait for walk signal")


# End
print("End")