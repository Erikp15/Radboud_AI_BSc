from __future__ import annotations
import numpy as np
from abc import abstractmethod
from numba import jit, int32, float32
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board


class Heuristic:
    """Abstract class defining a heuristic
    """
    def __init__(self, game_n: int) -> None:
        """
        Args:
            game_n (int): n in a row required to win
        """
        self.game_n: int = game_n
        self.eval_count: int = 0


    def get_best_action(self, player_id: int, board: Board) -> [int, float]:
        """Determines the best column for the next move

        Args:
            player_id (int): the player for which to compute the heuristic value
            board (Board): the board to evaluate

        Returns:
            int: column with the best heuristic value
        """
        utils: np.ndarray = []
        if player_id == 1:
            utils = np.full(board.width, -np.inf, dtype=float)
        else:
            utils = np.full(board.width, np.inf, dtype=float)

        for i in range(board.width):
            if board.is_valid(i):
                self.eval_count += 1
                utils[i] = self.evaluate_board(player_id, board.get_new_board(i, player_id))

        if player_id == 1:
            return (np.argmax(utils), np.max(utils))
        else:
            return (np.argmin(utils), np.min(utils))
    

    def evaluate_board(self, player_id: int, board: Board) -> float:
        """Helper function to assign a utility to a board

        Args:
            player_id (int): the player for which to compute the heuristic value
            board (Board): the board to evaluate

        Returns:
            float: the utility of a board
        """
        state: np.ndarray = board.get_board_state()
        return self._evaluate(player_id, state, self.winning(state, self.game_n))
    

    @staticmethod
    def winning(state: np.ndarray, game_n: int) -> int:
        """Determines whether a player has won, and if so, which one

        Args:
            state (np.ndarray): the board to check
            game_n (int): n in a row required to win

        Returns:
            int: 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise
        """
        from app import winning as app_winning # imported here to avoid circular imports
        return app_winning(state, game_n)
    

    def __str__(self) -> str:
        """ 
        Returns:
            str: name of the heuristic
        """
        return self._name()


    @abstractmethod
    def _name(self) -> str:
        """Abstract method for naming the heuristic

        Returns:
            str: name of the heuristic
        """
        pass


    @abstractmethod
    def _evaluate(self, player_id: int, state: np.ndarray, winner: int) -> float:
        """Abstract method for evaluating a board state

        Args:
            player_id (int): the player for which to compute the heuristic value
            state (np.ndarray): the board to check
            winner (int): 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise

        Returns:
            float: heuristic value for the board state
        """
        pass    


class SimpleHeuristic(Heuristic):
    """A simple heuristic
    Inherits from Heuristic
    """
    def __init__(self, game_n: int) -> None:
        """
        Args:
            game_n (int): n in a row required to win
        """
        super().__init__(game_n)


    def _name(self) -> str:
        """
        Returns:
            str: the name of the heuristic; Simple
        """
        return 'Simple'
    
    @staticmethod
    @jit(nopython=True, cache=True)
    def _evaluate(player_id: int, state: np.ndarray, winner: int) -> float:
        """Determine utility of a board state

        Args:
            player_id (int): the player for which to compute the heuristic value
            state (np.ndarray): the board to check
            winner (int): 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise

        Returns:
            float: heuristic value for the board state
        """
        width: int
        height: int
        width, height = state.shape

        if winner == 1: # player 1 won
            return np.inf
        elif winner < 0: # draw
            return 0.
        elif winner == 2: # player 2 won
            return -np.inf
        
        # not winning or losing, return highest number of claimed squares in a row      
        max_in_row: int = 0
        for i in range(width):
            for j in range(height):
                if state[i, j] != player_id:
                    continue

                max_in_row = max(max_in_row, 1)

                for x in range(1, width - i):
                    if state[i + x, j] == player_id:
                        max_in_row = max(max_in_row, x + 1)
                    else:
                        break

                for y in range(1, height - j):
                    if state[i, j + y] == player_id:
                        max_in_row = max(max_in_row, y + 1)
                    else:
                        break

                for d in range(1, min(width - i, height - j)):
                    if state[i + d, j + d] == player_id:
                        max_in_row = max(max_in_row, d + 1)
                    else:
                        break

                for a in range(1, min(width - i, j)):
                    if state[i + a, j - a] == player_id:
                        max_in_row = max(max_in_row, a + 1)
                    else:
                        break

        return float(max_in_row)

class NoHeuristic(Heuristic):
    """A simple heuristic
    Inherits from Heuristic
    """
    def __init__(self, game_n: int) -> None:
        """
        Args:
            game_n (int): n in a row required to win
        """
        super().__init__(game_n)


    def _name(self) -> str:
        """
        Returns:
            str: the name of the heuristic; Simple
        """
        return 'Simple'
    
    @staticmethod
    @jit(nopython=True, cache=True)
    def _evaluate(player_id: int, state: np.ndarray, winner: int) -> float:
        """Determine utility of a board state

        Args:
            player_id (int): the player for which to compute the heuristic value
            state (np.ndarray): the board to check
            winner (int): 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise

        Returns:
            float: heuristic value for the board state
        """
        width: int
        height: int
        width, height = state.shape


        if winner == 1: # player 1 won
            return np.inf
        elif winner < 0: # draw
            return 0.
        elif winner == 2: # player 2 won
            return -np.inf
        return -1
    
class ParityHeuristic(Heuristic):
    """A simple heuristic
    Inherits from Heuristic
    """
    def __init__(self, game_n: int) -> None:
        """
        Args:
            game_n (int): n in a row required to win
        """
        super().__init__(game_n)


    def _name(self) -> str:
        """
        Returns:
            str: the name of the heuristic; Simple
        """
        return 'Simple'
    
    @staticmethod
    @jit(nopython=True, cache=True)
    def _evaluate(player_id: int, state: np.ndarray, winner: int) -> float:
        """Determine utility of a board state

        Args:
            player_id (int): the player for which to compute the heuristic value
            state (np.ndarray): the board to check
            winner (int): 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise

        Returns:
            float: heuristic value for the board state
        """
        width: int
        height: int
        width, height = state.shape


        if winner == 1: # player 1 won
            return np.inf
        elif winner < 0: # draw
            return 0.
        elif winner == 2: # player 2 won
            return -np.inf

        eval: float = 0
        for row in range(height):
            if height-row % 2 == 1:
                for col in range(width):
                    if state[row, col] == 1:
                        eval += 3
                        eval += abs(width/2 - col)
                    if state[row, col] == 2:
                        eval -= abs(width/2 - col)
            else:
                for col in range(width):
                    if state[row, col] == 1:
                        eval += abs(width/2 - col)
                    if state[row, col] == 2:
                        eval -= 3
                        eval -= abs(width/2 - col)                        
        return eval