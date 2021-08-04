import os
import sys
from dotenv import load_dotenv
import subprocess

from os.path import dirname, realpath

root = dirname(realpath(__file__))
load_dotenv()
if sys.argv[1] == "build":
    subprocess.run("hugo -D")
    subprocess.run(f".\\node_modules\\.bin\\atomic-algolia.cmd")
else:
    subprocess.run(f".\\node_modules\\.bin\\atomic-algolia.cmd")
    subprocess.run("hugo server -D")
