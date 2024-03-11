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

        if cmd_args[0] == 'exit':
            print('Exiting')
            return 1

        if cmd_args[0] == 'help':
            Interpreter.show_help(commands)
            return 0

        if cmd_args[0] == 'save':
            Interpreter.save()

        if len(cmd_args) == 5 and cmd_args[0] == 'host' and cmd_args[1] == 'add':
            hostname = cmd_args[2]
            op_sys = cmd_args[3]
            farm_name = cmd_args[4]
            os_options = [e.name for e in OperatingSystem]
            if op_sys not in os_options:
                print(f'No such OS "{op_sys}"')
                return 0

            result = manager.add_host_to_farm(farm_name, hostname, op_sys)



        elif len(cmd_args) == 3 and cmd_args[0] == 'host' and cmd_args[1] == 'remove':



            # hostname = cmd_args[2]
            # if farm.remove_host(hostname):
            #     print(f'Host {hostname} was removed')
            # else:
            #     print(f'Host  {hostname} not exist')

        elif len(cmd_args) == 3 and cmd_args[0] == 'farm' and cmd_args[1] == 'show':
            farm_name = cmd_args[2]
            manager.show_farm_hosts(farm_name)
        else:
            print(f'No such command "{cmd_args[0]}"')

        return 0
