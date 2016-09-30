# The RealisticREndering tech demo produced by Epic Games.
import logging, gym
logger = logging.getLogger(__name__)

try:
    from unrealcv import client
    client.connect()
except:
    pass

error_msg = '''
Can not connect to RealisticRendering
'''

import cv2

# Need to define a task for reinforcement learning

# Encapsule the actions of a camera.
class ACamera(): # An UnrealCV agent which is simplified as a camera
    # This is an agent which uses UnrealCV commands to control the camera within the scene.
    pass

class ToyEnv(gym.Env):
    metadata = {
        'render.modes': ['human']
        # human will show the rendering for human also
    }
    def __init__(self):
        # if not client.isconnected():
        #     # Also make sure the confirm message is from RealisticRendering
        #     raise gym.error.DependencyNotInstalled(error_msg)
        print 'Try to initialize the Env'
        pass
        # Make sure the client is correctly connected to the server.
        # self.action_space = spaces. ??
        self.model = ACamera()
        # action_space and observation_space

    def _reset(self):
        # Reset this environment
        pass

    def _step(self, action):
        # What is a valid action?
        pass

        # What state is included?? hp?

        # return (state, reward, done, info)
        # observation : an environment-specific object representation
        # reward : for one action
        # done: lose all hp??


    def _render(self, mode='human', close=False):
        # What is mode?
        # What is the return value?
        filename = client.request('vget /camera/0/lit')
        # Make sure filename is valid
        im = cv2.imread(filename)

        # Return an rgb array
        return im

class FirstPersonShooter(gym.Env):
    pass
