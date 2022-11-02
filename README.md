<h1 align="center">A Lejondary Discord Basic Bot(ch)</h1>

## Description

Basic Bot(ch) is a simple Discord chatbot that will respond with a reciprocating YEEE when you yee!  

Developed using the Discord library and API, discord.py v2.0, for Python 3.10.8.  
-  Documentation:   
   `https://discordpy.readthedocs.io/en/stable/`  
-  v2.0 Changes:  
   `https://discordpy.readthedocs.io/en/stable/migrating.html`  

Python 3.8 and higher is currently supported.   

## Installation

-  Use Python 3.8 or higher
   >`https://www.python.org/downloads/`
-  Ensure that you have pip installed:
   >`https://pip.pypa.io/en/stable/getting-started/`  
   >`https://pip.pypa.io/en/stable/installation/`
-  Install dotenv from PyPI with the following command:
   >`pip install python-dotenv`
   >`https://pypi.org/project/python-dotenv/`
-  Install discord-pretty-help from PyPI with the following command:
   >`pip install discord-pretty-help`
   >`https://pypi.org/project/discord-pretty-help/`
-  Install the Discord library discord.py
   >`https://discordpy.readthedocs.io/en/latest/intro.html`
-  Create a Discord Bot Account
   >`https://discordpy.readthedocs.io/en/stable/discord.html#`
-  Locate and Copy Discord Bot Login Token 
   >`https://docs.discordbotstudio.org/setting-up-dbs/finding-your-bot-token`
-  Invite Basic Bot(ch) to your Server
   >`https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot`

## Setup

-  Clone the repository on your machine  
   >`https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository`
-  Create a .env file in the `basic_botch/` directory  
   >Make these 3 variables and insert your information:   
   ```bash
   BOT_TOKEN='YourToken'
   OWNER='YourDiscordID' # Numerical ID
   PREFIX='YourPrefix'
   ```
   >Save the file  
-  `IMPORTANT:` Add the '.env' file to your .gitignore file   
   >You must complete this step if you plan on sharing your code!  
-  `OPTIONAL:` If you want Basic Bot(ch) to announce its online status to a specific channel:  
   >On line 14 of `basic_botch/cogs/yee.py` file, input the desired channel's ID  
-  Run the `basic_botch.py` file on your OS
   >`$ py -3 basic_botch.py` for Windows  
   >`$ python3 basic_botch.py` for non-Windows
-  After running the file, Basic Bot(ch) will be online on your server!  

## To Use Basic Bot(ch):

-  Commands:
   >yee - Basic Bot(ch) will YEEE! in the channel where the command was called  

## TODO

- [x] pip pretty help
- [ ] fix unloading procedure
- [ ] .env channel ID
