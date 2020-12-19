import json
import os
import argparse

import minecraft_launcher_lib

parser = argparse.ArgumentParser(prog="PROG", description="Launch Minecraft: Java Edition from the command line.")

parser.add_argument('name', metavar='N', type=str, help="A unique name for the instance.")
parser.add_argument('version', metavar='V', type=str, help="The Minecraft version for the instance.")

args = parser.parse_args()
info = vars(args)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def maximum(max_value,value):
    max_value[0] = value


def create_instance(name, version):
    max_value = [0]
    if not os.path.exists("instances"):
        os.mkdir("instances")
    if os.path.exists("instances/" + name):
        print("This instance name is already in use!")
        exit()
    else:
        os.mkdir("instances/" + name)
        open("instances/" + name + "/" + name + ".json", "x")
        data = {
            "name": name,
            "version": version
        }
        with open("instances/" + name + "/" + name + ".json", "w") as outfile:
            json.dump(data, outfile)

        callback = {
            "setProgress": lambda value: printProgressBar(value, max_value[0]),
            "setMax": lambda value: maximum(max_value, value)
        }

        print("Installing Minecraft...")
        minecraft_launcher_lib.install.install_minecraft_version(version,
                                                                 "instances/" + name + "/", callback=callback)
create_instance(info['name'], info['version'])