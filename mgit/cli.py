import click
from mgit.common import MGit
from mgit.common.constants import Action, Environment

@click.command()
@click.argument('action')
@click.argument('imagetag')
@click.option('--environment', '-e', default='stg', help='')
def mgit(action, imagetag, environment):
    m = MGit()
    if Action.SYNC.value == action:
        m.sync()
    elif Action.COMMIT.value == action:
        m.sync()
        m.commit(imagetag, environment)
    elif Action.DEPLOY.value == action:
        m.sync()
        m.commit(imagetag, environment)
        m.push()


if __name__ == "__main__":
    print(Action.COMMIT.name)
