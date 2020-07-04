# An abstract class for a chess piece
# The method is_valid_move needs to be
# implemented for each individual chess
# piece since they have different movements
class Piece:
    def __init__(self, _rank, _file):
        self.rank = _rank 
        self.file = _file

    def move_piece(self, new_rank, new_file):
        if self.is_valid_move(new_rank, new_file):
            self.rank = new_rank 
            self.file = new_file 
    
    def is_valid_move(self, _rank, _file):
        raise NotImplementedError

if __name__ == "__main__":
    p = Piece(1,2)
   
    try:
        p.move_piece(2, 2)
    except NotImplementedError:
        print("Abstract class working")