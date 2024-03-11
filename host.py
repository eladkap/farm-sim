from status import Status

"""
hostname - host name
op_sys - operating system (Windows/Linux)
fs - file system
"""


class Host(object):
    def __init__(self, hostname: str, op_sys: str):
        self.__hostname = hostname
        self.__op_sys = op_sys
        self.__status = Status.UP
        self.__cpu_usage = 0
        self.__memory_usage = 0
        self.__fs = {}

    def to_dict(self):
        d = {
            'hostname': self.__hostname,
            'OS': self.__op_sys,
            'Status': self.__status
        }
        return d

    def __str__(self):
        return str(self.to_dict())

    def get_hostname(self):
        return self.__hostname

    def get_os(self):
        return self.__op_sys

    def get_status(self):
        return self.__status

    def get_cpu_usage(self):
        return self.__cpu_usage

    def get_memory_usage(self):
        return self.__memory_usage

    def set_status(self, status: str):
        self.__status = status

    def set_cpu_usage(self, cpu_usage: int):
        self.__cpu_usage = cpu_usage

    def set_memory_usage(self, memory_usage: int):
        self.__memory_usage = memory_usage
