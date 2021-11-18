from dotenv import load_dotenv
import subprocess
import click

from os.path import dirname, realpath

root = dirname(realpath(__file__))
load_dotenv()


@click.command()
@click.option('--watch/--no-watch', default=True)
@click.option('--build/--dev', default=False)
def run_hugo(watch: bool, build: bool):
    command = "hugo -D" if build else "hugo server -D"
    if not watch:
        command = f"{command} --watch=false"

    subprocess.run(command, shell=True)


if __name__ == '__main__':
    run_hugo()
