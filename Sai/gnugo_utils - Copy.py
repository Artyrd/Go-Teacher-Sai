import os
import subprocess
import global_var
from sgfmill import sgf

def get_response_move(filename):
    ''' shell out  and call the gnugo program and give it an in sgf file and an out sgf file'''
    #filename is the sgf_out.sgf from sgf_utils.py
    print(f"Inputting board to gnugo for file {filename} and ai_colour {global_var.ai_colour}")
    cmd = r'bin\gnugo-3.8\gnugo.exe --infile '+ "\'"+filename+"\'" + f' --color {global_var.ai_colour}' r' --quiet --outfile sgf_files\response.sgf'
    #print(cmd)

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    p.kill()

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