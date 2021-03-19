import copy
import random


class GameTreeNode3:
    def __init__(self, gstate, parentNode=None, last_move=None, valid_move_list=None):
        self.state = gstate
        self.finished, self.won = checkFinishedAndWhoWon(self.state)
        self.parent = parentNode
        self.children = []
        self.move = last_move
        self.Q = 0  # number of wins
        self.N = 0  # number of visits
        self.valid_moves = valid_move_list

    def fully_expanded(self):
        return len(self.children) == len(self.valid_moves)

    def expand(self, move, n_rollouts):
        # when expanding a node with a new child node, we are not also going to perform a number of roll-outs.
        # first, we create the new node:
        new_state = play(self.state, move)
        if new_state is None:
            return
        new_valid_moves = copy.deepcopy(self.valid_moves)
        new_valid_moves.remove(move)
        new_node = GameTreeNode3(new_state, parentNode=self, last_move=move, valid_move_list=new_valid_moves)
        # add it to the children:
        self.children.append(new_node)
        # and then perform a number of random roll-outs: random plays until the game finishes
        for i in range(n_rollouts):
            score = new_node.roll_out()
            # and process the result (score) we get from this rollout
            new_node.process_result(score)

    def roll_out(self):
        # rollouts are quite simple
        # when the node respresents a game state of a game that's finished, we immediately return the result
        if self.finished:
            if self.won == 1:
                return 1
            elif self.won == 2:
                return -1
            else:
                return 0
        # else we play moves in on the remaining open fields
        moves = copy.deepcopy(self.valid_moves)
        random.shuffle(moves)
        new_state = self.state
        for move in moves:
            new_state = play(new_state, move)
            fin, whowon = checkFinishedAndWhoWon(new_state)
            # until the game finishes, and return the score:
            if fin:
                if whowon == 1:
                    return 1
                elif whowon == 2:
                    return -1
                else:
                    return 0

    def process_result(self, rollout_result):
        # then we increase Q by the score, and N by 1
        self.Q += rollout_result
        self.N += 1
        # and do the same, recursively, for its ancestors
        if self.parent is not None:
            self.parent.process_result(rollout_result)


def checkFinishedAndWhoWon(game_state):
    open_fields = False
    who_won = 0  # default: no one
    board = game_state[1]
    # check lines
    for i in [0, 1, 2]:
        player = board[i][0]
        line = True
        for j in [0, 1, 2]:
            if board[i][j] == 0:
                open_fields = True
                line = False
                break
            if board[i][j] != player:
                line = False
                break
        if line:
            return True, player
    # check columns
    for i in [0, 1, 2]:
        player = board[0][i]
        line = True
        for j in [0, 1, 2]:
            if board[j][i] != player:
                line = False
                break
        if line:
            return True, player
    # check diagonals
    player = board[1][1]  # the middle
    if player == 0:
        return False, 0
    if (board[0][0] == player) and (board[2][2] == player):
        return True, player
    if (board[2][0] == player) and (board[0][2] == player):
        return True, player
    return not open_fields, 0


# B: getting a new game state
def play(game_state, move):  # move is a tuple indicating where the player to move is going to place a stone
    new_game_state = ((1 if (game_state[0] == 2) else 2), copy.deepcopy(game_state[1]))
    if new_game_state[1][move[0]][move[1]] == 0:
        new_game_state[1][move[0]][move[1]] = game_state[0]
    else:
        return None  # invalid move
    return new_game_state


def tree2StringWithValues(game_tree_node3, prefix=""):
    result = ""
    if game_tree_node3 is not None:
        result += prefix + str(int(len(prefix) / 2)) + ": " + str(game_tree_node3.state) + "\n"
        result += prefix + "value: " + str(game_tree_node3.Q / game_tree_node3.N) + "\n"
        result += prefix + "{\n"
        cprefix = (prefix + "  ")
        for child in game_tree_node3.children:
            result += tree2StringWithValues(child, cprefix)
        result += prefix + "}\n"
    return result


def best_next_move(game_tree_node3):
    if not game_tree_node3.children:
        print("list empty")
        return
    max_child = [0, game_tree_node3.children[0].Q / game_tree_node3.children[0].N]
    for i in range(len(game_tree_node3.children)):
        if max_child[1] < (game_tree_node3.children[i].Q / game_tree_node3.children[i].N):
            max_child[0] = i
            max_child[1] = game_tree_node3.children[i].Q / game_tree_node3.children[i].N
    return game_tree_node3.children[max_child[0]].move


# when we do this, with a 100 roll-outs for each child node, we get value estimates (not exact values, just estimates)
# for each child node:
state = (1, [[2, 2, 1], [1, 0, 2], [0, 0, 1]])  # A possible game state after three moves (=6 plies)

root = GameTreeNode3(state, valid_move_list=[(1, 1), (2, 0), (2, 1)])
for mv in root.valid_moves:
    root.expand(mv, 100)
print(best_next_move(root))