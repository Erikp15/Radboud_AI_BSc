from heuristics import Heuristic, ParityHeuristic, SimpleHeuristic, NoHeuristic
from players import PlayerController, HumanPlayer, MinMaxPlayer, AlphaBetaPlayer
from board import Board
from typing import List
import numpy as np
from numba import jit
import copy

def start_game(game_n: int, board: Board, players: List[PlayerController]) -> int:
    """Starting a game and handling the game logic

    Args:
        game_n (int): n in a row required to win
        board (Board): board to play on
        players (List[PlayerController]): players of the game

    Returns:
        int: id of the winning player, or -1 if the game ends in a draw
    """
    print('Start game!')
    current_player_index: int = 0 # index of the current player in the players list
    winner: int = 0
    num_of_moves = 0
    Game_states: board = []
    # Main game loop
    while winner == 0:
        current_player: PlayerController = players[current_player_index]
        move: int = current_player.make_move(board)
        while not board.play(move, current_player.player_id):
            move = current_player.make_move(board)
        num_of_moves += 1
        current_player_index = 1 - current_player_index
        print(board)
        Game_states.append(copy.deepcopy(board))
        winner = winning(board.get_board_state(), game_n)

    if winner < 0:
        print('Game is a draw!')
    else:
        print(f'Player {current_player} won!')

    for p in players:
        print(f'Player {p} evaluated on average {p.get_eval_count()/num_of_moves} board states per move!')

    return winner


@jit(nopython=True, cache=True)
def winning(state: np.ndarray, game_n: int) -> int:
    """Determines whether a player has won, and if so, which one

    Args:
        state (np.ndarray): the board to check
        game_n (int): n in a row required to win

    Returns:
        int: 1 or 2 if the respective player won, -1 if the game is a draw, 0 otherwise
    """
    player: int
    counter: int

    # Vertical check
    for col in state:
        counter = 0
        player = -1
        for field in col[::-1]:
            if field == 0:
                break
            elif field == player:
                counter += 1
                if counter >= game_n:
                    return player
            else:
                counter = 1 
                player = field
            
    # Horizintal check
    for row in state.T:
        counter = 0
        player = -1
        for field in row:
            if field == 0:
                counter = 0
                player = -1
            elif field == player:
                counter += 1
                if counter >= game_n:
                    return player
            else:
                counter = 1
                player = field

    # Ascending diagonal check
    for i, col in enumerate(state[:- game_n + 1]):
        for j, field in enumerate(col[game_n - 1:]):
            if field == 0:
                continue
            player = field
            for x in range(game_n):
                if state[i + x, j + game_n - 1 - x] != player:
                    player = -1
                    break
            if player != -1:
                return player
            
    # Descending diagonal check
    for i, col in enumerate(state[game_n - 1:]):
        for j, field in enumerate(col[game_n - 1:]):
            if field == 0:
                continue
            player = field
            for x in range(game_n):
                if state[i + game_n - 1 - x, j + game_n - 1 - x] != player:
                    player = -1
                    break
            if player != -1:
                return player
        
    # Check for a draw
    if np.all(state[:, 0]):
        return -1 # The board is full, game is a draw

    return 0 # Game is not over 
    

def get_players(game_n: int) -> List[PlayerController]:
    """Gets the two players

    Args:
        game_n (int): n in a row required to win

    Raises:
        AssertionError: if the players are incorrectly initialised

    Returns:
        List[PlayerController]: list with two players
    """
    heuristic1: Heuristic = NoHeuristic(game_n)
    heuristic2: Heuristic = NoHeuristic(game_n)

    human1: PlayerController = MinMaxPlayer(1, game_n, depth_1, heuristic1)
    human2: PlayerController = AlphaBetaPlayer(2, game_n, depth_2, heuristic2)

    # TODO: Implement other PlayerControllers (MinMaxPlayer and AlphaBetaPlayer)

    players: List[PlayerController] = [human1, human2]

    assert players[0].player_id in {1, 2}, 'The player_id of the first player must be either 1 or 2'
    assert players[1].player_id in {1, 2}, 'The player_id of the second player must be either 1 or 2'
    assert players[0].player_id != players[1].player_id, 'The players must have an unique player_id'
    assert players[0].heuristic is not players[1].heuristic, 'The players must have an unique heuristic'
    assert len(players) == 2, 'Not the correct amount of players'

    return players


if __name__ == '__main__':
    game_n: int = 4 # n in a row required to win
    width: int = 7  # width of the board
    height: int = 6 # height of the board
    depth_1: int = 5 # maximum depth of player 1 search
    depth_2: int = 5 # maximum depth of player 2 search
    # Check whether the game_n is possible
    print("Input board width:")
    width = int(input())
    print("Input board height:")
    height = int(input())    
    print("Input number of moves to win:")
    game_n = int(input())
    assert 1 < game_n <= min(width, height), 'game_n is not possible'

    board: Board = Board(width, height)
    start_game(game_n, board, get_players(game_n))
