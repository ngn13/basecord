from setuptools import setup, find_packages

VERSION = "0.0.1" 
DESCRIPTION = "Nextcord based discord bot framework"

setup(
        name="basecord", 
        version=VERSION,
        author="ngn13",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["nextcord", "colorama"], 
        entry_points={"console_scripts": ["basecord=basecord.build:main"]}
)