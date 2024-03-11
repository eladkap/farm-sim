from host import Host


class Farm(object):
    def __init__(self, name):
        self.__name = name
        self.__hosts = {}

    def __len__(self):
        return len(self.__hosts.keys())

    def get_name(self):
        return self.__name

    def get_hosts(self):
        return self.__hosts

    def add_host(self, host: Host) -> bool:
        if host.get_hostname() in self.__hosts.keys():
            return False
        self.__hosts[host.get_hostname()] = host
        return True

    def remove_host(self, hostname: str) -> bool:
        if hostname not in self.__hosts.keys():
            return False
        self.__hosts.pop(hostname)
        return True

    def show_hosts(self):
        for host in self.__hosts:
            print(host)
