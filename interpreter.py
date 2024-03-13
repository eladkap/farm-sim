from farm import Farm
from host import Host
from manager import Manager
from operating_system import OperatingSystem


class Interpreter:
    @staticmethod
    def show_help(commands: list):
        titles = list(commands[0].keys())
        print('\t\t\t\t\t\t'.join(titles))
        for command in commands:
            print('\t\t\t\t\t\t'.join(command.values()))

    @staticmethod
    def save():
        pass

    @staticmethod
    def analyze_command(commands: list, commands_tree: dict, manager: Manager, cmd_args: str) -> int:
        cmd_args = cmd_args.split()

        if len(cmd_args) == 0:
            return 0

        elif cmd_args[0] == 'exit':
            print('Exiting')
            return 1

        elif cmd_args[0] == 'help':
            Interpreter.show_help(commands)
            return 0

        elif cmd_args[0] == 'save':
            Interpreter.save()

        elif len(cmd_args) == 3 and cmd_args[0] == 'farm' and cmd_args[1] == 'create':
            farm_name = cmd_args[2]
            if manager.create_farm(farm_name):
                print(f'Farm {farm_name} was created.')
            else:
                print(f'Farm {farm_name} already exists')

        elif len(cmd_args) == 3 and cmd_args[0] == 'farm' and cmd_args[1] == 'show':
            farm_name = cmd_args[2]
            manager.show_farm(farm_name)

        elif len(cmd_args) == 5 and cmd_args[0] == 'host' and cmd_args[1] == 'create':
            farm_name = cmd_args[2]
            hostname = cmd_args[3]
            op_sys = cmd_args[4]
            if manager.add_host_to_farm(farm_name, hostname, op_sys):
                print(f'Host {hostname} was added to farm {farm_name}.')
            else:
                print(f'Farm {farm_name} already exists.')

        elif len(cmd_args) == 3 and cmd_args[0] == 'host' and cmd_args[1] == 'show':
            hostname = cmd_args[2]
            if not manager.is_host_exists(hostname):
                print(f'No such host {hostname}.')
            else:
                manager.show_host(hostname)

        else:
            print(f'No such command "{cmd_args[0]}"')

        return 0
