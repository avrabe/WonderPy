import ctypes
import json
import os
import platform

from morseapi import MorseRobot

from WonderPy.components.wwMedia import WWMedia
from WonderPy.config import WW_ROOT_DIR


class two_packet_wrappers():
    def __init__(self):
        self.packet1_bytes_num = 0
        self.packet1_bytes = None
        self.packet2_bytes_num = 0
        self.packet2_bytes = None


def loadHAL():
    if _get_platform() == "darwin":
        return _load_HAL_Darwin()
    else:
        return HAL()


def _get_platform():
    uname = platform.uname()[0]
    return str(uname).lower()


def _load_HAL_Darwin(self):
    HAL_path = os.path.join(WW_ROOT_DIR, 'lib/WonderWorkshop/osx/libWWHAL.dylib')
    libHAL = ctypes.cdll.LoadLibrary(HAL_path)
    libHAL.packets2Json.restype = ctypes.c_char_p
    return libHAL
    # self.libHAL.json2Packets.argtypes = (c_char_p, WWBTLEManager.two_packet_wrappers)


class HAL():
    def packets2Json(self, pw):
        ## print(pw.packet1_bytes_num, pw.packet2_bytes_num)

        # ('packet1_bytes_num', ctypes.c_byte),
        # ('packet1_bytes', ctypes.c_byte * 20),
        # ('packet2_bytes_num', ctypes.c_byte),
        # ('packet2_bytes', ctypes.c_byte * 20),
        return "{}"

    def json2Packets(self, json_str, packets):
        '''
        Ignore for now 
        :param json_str:
        :param packets:
        :return:
        '''
        pass

    def json2Packets1(self, json_str):
        print(json_str)
        commands = json.loads(json_str)
        converse = {
            WWMedia.WWSound.WWSoundDot.HOWDY: "hi",
            WWMedia.WWSound.WWSoundDot.HOLD_ME: "ayayay",
            WWMedia.WWSound.WWSoundDot.READYSET: "brrp",
            WWMedia.WWSound.WWSoundDash.HOWSGOING: "elephant",
            WWMedia.WWSound.WWSoundDash.LETS_GO: "confused2"
        }
        packets = two_packet_wrappers()
        print("two")
        if '300' in commands:
            robot = MorseRobot()
            packets.packet2_bytes_num = 0
            packets.packet1_bytes_num = 20
            myfile = converse[commands['300']['file']]
            byte_array = robot.say(myfile)
            packets.packet1_bytes = byte_array
            print("say", myfile, byte_array)
        if '205' in commands:
            robot = MorseRobot()
            packets.packet2_bytes_num = 0
            packets.packet1_bytes_num = 20
            degree = commands['205']['degree']
            byte_array = robot.turn(degree)
            packets.packet1_bytes = byte_array
            print("turn", degree, byte_array)
        return packets
