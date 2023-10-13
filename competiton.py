import brain
import max_n
import mcts
import time
import copy
from game import State

def play(state: State, player, time_list=None):
    state = copy.deepcopy(state)

    if len(state.legal_actions()) == 0:
        return state.next(None)

    start = time.time()
    next_state = player(state)
    end = time.time()
    print(f"turn: {state.turn}, player: {player.__name__}, runtime: {(end-start):.5f}", end='\r')

    run_time = end - start
    if time_list is not None:
        time_list.append(run_time)
    
    return next_state

time_list = []
r = 100
draws = 0

actions = [brain.brain1, brain.brain2, brain.brain3, max_n.max_n_action]
actions = [[action, 0] for action in actions]
for i in range(r):
    now_state= State()
    
    while(not now_state.is_done()):
        now_state = play(now_state, actions[0][0])
        if now_state.is_done():
            break

        now_state = play(now_state, actions[1][0])
        if now_state.is_done():
            break

        now_state = play(now_state, actions[2][0])
        if now_state.is_done():
            break

        now_state = play(now_state, actions[3][0])

    actions = actions[1:] + [actions[0]]

    if now_state.winner() != -1:
        actions[now_state.winner()][1] += 1
    else:
        draws += 1

    print(f"{i+1}/{r}: \
          {actions[0][0].__name__}: {actions[0][1]/r:.5f}, \
          {actions[1][0].__name__}: {actions[1][1]/r:.5f}, \
          {actions[2][0].__name__}: {actions[2][1]/r:.5f}, \
          {actions[3][0].__name__}: {actions[3][1]/r:.5f}, \
          draw: {draws/r:.5f}", end='\n', flush=True)