# py_cli_template

## How to Build
```sh
# build, aka PyPA build, is the more modern PEP517
# equivalent of the older setup.py sdist bdist_wheel build command with which you might be familiar
# If you’ve not done this before, you can install the build tool like this:
$ pip install build

# Now, in the root of your project directory, you can run:
$ python -m build
```

## Install your wheel with pip
```sh
$ pip install dist/<packagename>-<version>-py3-none-any.whl
```

## How to run all unittests
```sh
$ python -m pytest -s
```

## Testing your install in a clean environment
```sh
# create virtual environment
$ python3 -m venv .env/fresh-install-test

# activate your virtual environment
$ . .env/fresh-install-test/bin/activate

# install your package into this fresh environment
$ pip install dist/<packagename>-<version>-py3-none-any.whl

# your shortcuts are now in the venv bin directory
$ ls .env/fresh-install-test/bin/
clitool1
clitool2

# so you can run it directly from the cli
$ clitool1 world

# and run the second application
$ clitool2 world
```

I created this template based on [How to package and deploy CLI applications with Python PyPA setuptools build](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/).
Check out more details [here](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)
