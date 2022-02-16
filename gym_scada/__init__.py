from atexit import register
from gym.envs.registration import register

# register the environment version
register(id='scada-v0', entry_point='gym_scada.envs:ScadaEnv',)
register(id='scada-v2', entry_point='gym_scada.envs:ScadaEnv2',)
