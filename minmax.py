import math
def minimax(self, game_state, current_player, depth=None):
        max_player = self.player_mark
        other_player = 'O' if current_player == 'X' else 'X'

        if game_state.winner == other_player:
            return {'position': None, 'score': 1 * (game_state.count_empty_squares() + 1) if other_player == max_player else -1 * (game_state.count_empty_squares() + 1)}

        elif not game_state.empty_squares_exist():
            return {'position': None, 'score': 0}

        # Fix for depth: if depth is None, we don't check for depth limit
        if depth is not None and depth == 0:
            return {'position': None, 'score': 0}

        if current_player == max_player:
            best_score = {'position': None, 'score': -math.inf}
        else:
            best_score = {'position': None, 'score': math.inf}

        for move in game_state.available_moves():
            game_state.make_move(move, current_player)
            # Make sure to decrement depth only when it's not None
            new_depth = depth - 1 if depth is not None else None
            simulated_result = self.minimax(game_state, other_player, new_depth)

            game_state.board[move] = ' '  # Undo move
            game_state.winner = None
            simulated_result['position'] = move

            if current_player == max_player:
                if simulated_result['score'] > best_score['score']:
                    best_score = simulated_result
            else:
                if simulated_result['score'] < best_score['score']:
                    best_score = simulated_result

        return best_score

