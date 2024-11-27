### Project contribution setup

Clone the project
```shell script
git clone https://github.com/Happy-Kumar-Sharma/trace-logger.git
```
move into the project folder
```shell script
cd trace-logger
```

Install the virtualenv
```shell script
pip install virtualenv
```

Enter into virtual env
```shell script
python -m venv venv
```

Activate the virtual env
```shell script
source venv/Scripts/activate
```

Install packages from requirements.txt file
```shell script
pip install -r requirements.txt
```

Install pre-commit -- not to follow [Optional]
First, install the pre-commit package by running
```shell script
pip install pre-commit
```

Install the pre-commit hooks
```shell script
pre-commit install
```

Delete precommit hooks [Not required]
```shell script
pre-commit clean
```

Auto update precommit [Not required]
```shell script
pre-commit autoupdate
```

Check standard guidline of this project [Optional]
```shell script
pre-commit run --all-files
```

Install build tools:
```shell script
pip install build twine
```

Build the package:
```shell script
python -m build
```

Clean Previous Builds
```shell script
rm -rf dist build *.egg-info
```

Run the tests using
```shell script
pytest tests/
```
