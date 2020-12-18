import os

import minecraft_launcher_lib
import subprocess
import argparse
import json

parser = argparse.ArgumentParser(prog="PROG", description="Launch Minecraft: Java Edition from the command line.")

parser.add_argument('username', metavar='U', type=str, help="Your Minecraft e-mail or legacy username.")
parser.add_argument('password', metavar='P', type=str, help="Your Minecraft password")
parser.add_argument('instance', metavar='I', type=str, help="The instance to launch.")

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

def launch(instance):
    max_value = [0]

    callback = {
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
    }

    directory = "instances/" + instance + "/" + instance + ".json"

    if os.path.exists(directory):
        with open(directory) as jsonfile:
            instance_info = json.load(jsonfile)

        print("Installing Minecraft...")
        minecraft_launcher_lib.install.install_minecraft_version(instance_info['version'], "instances/" + instance + "/", callback=callback)
        print("Install complete, logging in...")
        login_info = minecraft_launcher_lib.account.login_user(info['username'], info['password'])

        try:
            options = {
                "username": login_info["selectedProfile"]["name"],
                "uuid": login_info["selectedProfile"]["id"],
                "token": login_info["accessToken"]
            }

            print("Authentication successful! Launching Minecraft...")

            try:
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(instance_info['version'], "instances/" + instance + "/",
                                                                                         options)
                subprocess.call(minecraft_command)
            except FileNotFoundError:
                print("Launch failed! Check the version name.")

        except KeyError:
            print("Authentication Failed! Check your credentials, or Yggdrasil may be down.")
    else:
        print("That instance does not exist!")

launch(info['instance'])








