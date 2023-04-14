import nextcord
from nextcord.ext.commands import Bot

def get_status(status: str) -> nextcord.Status:
    statusmap = {
        "idle": nextcord.Status.idle,
        "online": nextcord.Status.online,
        "offline": nextcord.Status.offline,
        "dnd": nextcord.Status.dnd
    }
    try:
        return statusmap[status]
    except KeyError:
        raise Exception(f"invalid status, valid staus are {statusmap.keys()}")

async def set_status(bot: Bot, status: str) -> None:
    get_status(status)
    await bot.change_presence(status=status)

async def set_activity(bot: Bot, activity: str, name: str, url:str="https://www.youtube.com/watch?v=dQw4w9WgXcQ") -> None:
    activitymap = {
        "playing": nextcord.Game(name=name),
        "streaming": nextcord.Streaming(name=name, url=url),
        "listening": nextcord.Activity(type=nextcord.ActivityType.listening, name=name),
        "watching": nextcord.Activity(type=nextcord.ActivityType.watching, name=name)
    }
    try:
        activity = activitymap[activity]
    except KeyError:
        raise Exception(f"invalid activity, valid activities are {activitymap.keys()}")
    await bot.change_presence(activity=activity)

def check_guild(content):
    checklist = ["GUILDS=[]", "GUILDS=None", "GUILDS=0"]
    noscontent = content.replace(" ", "")
    for c in checklist:
        if c in noscontent:
            return True
    return False
