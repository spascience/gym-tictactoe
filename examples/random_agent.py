#!/usr/bin/env python
import random

from gym_tictactoe.env import TicTacToeEnv, agent_by_mark


class RandomAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, obs, ava_actions):
        return random.choice(ava_actions)


def play(max_episode=2):
    episode = 0
    env = TicTacToeEnv()
    agents = [RandomAgent('O'),
              RandomAgent('X')]

    while episode < max_episode:
        obs = env.reset()
        _, mark = obs
        done = False
        while not done:
            env.show_turn(True, mark)

            agent = agent_by_mark(agents, mark)
            ava_actions = env.available_actions()
            action = agent.act(obs, ava_actions)
            obs, reward, done, info = env.step(action)
            env.render()

            if done:
                env.show_result(True, mark, reward)
                break
            else:
                _, mark = obs
        episode += 1


if __name__ == '__main__':
    play()
