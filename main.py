import json
import platform

from farm import Farm
from host import Host

# todo: do this when analyzing command inputs:
from interpreter import Interpreter
from manager import Manager
from operating_system import OperatingSystem

"""
Use command tree to walk over the tree like TRIE and detect the command args.
- Detect the first invalid arg and inform the user.
E.g: server addd -> "addd" arg is invalid

- Detect missing arg and inform user arg options.
E.g: server add hfa-test1d1 -> OS arg is missing (WINDOWS/LINUX)
E.g: server -> another arg is missing [show, add, delete]
"""


def load_commands_tree():
    commands_tree = {}
    with open('resources/commands_tree.json', 'r') as reader:
        commands_tree = json.load(reader)
    return commands_tree


def load_commands():
    commands = []
    with open('resources/commands.csv') as reader:
        lines = reader.readlines()
        titles = [word.strip(' \n') for word in lines[0].split(',')]
        for line in lines[1:]:
            attrs = [word.strip(' \n') for word in line.split(',')]
            command = {}
            for i, title in enumerate(titles):
                command[title] = attrs[i]
            commands.append(command)
    return commands


def run() -> int:
    manager = Manager()

    commands_tree = load_commands_tree()
    commands = load_commands()

    prompt = f'{platform.node()}> '
    while True:
        cmd_input = input(f'{prompt}')
        result = Interpreter.analyze_command(commands, commands_tree, manager, cmd_input)
        if result != 0:
            break

    return 0


def main():
    exitcode = run()
    print(f'return code: {exitcode}')


if __name__ == '__main__':
    main()
