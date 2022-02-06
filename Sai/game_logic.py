import global_var

def game_logic(b_count, w_count):
    result = True
    turn_colour_match = False
    secondary_match = False
    capture_flag = False
    print("Running game logic...")
    print(f"turn #{global_var.turn}")
    print(f"turn colour is {turn_colour()}")
    print("expected black:\t",global_var.b_exp, "exceptected white:\t", global_var.w_exp)
    print("counted black:\t",b_count, "counted white:\t", w_count)
    # black's turn
    if turn_colour() == 'black': 
        if b_count == global_var.b_exp:
            turn_colour_match = True
            if w_count == global_var.w_exp:
                secondary_match = True
            elif w_count < global_var.w_exp:
                print(f"Blacks #{b_count} stone reduced whites from {global_var.w_exp} to {w_count}")
                capture_flag = True #capture occured if playing move reduced num of other stones
                global_var.w_exp = w_count
        else:
            return False
    # white's turn
    elif turn_colour() == 'white':
        if w_count == global_var.w_exp:
            turn_colour_match = True
            if b_count == global_var.b_exp:
                secondary_match = True
            elif b_count < global_var.b_exp:
                print(f"whites #{w_count} stone reduced blacks from {global_var.b_exp} to {b_count}")
                capture_flag = True #capture occured if playing move reduced num of other stones
                global_var.b_exp = b_count
        else:
            return False
    if secondary_match != True and capture_flag != True:
        print("Excess secondary stones on the board")
        return False

    if capture_flag == True:
        print("A capture happened!")

    return True

# check if board reading is the same across two readings
def stable_board_state(b_count, w_count):
    if (b_count != global_var.b_prev) or (w_count != global_var.w_prev):
        # update prev count with new count
        global_var.b_prev = b_count
        global_var.w_prev = w_count
        return False
    else:
        return True

def turn_colour():
    if global_var.turn % 2 == 0:
        return 'black'
    elif global_var.turn % 2 == 1:
        return 'white'

def increment_exp_ai_col():
    if global_var.ai_colour == 'black':
        global_var.b_exp += 1
    elif global_var.ai_colour == 'white':
        global_var.w_exp += 1
        
def increment_exp_player_col():
    if global_var.player_colour == 'black':
        global_var.b_exp += 1
        print("increased player's exp black stone")
    elif global_var.player_colour == 'white':
        global_var.w_exp += 1
        print("increased player's exp white stone")