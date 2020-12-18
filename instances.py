import json
import os
import argparse

parser = argparse.ArgumentParser(prog="PROG", description="Launch Minecraft: Java Edition from the command line.")

parser.add_argument('name', metavar='N', type=str, help="A unique name for the instance.")
parser.add_argument('version', metavar='V', type=str, help="The Minecraft version for the instance.")

args = parser.parse_args()
info = vars(args)

def create_instance(name, version):
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

create_instance(info['name'], info['version'])