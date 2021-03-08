import os
import shutil

import minecraft_launcher_lib
import subprocess
import argparse
import json

parser = argparse.ArgumentParser(prog="PROG", description="Launch Minecraft: Java Edition from the command line.")
subparsers = parser.add_subparsers(dest='subparser_name')

launch_parser = subparsers.add_parser('launch', help="Launches an instance.")
create_parser = subparsers.add_parser('create', help="Creates an instance.")
delete_parser = subparsers.add_parser('delete', help="Deletes an instance.")

launch_parser.add_argument('username', metavar='USER', type=str, help="Your Minecraft e-mail or legacy username.")
launch_parser.add_argument('password', metavar='PASSWORD', type=str, help="Your Minecraft password")
launch_parser.add_argument('instance', metavar='INSTANCE', type=str, help="The instance to launch.")

create_parser.add_argument('name', metavar='NAME', type=str, help="A unique name for the instance.")
create_parser.add_argument('version', metavar='VERSION', type=str, help="The Minecraft version for the instance.")

delete_parser.add_argument('name', metavar='NAME', type=str, help="The name of the instance to delete.")

args = parser.parse_args()
info = vars(args)



def launch(instance):

    directory = os.path.join("instances", instance, instance + ".json")

    if os.path.exists(directory):
        with open(directory) as jsonfile:
            instance_info = json.load(jsonfile)

        print("Logging in...")
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


# Progress Bar Code by JakobDev
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
# End of Progress Bar Code

def create_instance(name, version):
    max_value = [0]
    if not os.path.exists("instances"):
        os.mkdir("instances")
    if os.path.exists(os.path.join("instances", name)):
        print("This instance name is already in use!")
        exit()
    else:
        os.mkdir(os.path.join("instances", name))
        open(os.path.join("instances", name, name + ".json"))
        data = {
            "name": name,
            "version": version
        }
        with open(os.path.join("instances", name, name + ".json"), "w") as outfile:
            json.dump(data, outfile)

        callback = {
            "setProgress": lambda value: printProgressBar(value, max_value[0]),
            "setMax": lambda value: maximum(max_value, value)
        }

        print("Installing Minecraft...")
        minecraft_launcher_lib.install.install_minecraft_version(version,
                                                                 "instances/" + name + "/", callback=callback)

def delete_instance(name):
    response = input("Are you sure you would like to delete the instance: " + name + "? This will remove all your data for that instance. [y/n] ")
    if response == "y":
        directory = os.path.join("instances", name, name + ".json")
        if os.path.exists(directory):
            print("Deleting instance...")
            shutil.rmtree(os.path.join("instances", name))
            print("Instance deleted!")
        else:
            print("This instance is invalid or does not exist!")
    elif response == "n":
        print("Deletion cancelled. Aborting...")
        quit()
    else:
        print("Invalid confirmation response! Aborting...")


try:
    if info['subparser_name'] == 'create':
        create_instance(info['name'], info['version'])
    elif info['subparser_name'] == 'launch':
        launch(info['instance'])
    elif info['subparser_name'] == 'delete':
        delete_instance(info['name'])
    else:
        print("Please provide a valid subcommand!")
except KeyError:
    print("You must provide a subcommand!")







