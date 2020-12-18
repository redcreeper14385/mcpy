# mcpy
A CLI Minecraft launcher written in Python.
### Installation
Just click the `Code` button on GitHub then press `Download ZIP`. Unzip it and open a command line in that folder. <br>
Alternatively, you can download the ZIPs from GitHub Releases.
### Making an Instance
Run `instances.py <name> <version>` to create an instance. Example: <br>
```
instances.py Hypixel 1.8.9
```
Note: the instance name must be unique!
### Launching an Instance
Run `launch.py <username> <password> <instance>` to launch the given instance. Example: <br>
```
launch.py example@example.com wordpass321 Hypixel
```
Note: `<username>` should be your Mojang e-mail, or your legacy username if you are still using one.
### Where are my instances?
Your instances can be found in the `instances` folder wherever you ran this script.

This code was written using [minecraft-launcher-lib](https://minecraft-launcher-lib.readthedocs.io), an easy-to-use library for authenticating against Yggdrasil and downloading and launching Minecraft JARs.
