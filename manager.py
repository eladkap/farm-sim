from farm import Farm
from host import Host
from operating_system import OperatingSystem


class Manager(object):
    def __init__(self):
        self.__hosts = []
        self.__farms = {}

    def get_farms(self):
        return self.__farms

    def create_farm(self, farm_name: str) -> bool:
        if farm_name in self.__farms.keys():
            print(f'Farm "{farm_name}" already exists.')
            return False
        farm = Farm(farm_name)
        self.__farms[farm_name] = farm
        print(f'Farm "{farm_name}" was created.')
        return True

    def add_host_to_farm(self, farm_name: str, hostname: str, op_sys: str) -> bool:
        if farm_name not in self.__farms.keys():
            print(f'No such farm "{farm_name}".')
            return False

        os_options = [e.name for e in OperatingSystem]
        if op_sys not in os_options:
            print(f'No such OS "{op_sys}"')
            return False

        farm = self.__farms[farm_name]

        host = Host(hostname, op_sys)
        if farm.add_host(host):
            print(f'Host "{hostname}" was added to farm "{farm_name}".')
            return True
        else:
            print(f'host "{hostname}" already exists.')
            return False

    def remove_host_from_farm(self, farm_name: str, hostname: str) -> bool:
        if farm_name not in self.__farms.keys():
            print(f'No such farm "{farm_name}"')
            return False

        farm = self.__farms[farm_name]

        if farm.has_host(hostname):
            farm.remove_host(hostname)
            print(f'Host "{hostname}" was removed from farm "{farm_name}".')
            return True
        else:
            print(f'Host "{hostname}" does not exist in farm "{farm_name}".')
            return False

    def show_farm(self, farm_name):
        if farm_name not in self.__farms.keys():
            print(f'No such farm "{farm_name}"')
            return

        print(f'Farm: {farm_name}')
        farm = self.__farms[farm_name]
        farm.show_hosts()

    def is_host_exists(self, hostname: str) -> bool:
        for farm_name in self.__farms.keys():
            farm = self.__farms[farm_name]
            if farm.has_host(hostname):
                return True
        return False

    def show_host(self, hostname: str):
        for farm_name in self.__farms.keys():
            farm = self.__farms[farm_name]
            if farm.has_host(hostname):
                host = farm.get_host(hostname)
                print(host)

    def to_dict(self) -> dict:
        farm_jsons = []
        for farm_name in self.__farms:
            farm = self.__farms[farm_name]
            farm_jsons.append(farm.to_dict())

        d = {
            "farms": farm_jsons
        }

        return d
