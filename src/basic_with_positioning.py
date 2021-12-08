import chess

"""
Here is one example of an improvement to the basic chess model.

This model takes the position of pieces into account when calculating the min max score
which should make it more intellegent. However, there is deffinately room for improvement.

Also, feel free to copy the tables as they should already be reletively optimized
"""

class tables:
    """
    the class tables provides tables for ideal positions for your bot. All tables
    are symetric across the y-axis, so for black, you can just index the table backwards

    Feel free to change these, but these tables should already be relativily optimized
    """
    #Ideal positions for a white pawn
    pawn_table = [
        0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
        5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,
        1.0,1.0,2.0,3.0,3.0,2.0,1.0,1.0,
        0.5,0.5,1.0,2.5,2.5,1.0,0.5,0.5,
        0.0,0.0,0.0,2.0,2.0,0.0,0.0,0.0,
        0.5,-0.5,-1.0,0.0,0.0,-1.0,-0.5,0.5,
        0.5,1.0,1.0,-2.0,-2.0,1.0,1.0,0.5,
        0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    ]

    knight_table = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, 4.0, -5.0,
        -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
        -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,       
        -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
        -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
        -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
        -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
    ]

    bishop_table = [
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
        -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
        -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
        -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
        -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
        -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
        -2.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -2.0
    ]

    rook_table = [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0 , 0.0, 0.0, 0.0 , 0.0, -0.5,
        -0.5, 2.0, 0.0 , 0.0, 0.0 , 2.0 , 0.0 , -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0
    ]

    queen_table = [
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
        -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
        -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
        0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
        -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
        -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
    ]

    king_table = [
        -3.0, -4.0, 4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, 4.0, -5.0, -5.0, -4.0, 4.0, -3.0,
        -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
        -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
        2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
        2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0
    ]


class StubAgent:
    """
    Your agent class. Please rename this to {TeamName}Agent, and this file to {TeamName}.py
    """
    depth = 3

    cache = {}

    def __init__(self, is_white):
        """
        Constructor, initialize your fields here.
        :param is_white: Initializes the color of the agent.
        """
        self.is_white = is_white

    @staticmethod
    def get_team_name():
        """
        Report your team name. Used for scoring purposes.+
        """
        return "stub"

    def heuristic(self, board):
        """
        Determine whose favor the board is in, and by how much.
        Positive values favor white, negative values favor black.

        :param board:
        :return: Returns the estimated utility of the board state.
        """
        # Evaluate scores of each piece
        value = sum(
            get_piece_utility(board.piece_at(square), square)
            if board.piece_at(square) is not None else 0
            for square in chess.SQUARES
        )


        # If this is a draw, value is 0 (same for both players)
        if board.can_claim_draw():
            value = 0

        return value

    def make_move(self, board):
        """
        Determine the next move to make, given the current board.
        :param board: The chess board
        :return: The selected move
        """
        global_score = -1e8 if self.is_white else 1e8
        chosen_move = None

        for move in board.legal_moves:
            board.push(move)

            local_score = self.minimax(board, self.depth - 1, not self.is_white, -1e8, 1e8)
            self.cache[hash_board(board, self.depth - 1, not self.is_white)] = local_score

            if self.is_white and local_score > global_score:
                global_score = local_score
                chosen_move = move
            elif not self.is_white and local_score < global_score:
                global_score = local_score
                chosen_move = move

            board.pop()

        return chosen_move

    def minimax(self, board, depth, is_maxing_white, alpha, beta):
        """
        Minimax implementation with alpha-beta pruning.

        Source: https://github.com/devinalvaro/yachess

        :param board: Chess board
        :param depth: Remaining search depth
        :param is_maxing_white: Whose score are we maxing?
        :param alpha: Alpha-beta pruning value
        :param beta: Alpha-beta pruning value
        :return: The utility of the board state
        """
        # Check if board state is in cache
        if hash_board(board, depth, is_maxing_white) in self.cache:
            return self.cache[hash_board(board, depth, is_maxing_white)]

        # Check if game is over or we have reached maximum search depth.
        if depth == 0 or not board.legal_moves:
            self.cache[hash_board(board, depth, is_maxing_white)] = self.heuristic(board)
            return self.cache[hash_board(board, depth, is_maxing_white)]

        # General case
        best_score = -1e8 if is_maxing_white else 1e8
        for move in board.legal_moves:
            board.push(move)

            local_score = self.minimax(board, depth - 1, not is_maxing_white, alpha, beta)
            self.cache[hash_board(board, depth - 1, not is_maxing_white)] = local_score

            if is_maxing_white:
                best_score = max(best_score, local_score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, local_score)
                beta = min(beta, best_score)

            board.pop()

            if beta <= alpha:
                break
        self.cache[hash_board(board, depth, is_maxing_white)] = best_score
        return self.cache[hash_board(board, depth, is_maxing_white)]


def hash_board(board, depth, is_maxing_white):
    """
    Get a representation of the system that we can cache.
    """
    return str(board) + ' ' + str(depth) + ' ' + str(is_maxing_white)


def get_piece_utility(self, piece, position):
    """
    Get the utility of a piece.
    :return: Returns the standard chess score for the piece, positive if white, negative if black.
    """
    table_effect = 1 # tables have 1 times the effect, seems to go wonky if this is modified

    piece_symbol = piece.symbol()
    is_white = not piece_symbol.islower()
    index_direction = 1 if is_white else -1

    lower = piece_symbol.lower()
    score = 0

    if lower == 'p':
        score += 10
        score += tables.pawn_table[position * index_direction] * table_effect
    elif lower == 'n':
        score += 30
        score += tables.knight_table[position * index_direction] * table_effect
    elif lower == 'b':
        score += 30
        score += tables.bishop_table[position * index_direction] * table_effect
    elif lower == 'r':
        score += 50
        score += tables.rook_table[position * index_direction] * table_effect
    elif lower == 'q':
        score += 90
        score += tables.queen_table[position * index_direction] * table_effect
    elif lower == 'k':
        score += 900
        score += tables.king_table[position * index_direction] * table_effect
    
    score *= 1 if is_white else -1

    return score
