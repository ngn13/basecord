from basecord.bot import Basecord
from nextcord.ext.commands import Cog as c
from nextcord import Interaction
from nextcord import slash_command

class Cog(c):
    def __init__(self, bc: Basecord) -> None:
        self.bc = bc
        self.db = bc.db
        self.config = bc.config
        self.init_guilds()

    def init_guilds(self):
        global GUILDS
        GUILDS = self.bc.config["guilds"]
