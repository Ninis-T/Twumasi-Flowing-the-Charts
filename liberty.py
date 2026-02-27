# start

# start with following liberty avenue
print("Follow Liberty Ave")

# This code will see if you have gone 2 miles by checking if it is true.
# This sets up the first decision in the if else chart.
gone_two_miles = True

# this sees if you gone two miles and if so you will travel 40th street
if gone_two_miles:
    print("Travel on 40th Street")
    
    # this part of the code sees if you have reached the bridge
    # if so you will not cross and turn right, if not you keep going on 40th street
    reached_bridge = True
    
    if reached_bridge:
        print("Do not cross")
        
        # now it makes you go right on Foster st
        print("Turn right on to Foster Street")
        print("Follow Foster Street")
        
        # this checks if this is the first left turn
        first_left_turn = True
        
        # this sees if this is the first left turn
        # if yes you follow the road, if not you keep following foster street
        if first_left_turn:
            print("Follow the road")
            
            # this makes you check if you reached the building
            reached_building = True
            
            # if you reached the building you stop
            # if not you keep following the road
            if reached_building:
                print("Stop")
            else:
                print("Keep following the road")
        
        else:
            print("Keep following Foster Street")
    
    else:
        print("Keep traveling on 40th Street")

# this is what happens if you have not gone 2 miles
# you will keep going on liberty avenue
else:
    print("Keep going on Liberty Ave")

# END
print("End")