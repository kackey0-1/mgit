from setuptools import setup

setup(
    name="multi_repo_deploy",
    version='0.0.3',
    install_requires=[
        'Click',
        'gitpython'
    ],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mgit=mgit.cli:mgit',
        ],
    },
)
