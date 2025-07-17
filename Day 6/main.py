def ether():
    while front_is_clear() and wall_on_right():
        move() 
        if at_goal:
            return
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
        if at_goal:
            return
    elif right_is_clear()==False and front_is_clear():   
        move()
        if at_goal:
            return
    elif front_is_clear()==False and right_is_clear()==False:
        turn_left()
while not at_goal():
    ether()