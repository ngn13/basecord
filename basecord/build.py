import sys
import os
import shutil
import json
import requests
import getpass
from zipfile import ZipFile
from colorama import init, Fore, Style
init(autoreset=True)

class Builder:
    def __init__(self):
        self.URL = "https://github.com/ngn13/basecord-template/archive/refs/heads/main.zip"
        self.ZIP = "tmp.zip"
        self.CONFIG = {}
        self.AUTHOR = "Anon"

        try:
            self.NAME = sys.argv[1]
        except:
            self.err("Usage: basecord <project_name>")

        if os.path.isdir(NAME) or os.path.exists(NAME):
            self.err(f"Directory '{NAME}' already exists")

        self.pr("Welcome to Basecord project creator tool")
        self.pr("Let me help you create your project!")
    
        self.ask()
        self.download()
        self.extract(NAME)
    
        self.pr("You are ready to go!")
        self.pr("Start your bot with "+Fore.CYAN+"python bot.py")
    
    def err(self, txt):
        print(Fore.RED+Style.BRIGHT+"! "+Fore.RESET+txt)
        exit()
    
    def pr(self, txt):
        print(Fore.MAGENTA+Style.BRIGHT+"> "+Fore.RESET+txt)
    
    def inp(self, txt):
        return input(Fore.GREEN+Style.BRIGHT+"? "+Fore.RESET+txt+": ")
    
    def secret(self, txt):
        return getpass.getpass(Fore.GREEN+Style.BRIGHT+"? "+Fore.RESET+txt+": ")
    
    def ask(self):
        self.CONFIG["token"] = self.secret("Discord token")
        self.CONFIG["guilds"] = self.inp("Guild IDs (split with comma)").replace(" ", "").split(",")
        self.AUTHOR = self.inp("Author")    

    def download(self):
        self.pr("Downloading the project template...")
        req = requests.get(self.URL)
        with open(self.ZIP, "wb") as f:
            f.write(req.content)
        self.pr("Done!")
    
    def extract(self):
        with ZipFile(ZIP, "r") as z:
            z.extractall(".")

        shutil.move("basecord-template-main", self.NAME)
        os.remove(self.ZIP)
        os.chdir(self.NAME)

        f = open("README.md", "r")
        readme = f.read()
        f.close()

        f = open("LICENSE.txt", "r")
        license = f.read()
        f.close()

        readme = readme.replace("~author~", self.AUTHOR)
        license = license.replace("~author~", self.AUTHOR)

        f = open("README.md", "w")
        f.write(readme)
        f.close()

        f = open("LICENSE.txt", "w")
        f.write(license)
        f.close()

        f = open("config.json", "w")
        f.write(json.dumps(self.CONFIG))
        f.close()

def main():
    Builder()
    
if __name__ == "__main__":
    main()