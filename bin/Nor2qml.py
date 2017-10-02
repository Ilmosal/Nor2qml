import os, sys

USR_PATH = os.getcwd()
MODULE_PATH = (os.path.realpath(__file__))[:-len("bin/run.py")]

os.chdir(MODULE_PATH)
sys.path = sys.path + [""]

import click

from nor2qml.core import nordic2quakeml

@click.command()
@click.argument('nordic', nargs=1)
def nor2qml(nordic):
	nordic2quakeml.nordic2QuakeML(USR_PATH, nordic)

if __name__ == "__main__":
	nor2qml()
