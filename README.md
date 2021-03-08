# mcpy
A CLI Minecraft launcher written in Python.
### Installation
Just click the `Code` button on GitHub then press `Download ZIP`. Unzip it and open a command line in that folder. <br>
Bear in mind that that folder is where your Minecraft instances will be stored. (see **Where are my Instances?**) <br>
Alternatively, you can download the ZIPs from GitHub Releases.<br>
You'll then need to install the necessary dependencies, so run `pip install -r requirements.txt` in the command line of the folder.
### Making an Instance
Run `mc.py create <name> <version>` to create an instance. Example: <br>
```
mc.py create Hypixel 1.8.9
```
Note: the instance name must be unique!
### Launching an Instance
Run `mc.py launch <username> <password> <instance>` to launch the given instance. Example: <br>
```
mc.py launch example@example.com wordpass321 Hypixel
```
Note: `<username>` should be your Mojang e-mail, or your legacy username if you are still using one.
### Deleting an Instance
Run `mc.py delete <instance>` to delete the instance. You will be prompted to confirm the deletion. Example: <br>
```
mc.py delete Hypixel
```
### Where are my instances?
Your instances can be found in the `instances` folder wherever you ran this script. <br>
If you wish to move these, you must move the script along with it. <br>
You **cannot** use mcpy in your default Minecraft folder.

This code was written using [minecraft-launcher-lib](https://minecraft-launcher-lib.readthedocs.io), an easy-to-use library for authenticating against Yggdrasil and downloading and launching Minecraft JARs.
