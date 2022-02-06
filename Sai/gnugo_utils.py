import os
import subprocess
import global_var
from sgfmill import sgf

def engine_init():
    print("initiating Katago...")
    cmd = r'..\Engines\katago-v1.8.2-opencl-windows-x64\katago.exe gtp -model ..\Engines\katago-v1.8.2-opencl-windows-x64\g170-b40c256x2-s5095420928-d1229425124.bin.gz'
    global_var.p_engine = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) #avoid shell=True?
    #global_var.p_engine.stdin.write('\n'.encode('ascii'))
    global_var.p_engine.stdin.flush()
    #print(global_var.p_engine.stdout.readline())
    #out, err = global_var.p_engine.communicate()

    
def get_response_move(filename):
    print(f"Inputting board to engine for file {filename} and ai_colour {global_var.ai_colour}")
    #cmd = r'bin\gnugo-3.8\gnugo.exe --infile '+ "\'"+filename+"\'" + f' --color {global_var.ai_colour}' r' --quiet --outfile sgf_files\response.sgf'
    cmd = f'loadsgf {filename} \n'.encode('ascii')
    global_var.p_engine.stdin.write(cmd)
    global_var.p_engine.stdin.flush()
    out = global_var.p_engine.stdout.readline()
    while out.decode('ascii')[0] != '=':
        print("flag1")
        print(f"output is:[{out.decode('ascii')}]")
        out = global_var.p_engine.stdout.readline()
    #out, err = global_var.p_engine.communicate(input=f"loadsgf {filename}\n")
    #print(out.decode('ascii'))
    #print(cmd)
    print(f"last output is:[{out.decode('ascii')}]")

    print("generating move")
    # Katago move output is: "= D16"
    cmd = f'genmove {global_var.ai_colour}\n'.encode('ascii')
    global_var.p_engine.stdin.write(cmd)
    global_var.p_engine.stdin.flush()
    out = global_var.p_engine.stdout.readline().decode('ascii')
    while out[0] != '=':
        print("flag2")
        print(f"output is:[{out}]")
        out = global_var.p_engine.stdout.readline().decode('ascii')
    if len(out) < 3:
        print("something went wrong with genmove's output")
        return None
    print(f"last output is:[{out}]")
    move = []
    if global_var.ai_colour == 'white':
        move.append('w')
    else:
        move.append('b')
    #move.append(global_var.ai_colour)
    x = out[2]
    print(f"x is:[{x}]")
    x = ord(x)
    # katago doesnt use 'I' in coordinates
    if x > ord('I'):
        x += -1
    x = x - ord('A') + 1
    print(f"x is:[{x}]")
    #y = out[3:-1]
    y = out[3:]
    y = y.rstrip()
    print(f"y is:[{y}]")
    y = int(y)
    print(f"y is:[{y}]")
    #move.append((x,y))
    # reverse x,y bc computer science and change to 0 index
    move.append((y-1,x-1))
    print(f"move is:[{move}]")
    show_board()
    #out, err = global_var.p_engine.communicate(input=f"loadsgf {filename}\n")
    #print(f"output is:[{out.decode('ascii')}]")
    #out = global_var.p_engine.stdout.readline()
    #print(f"output is:[{out.decode('ascii')}]")
    
    #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    #out, err = p.communicate()
    #p.kill()
    """
    print("Reading response from gnugo")
    with open(r"sgf_files\response.sgf", "rb") as f:
        game = sgf.Sgf_game.from_bytes(f.read())
    board_size = game.get_size()
    root_node = game.get_root()
    moves = []
    for node in game.get_main_sequence():
        moves.append(node.get_move())
    # return last move which is the response from gnugo
    return(moves[-1:][0])
    """
    # return the move in the format: "w, (16,4)"
    return move

def show_board():
    print(f"inside show_board")
    #cmd = r'bin\gnugo-3.8\gnugo.exe --infile '+ "\'"+filename+"\'" + f' --color {global_var.ai_colour}' r' --quiet --outfile sgf_files\response.sgf'
    cmd = f'showboard\n'.encode('ascii')
    global_var.p_engine.stdin.write(cmd)
    global_var.p_engine.stdin.flush()
    out = global_var.p_engine.stdout.readline().decode('ascii')
    while out[0] != 'W':
        print(out)
        out = global_var.p_engine.stdout.readline().decode('ascii')
    #out, err = global_var.p_engine.communicate(input=f"loadsgf {filename}\n")
    #print(out.decode('ascii'))
    #print(cmd)
    print(f"last output is:[{out}]")
    
def engine_exit():
    global_var.p_engine.kill()