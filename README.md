# LuckBot: A Simple Bot that Tests Your Luck

## Overview
#### LuckBot is a basic discord bot that lets users test their luck. With `?luckMAXNUM YOURCHOICE`, you can choose the range (MAXNUM), and also give the bot the number you pick (YOURCHOICE). If your number matches bot's randomly generated number within the same range then congratulations, from me and the bot too. If not, unfortunate :(

## Features
- Accepts user input in the format `?luckMAXNUM YourChoice`.
- Generates a random number between 1 and `MAXNUM`.
- Compares the generated number with the user's choice.
- Sends either a congratulatory or an unfortunate message.
- Built with simple modules, making it lightweight, easy to understand and beginner-friendly.

## Installation & Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/Mikayn/luckbot.git
   cd luckbot
   ```
2. Install the libraries required from `requirements.txt`

3. Make your own bot in Discord's [developer portal.](https://discord.com/developers/applications)
4. Create a `.env` file and add your bot token as:
```sh
TOKEN=your_bot_token
```
5. Run the bot:
```sh
python main.py
```
## License
This project is a side-project and open-source. Feel free to contribute if you have ideas.
