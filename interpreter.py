import json

from manager import Manager


class Interpreter:
    @staticmethod
    def show_help(commands: list):
        titles = list(commands[0].keys())
        print('\t\t\t\t\t\t'.join(titles))
        for command in commands:
            print('\t\t\t\t\t\t'.join(command.values()))

    @staticmethod
    def save(manager: Manager, file_path: str):
        if len(manager.get_farms()) == 0:
            print('Nothing to save.')
            return
        with open(file_path, 'w') as fp:
            json.dump(manager.to_dict(), fp, indent=2)
        print(f'Farms data was saved to file {file_path}.')

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
            if len(cmd_args) == 1:
                print('Usage: save FILE-PATH')
                return 0
            if len(cmd_args) == 2:
                file_path = cmd_args[1]
                Interpreter.save(manager, file_path)

        elif len(cmd_args) == 3 and cmd_args[0] == 'farm' and cmd_args[1] == 'create':
            farm_name = cmd_args[2]
            manager.create_farm(farm_name)


        elif len(cmd_args) == 3 and cmd_args[0] == 'farm' and cmd_args[1] == 'show':
            farm_name = cmd_args[2]
            manager.show_farm(farm_name)

        elif len(cmd_args) == 5 and cmd_args[0] == 'host' and cmd_args[1] == 'create':
            farm_name = cmd_args[2]
            hostname = cmd_args[3]
            op_sys = cmd_args[4]
            manager.add_host_to_farm(farm_name, hostname, op_sys)

        elif len(cmd_args) == 3 and cmd_args[0] == 'host' and cmd_args[1] == 'show':
            hostname = cmd_args[2]
            if not manager.is_host_exists(hostname):
                print(f'No such host "{hostname}".')
            else:
                manager.show_host(hostname)

        elif len(cmd_args) == 5 and cmd_args[0] == 'host' and cmd_args[1] == 'remove':
            farm_name = cmd_args[2]
            hostname = cmd_args[3]
            manager.remove_host_from_farm(farm_name, hostname)

        else:
            print(f'No such command "{cmd_args[0]}"')

        return 0
