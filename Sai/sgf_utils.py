from sgfmill import sgf
import pickle
import string
import global_var

from gnugo_utils import get_response_move

BOARD_SIZE = 19
#output_file = r'sgf_files/' + global_var.sgf_name

def to_SGF(board):
  # Return an SGF representation of the board state
  #side_to_move = "white"
  board_letters = string.ascii_lowercase # 'a' to 'z'
  output = "(;GM[1]FF[4]SZ[" + str(BOARD_SIZE) + "]\n"
  output = f"(;FF[4]\nGM[1]\nDT[{global_var.game_date}]\nSZ[{str(BOARD_SIZE)}]\n"
  #if side_to_move == "black":
  if global_var.player_colour == "black":
    output += "PL[B]\n"
  else:
    output += "PL[W]\n"
  black_moves, white_moves = "", ""
  for i, row in enumerate(board):
    for j, color in enumerate(row):
      if color == "black":
        black_moves += "AB"
        black_moves += "[" + board_letters[j] + board_letters[i] + "]"
      elif color == "white":
        white_moves += "AW"
        white_moves += "[" + board_letters[j] + board_letters[i] + "]"

  if global_var.player_colour == "black":
    output += black_moves + "\n" + white_moves + "\n" + ")\n"
  else:
    output += white_moves + "\n" + black_moves + "\n" + ")\n"
  return output


def save_SGF(board):
  #global output_file
  output_file = r'sgf_files/' + global_var.sgf_name
  sgf = open(output_file, "w")
  sgf.write(to_SGF(board))
  sgf.close()
  print("Saved to file " + output_file)

  return get_response_move(output_file)

  

if __name__ == "__main__":
  with open('board_state.data', 'rb') as filehandle:
        # read the data as binary data stream
        board = pickle.load(filehandle)
  save_SGF(board)
