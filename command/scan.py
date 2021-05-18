import socket
import struct

from command.command import Command
from msocket import MSocket


class Scan(Command):

    @staticmethod
    def ips(start, end):
        start = struct.unpack('>I', socket.inet_aton(start))[0]
        end = struct.unpack('>I', socket.inet_aton(end))[0]
        return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

    def execute(self, sock: MSocket, args: list[str]) -> str:
        """ Scans open ports of a ip address in a range. """
        for ip in Scan.ips(args[0], args[1]):
            print('Scanning IP', ip, '...')
            try:

                # will scan ports between 1 to 65,535
                for port in range(2, 65535):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.001)

                    # returns an error indicator
                    result = s.connect_ex((ip, port))
                    if result == 0:
                        print("Port {} is open".format(port))
                    s.close()

            except KeyboardInterrupt:
                print("\n Exiting scanner...")
            except socket.gaierror:
                print("\n Hostname {} Could Not Be Resolved.".format(ip))
            except socket.error:
                print("\n Server not responding.")
        return 'Finished scanning'

    def help(self) -> str:
        return 'Scans open ports of a ip address in a range.'