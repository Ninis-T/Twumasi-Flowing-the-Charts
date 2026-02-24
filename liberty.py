#start
#start with following liberty avenue
print("Follow Liberty Ave")
#This code will see if you have gone 2 miles by seeing if its true this leads palce for the if else chart
gone_two_miles=True
#this sees if you gone to miles and if so you will travel 40th street
if gone_two_miles:
    print("Travel on 40th Street")
#this is what happens if you have not gone 2 miles you will keep going on liberty avenue
else:
    print("Keep going on Liberty Ave")
#this phase of the code sees if you have reached the bridge if so you will stand still if not you will keep going on 40th street
reached_bridge=True
if reached_bridge:
    print("Stand still")
    #now it makes you go right on Foster st
    print("Turn right on to Foster Street")
    print("Follow Foster Street")
    #This check if this is the first left turn
    first_left_turn = True 

    #this sees if this is the first left turn  
        if first_left_turn:
            print("Follow the road")
            
            # This makes you check if reached building
            reached_building = True   # change to False to test
            
            if reached_building:
                print("Stop")
            else:
                print("Keep following the road")
        
        else:
            print("Keep following Foster Street")
    
    else:
        print("Keep traveling on 40th Street")
else:
    print("Keep following Liberty Ave")

# END
print("End")