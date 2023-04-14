import sys
import os
import shutil
import requests
import getpass
from zipfile import ZipFile
from colorama import init, Fore, Style
init(autoreset=True)

URL = "https://github.com/ngn13/basecord-template/archive/refs/heads/main.zip"
ZIP = "tmp.zip"
CONFIG = {}
AUTHOR = "Anon"

def err(txt):
    print(Fore.RED+Style.BRIGHT+"! "+Fore.RESET+txt)
    exit()

def pr(txt):
    print(Fore.MAGENTA+Style.BRIGHT+"> "+Fore.RESET+txt)

def inp(txt):
    return input(Fore.GREEN+Style.BRIGHT+"? "+Fore.RESET+txt+": ")

def secret(txt):
    return getpass.getpass(Fore.GREEN+Style.BRIGHT+"? "+Fore.RESET+txt+": ")

def ask():
    CONFIG["token"] = secret("Discord token")
    CONFIG["guilds"] = inp("Guild IDs (split with comma)").replace(" ", "").split(",")
    AUTHOR = inp("Author")    

def download():
    pr("Downloading the project template...")
    req = requests.get(URL)
    with open(ZIP, "wb") as f:
        f.write(req.content)
    pr("Done!")
    
def extract(name):
    with ZipFile(ZIP, "r") as z:
        z.extractall(".")
    
    shutil.move("basecord-template-main", name)
    os.chdir(name)
    
    f = open("README.md", "r")
    readme = f.read()
    f.close()

    f = open("LICENSE.txt", "r")
    license = f.read()
    f.close()

    readme = readme.replace("~author~", AUTHOR)
    license = license.replace("~author~", AUTHOR)

    f = open("README.md", "w")
    f.write(readme)
    f.close()

    f = open("LICENSE.txt", "w")
    f.write(license)
    f.close()

    f = open("config.json", "w")
    f.write(json.dumps(CONFIG))
    f.close()

def main():
    try:
        NAME = sys.argv[1]
    except:
        err("Usage: basecord <project_name>")

    if os.path.isdir(NAME) or os.path.exists(NAME):
        err(f"Directory '{NAME}' already exists")

    pr("Welcome to Basecord project creator tool")
    pr("Let me help you create your project!")
    ask()
    download()
    extract(NAME)
    pr("You are ready to go!")
    pr("Start your bot with "+Fore.CYAN+"python bot.py")
    
if __name__ == "__main__":
    main()