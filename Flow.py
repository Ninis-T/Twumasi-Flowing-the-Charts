# start

# this first variable checks if there is a start block.
# it is a boolean variable which means it can only be True or False.
# if it is False, that means the input is invalid.
has_start = True


# this if statement checks whether there is a start.
# if there is no start (False), it will show invalid input and end.
# if there is a start (True), it will continue the program.
if has_start:
    
    print("Start")
    
    
    # this variable checks if the block is a rectangle.
    # a rectangle in a flowchart usually means perform an action.
    is_rectangle = True
    
    
    # this checks if the block is a rectangle.
    # if True, it performs the action.
    # if False, it skips to the next decision.
    if is_rectangle:
        print("Perform the action")
    
    
    # after performing the action (or skipping it),
    # the program goes to the next decision.
    print("Go to next decision")
    
    
    # this variable checks if the block is a diamond.
    # a diamond in a flowchart represents a decision.
    is_diamond = True
    
    
    # this checks if the block is a diamond.
    # if True, it answers the question and follows the correct arrow.
    # if False, it continues.
    if is_diamond:
        print("Answer the question and follow the correct arrow")
    
    
    # this represents continuing through the flowchart.
    print("Continue")
    
    
    # this variable checks if there is an end block.
    # if True, the program will end.
    # if False, it would normally loop back.
    has_end = True
    
    
    # this checks if there is an end.
    # if True, it prints End.
    # if False, it would loop until there is an end.
    if has_end:
        print("End")
    
    else:
        print("Loop until end")


# this else belongs to the has_start check.
# if there is no start, the input is invalid.
else:
    print("Show invalid input")

# End
print("End")