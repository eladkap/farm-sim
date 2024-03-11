from farm import Farm
from host import Host


class Manager(object):
    def __init__(self):
        self.__hosts = []
        self.__farms = {}

    def get_farms(self):
        return self.__farms

    def add_farm(self, name: str) -> bool:
        if name in self.__farms.keys():
            print(f'Farm "{name}" already exists')
            return False
        farm = Farm(name)
        self.__farms[name] = farm
        return True

    def add_host_to_farm(self, farm_name, hostname: str, op_sys: str) -> bool:
        if farm_name not in self.__farms.keys():
            print(f'No such farm "{farm_name}"')
            return False

        farm = self.__farms[farm_name]

        host = Host(hostname, op_sys)
        if farm.add_host(host):
            print(f'Host {hostname} was added to farm {farm_name}')
            return True
        else:
            print(f'Host {hostname} already exists in farm {farm_name}')
            return False

    def show_farm(self, farm_name):
