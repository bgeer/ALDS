import copy
import random


class GameTreeNode2:
    def __init__(self, gstate, parentNode=None, last_move=None):
        self.state = gstate
        self.finished, self.won = checkFinishedAndWhoWon(self.state)
        self.parent = parentNode
        self.children = []
        self.move = last_move
        self.value = None

    # please implement some way to compute the values for each node in the tree
    # such that this next function gives us the right answer
    def best_move(self):
        best_value = self.value
        for ch in self.children:
            if ch.value is best_value:
                return ch.move
        return None  # if this node does not have children

    def score(self):
        if self.finished:
            if self.won == 1:
                return 1
            elif self.won == 2:
                return -1
            else:
                return self.won
        else:
            if self.state[0] == 1:
                self.value = -2
                for child in self.children:
                    self.value = max(child.score(), self.value)
            else:
                self.value = 2
                for child in self.children:
                    self.value = min(child.score(), self.value)
        return self.value


def prettyPrintTTT(game_state):
    result = "\n"
    for i in range(3):
        result += "           "
        for j in range(3):
            if game_state[1][i][j] == 1:
                result += "x "
            elif game_state[1][i][j] == 2:
                result += "o "
            else:
                result += "- "
        result += "\n"
    result += "\n"
    if game_state[0] == 2:
        result += "   naughts (\'o\') to move"
    else:
        result += "   crosses (\'x\') to move"
    print(result)


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


def valid_moves(state):
    valid = []
    for i in range(len(state[1])):
        for j in range(len(state[1][i])):
            if state[1][i][j] == 0:
                valid.append((i, j))
    return valid


# B: getting a new game state
def play(game_state, move):  # move is a tuple indicating where the player to move is going to place a stone
    new_game_state = ((1 if (game_state[0] == 2) else 2), copy.deepcopy(game_state[1]))
    if new_game_state[1][move[0]][move[1]] == 0:
        new_game_state[1][move[0]][move[1]] = game_state[0]
    else:
        return None  # invalid move
    return new_game_state


def expandAllByOnePly2(game_tree_node, valid_moves):
    if game_tree_node.finished:
        return False # Nothing to do here, the game is finished
    for move in valid_moves:
        new_state = play(game_tree_node.state, move)
        game_tree_node.children.append(GameTreeNode2(new_state, parentNode=game_tree_node, last_move=move))
    return True


def tree2String(game_tree_node, prefix=""):
    result = ""
    if game_tree_node is not None:
        result += prefix + str(int(len(prefix) / 2)) + ": " + str(game_tree_node.state) + "\n"
        result += prefix + "{\n"
        cprefix = (prefix + "  ")
        for child in game_tree_node.children:
            result += tree2String(child, cprefix)
        result += prefix + "}\n"
    return result


def expandAllFinal2(game_tree_node):
    if game_tree_node.finished:
        return True
    for i in range(len(game_tree_node.children)):
        expandAllByOnePly2(game_tree_node.children[i], valid_moves(game_tree_node.children[i].state))
        expandAllFinal2(game_tree_node.children[i])


state = (1, [[2, 2, 1], [1, 0, 2], [0, 0, 1]])
root = GameTreeNode2(state)

expandAllByOnePly2(root, valid_moves(state))
expandAllFinal2(root)
print(tree2String(root))

root.score()
print(root.best_move())


state2 = play(state, root.best_move())
root2 = GameTreeNode2(state2)

expandAllByOnePly2(root2, valid_moves(state2))
expandAllFinal2(root2)
print(tree2String(root2))

root2.score()
print(root2.best_move())