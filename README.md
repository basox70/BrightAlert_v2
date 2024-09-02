## How to Use (No installation)
:warning: ONLY available if bot is online

You don't need to install the github repo. You can just join the server in order to DM the bot
link: https://discord.gg/mUpBKVZnYh (DM me on discord if link is down)

Then in your DM use the command: "!setup (email) (password)"

## How to Use (Local installation)

### Prerequisite
- [Python](https://www.python.org/) installed (version 3.12 is used for development)
- venv is recommened [docs](https://docs.python.org/3.9/library/venv.html)
- Have a discord bot available : https://discord.com/developers/applications

### Installation
- Download github folder
- Run cmd and move to the extracted folder
- [Optionnal] Create venv
- Install the requirements : `py -m pip install -r requirements.txt`
- If needed replace browser in `main.py` line 83 (default : ChromiumEdge)(Available : Chrome, Edge, Firefox, ChromiumEdge, Ie)
- [Mandatory] Copy `config-sample.yml` to `config.yml` and update the token with the one you have
- In the cmd, run `py main.py`
- Use `ctrl-C` to stop the bot

## What's next for BrightAlert_v2
Feel free to contact me if you want to help in this project
