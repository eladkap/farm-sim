import time
import random

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
        self.__status = Status.UP.name
        self.__cpu_usage = 0
        self.__memory_usage = 0
        self.__fs = {}

    def to_dict(self):
        d = {
            'hostname': self.__hostname,
            'OS': self.__op_sys,
            'status': self.__status
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

    def run(self):
        timestamp = 0
        while True:
            time.sleep(3)

            # Set random status
            if timestamp % 20 == 0:
                x = random.randint(0, 100)
                status = Status.UP.name if x > 5 else Status.DOWN.name
                self.set_status(status)

            # Set random CPU usage
            if timestamp % 5 == 0:
                cpu = random.randint(0, 100)
                self.set_cpu_usage(cpu)

            # Set random memory usage
            if timestamp % 4 == 0:
                memory = random.randint(0, 100)
                self.set_memory_usage(memory)

            timestamp += 1
