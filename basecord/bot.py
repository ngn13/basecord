import os
import sys
import asyncio
import nextcord
import pkgutil
import importlib
from shutil import rmtree
from nextcord import Intents
from nextcord.ext.commands import Bot as Bt

from basecord.util import set_status, get_status, check_guild
from basecord.config import Config
from basecord.db import Database

class Basecord(Bt):
    def __init__(self) -> None:
        self.basecord_version = "0.0.1"
        self.config = Config("config.json").cfg
        self.db = Database()
        self.mk_bot()
        self.register_cogs()
        self.banner()
        self.run(self.config["token"])

    def banner(self) -> None:
        header = f"## basecord v{self.basecord_version} | discord bot framework | github.com/ngn13/basecord ##"
        print("#"*len(header))
        print(header)
        print("#"*len(header))

    def mk_bot(self) -> None:
        intents = Intents().all()
        super().__init__(self.config["prefix"], intents=intents, status=get_status(self.config["status"]))

    def register_cogs(self):
        if not os.path.exists("cogs") or not os.path.isdir("cogs"):
            return
        
        for cogfile in os.listdir("cogs"):
            cogfile = "cogs/"+cogfile
            if os.path.isdir(cogfile):
                continue
            f = open(cogfile, "r")
            contents = f.read()
            f.close()
            if check_guild(contents):
                continue
            contents = "GUILDS = []\n"+contents
            f = open(cogfile, "w")
            f.write(contents)
            f.close()

        for importer, package_name, _ in pkgutil.iter_modules(["cogs"]):
            full_package_name = '%s.%s' % ("cogs", package_name)
            if full_package_name not in sys.modules:
                module = __import__("cogs."+package_name)
                module = getattr(module, package_name)
                module = getattr(module, package_name)
            self.add_cog(module(self))