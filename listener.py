#!/usr/bin/python3
import serial
import time
import threading
from pynput.keyboard import Key, Controller

keyboard = Controller()


def run_launchpad():
    with keyboard.pressed(
            Key.cmd,
            Key.esc):
        pass


def run_showdesktop():
    with keyboard.pressed(
            Key.cmd,
            'd'):
        pass


class MSerialPort:
    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self, data):
        number = self.port.write(data)
        return number

    def parse_data(self, data):
        if 'DOWN' in data:
            print('Down')
            run_launchpad()
        elif 'UP' in data:
            print('Up')
            run_showdesktop()
        elif 'LEFT' in data:
            print('Left')
            # ...
        elif 'RIGHT' in data:
            print('Right')
            # ...
        else:
            pass

    def read_data(self):
        while True:
            data = str(self.port.readline())
            self.parse_data(data)
            time.sleep(0.1)

    def run(self):
        threading.Thread(target=self.read_data).start()


if __name__ == '__main__':
    mSerial = MSerialPort('/dev/tty.usbmodem144301', 9600)
    mSerial.run()
