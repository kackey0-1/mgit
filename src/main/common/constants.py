from enum import Enum


class Action(Enum):
    SYNC = 'sync'
    COMMIT = 'commit'
    DEPLOY = 'deploy'


class Environment(Enum):
    DEV = 'dev'
    STG = 'stg'
    PERF = 'perf'
    PROD = 'prod'
