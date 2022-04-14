from setuptools import setup

setup(
    name="multi_repo_deploy",
    version='0.1',
    install_requires=[
        'Click',
        'gitpython'
    ],
    entry_points='''
        [console_scripts]
        mgit=src.main.cli:mgit
    ''',
)
