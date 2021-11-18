# ScatterBrain

Wait I already made this, except this is a more universal variant as well as a rewrite to a framework I'm more familiar with.
So since this is intended to be "general purpose" I'm going to use it to create fun commands, music and YDL functionality as well as give me complete control of the servers it's in, like a normal person would.

## Installation guide

Since this project uses pipenv to maintain it's dependencies running the command `pipenv install` will install the related dependencies.
This project utilises a json config file, an example of the structure can be found in the root directory under `config.example.json`. As a quick start you can rename the file to `config.json` and change the values to what you need.
Let this serve as an active reminder to **NOT SAVE YOUR TOKENS IN PUBLIC PLACES**, always ignore your token files or use environment variables.
The command `pipenv run main` or executing `python .\main,py` while inside the pipenv shell will activate the bot and attempt to run it.
