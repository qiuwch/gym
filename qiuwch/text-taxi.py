import sys
sys.path.append('..')
import gym
env = gym.make("Taxi-v1")
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)


# Learn how to define reward
# How to evaluate a policy
# How to measure frame rate
