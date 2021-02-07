## How to Use
You don't need to install the github repo. You can just join our server in order to DM the bot
link: https://discord.gg/ACXtYNnH

Then in your DM use the command: '!setup <email> <password>'

## Inspiration
We observed that the majority of software engineering students use discord as a way to communicate with other students regarding their online courses. Thus, we created a discord bot that can be installed on a server or accessed through dm's that after a simple one-command setup process sends you updates from your BrightSpace account.

## What it does
We made a discord bot that notifies students in their discord DM on their recent notifications that they've got on BrightSpace.

## How we built it
We built it using discord.py and pyautogui as well as selenium webdriver

## Challenges we ran into
Due to some students having two-factor authentication, it was troublesome for us to detect who had it and give them enough time to authenticate using their phone. Another problem we ran into is the fact that BrightSpace was difficult to navigate using chrome's inspect function. Many buttons had no IDs and shared classes which caused troubles for us.

## Accomplishments that we're proud of
We were able to make the bot communicate with a user through DM without exposing or keeping the user's information. We were also able to locate the notifications on the page and send them through DM by taking a screenshot.

## What we learned
We expanded our knowledge by learning new modules; such as pyautogui, selenium, and discord.py

## What's next for BrightAlert
We will try to advertise BrightAlert to students as we believe this bot could be of huge convenience to them.
