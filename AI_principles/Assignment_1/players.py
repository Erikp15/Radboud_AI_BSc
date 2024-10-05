from __future__ import annotations
from abc import abstractmethod
import numpy as np
from typing import TYPE_CHECKING
import time
if TYPE_CHECKING:
    from heuristics import Heuristic
    from board import Board


class PlayerController:
    """Abstract class defining a player
    """
    def __init__(self, player_id: int, game_n: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            heuristic (Heuristic): heuristic used by the player
        """
        self.player_id = player_id
        self.game_n = game_n
        self.heuristic = heuristic


    def get_eval_count(self) -> int:
        """
        Returns:
            int: The amount of times the heuristic was used to evaluate a board state
        """
        return self.heuristic.eval_count
    

    def __str__(self) -> str:
        """
        Returns:
            str: representation for representing the player on the board
        """
        if self.player_id == 1:
            return 'X'
        return 'O'
        

    @abstractmethod
    def make_move(self, board: Board) -> [int, float]:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        pass


class MinMaxPlayer(PlayerController):
    """Class for the minmax player using the minmax algorithm
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, depth: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 0 (-1 = empty)
            game_n (int): n in a row required to win
            depth (int): the max search depth
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)
        self.depth: int = depth


    def make_move(self, board: board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int, int: evaluation of position column to play in
        """
        # Checks if the game has been won by a player
        
        # TODO: implement minmax algortihm!
        # INT: use the functions on the 'board' object to produce a new board given a specific move
        # HINT: use the functions on the 'heuristic' object to produce evaluations for the different board states!
        
        # Example:
                            
        # This is obviously not enough (this is depth 1)
        # Your assignment is to create a data structure (tree) to store the gameboards such that you can evaluate a higher depths.
        # Then, use the minmax algorithm to search through this tree to find the best move/action to take!
        start_time = time.time()
        best_move: [int, float] = self.explore_pos(board, 1, 1)
        print("--- %s seconds ---" % (time.time() - start_time))
        return best_move[0]

    def explore_pos(self, board: board, curr_depth: int, curr_player_id: int) -> [int, float]:

        best_eval: [int, float] = [-1, -np.inf]
        if curr_player_id == 2:
            best_eval[1] = np.inf

        victory_checker = self.heuristic.get_best_action(curr_player_id, board)

        if victory_checker[1] == np.inf or victory_checker[1] == -np.inf or curr_depth == self.depth:
            return victory_checker

        for col in range(board.width):
            if board.is_valid(col):
                new_board: board = board.get_new_board(col, curr_player_id)
                if curr_player_id == 1:
                    curr_eval: [int, float] = [col, self.explore_pos(new_board, curr_depth + 1, 2)[1]]
                    #print("max " + str(curr_depth) + " " + str(col) + " " + str(curr_eval[1]))
                    if best_eval[1] <= curr_eval[1] :
                        best_eval = curr_eval
                else:
                    curr_eval: [int, float] = [col, self.explore_pos(new_board, curr_depth + 1, 1)[1]]
                    #print("min " + str(curr_depth) + " " + str(col) + " " + str(curr_eval[1]))
                    if best_eval[1] >= curr_eval[1] :
                        best_eval = curr_eval

        return best_eval
    
    

class AlphaBetaPlayer(PlayerController):
    """Class for the minmax player using the minmax algorithm with alpha-beta pruning
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, depth: int, alpha: float, beta: float, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 0 (-1 = empty)
            game_n (int): n in a row required to win
            depth (int): the max search depth
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)
        self.depth: int = depth
        self.alpha: float = -np.inf
        self.beta: float = np.inf


    def make_move(self, board: board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int, int: evaluation of position column to play in
        """
        # Checks if the game has been won by a player
        
        # TODO: implement minmax algortihm!
        # INT: use the functions on the 'board' object to produce a new board given a specific move
        # HINT: use the functions on the 'heuristic' object to produce evaluations for the different board states!
        
        best_move: [int, float] = self.explore_pos(board, 1, 1)
        return best_move[0]

    def explore_pos(self, board: board, curr_depth: int, curr_player_id: int) -> [int, float]:

        best_eval: [int, float] = [-1, -np.inf]
        if curr_player_id == 2:
            best_eval[1] = np.inf

        victory_checker = self.heuristic.get_best_action(curr_player_id, board)

        if victory_checker[1] == np.inf or victory_checker[1] == -np.inf or curr_depth == self.depth:
            return victory_checker

        for col in range(board.width):
            if board.is_valid(col):
                new_board: board = board.get_new_board(col, curr_player_id)
                if curr_player_id == 1:
                    curr_eval: [int, float] = [col, self.explore_pos(new_board, curr_depth + 1, 2)[1]]
                    #print("max " + str(curr_depth) + " " + str(col) + " " + str(curr_eval[1]))
                    if best_eval[1] <= curr_eval[1] :
                        best_eval = curr_eval
                else:
                    curr_eval: [int, float] = [col, self.explore_pos(new_board, curr_depth + 1, 1)[1]]
                    #print("min " + str(curr_depth) + " " + str(col) + " " + str(curr_eval[1]))
                    if best_eval[1] >= curr_eval[1] :
                        best_eval = curr_eval

        return best_eval


class HumanPlayer(PlayerController):
    """Class for the human player
    Inherits from Playercontroller
    """
    def __init__(self, player_id: int, game_n: int, heuristic: Heuristic) -> None:
        """
        Args:
            player_id (int): id of a player, can take values 1 or 2 (0 = empty)
            game_n (int): n in a row required to win
            heuristic (Heuristic): heuristic used by the player
        """
        super().__init__(player_id, game_n, heuristic)

    
    def make_move(self, board: Board) -> int:
        """Gets the column for the player to play in

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        print(board)

        if self.heuristic is not None:
            best_move = self.heuristic.get_best_action(self.player_id, board)
            print(f'Heuristic {self.heuristic} calculated the best move is:', end=' ')
            print(best_move[0] + 1, end='\n\n')

        col: int = self.ask_input(board)

        print(f'Selected column: {col}')
        return col - 1
    

    def ask_input(self, board: Board) -> int:
        """Gets the input from the user

        Args:
            board (Board): the current board

        Returns:
            int: column to play in
        """
        try:
            col: int = int(input(f'Player {self}\nWhich column would you like to play in?\n'))
            assert 0 < col <= board.width
            assert board.is_valid(col - 1)
            return col
        except ValueError: # If the input can't be converted to an integer
            print('Please enter a number that corresponds to a column.', end='\n\n')
            return self.ask_input(board)
        except AssertionError: # If the input matches a full or non-existing column
            print('Please enter a valid column.\nThis column is either full or doesn\'t exist!', end='\n\n')
            return self.ask_input(board)
        