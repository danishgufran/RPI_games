# RPI_games
Setup Python on Raspberry Pi and evaluate its performance with a simple Terminal game.
# Setting up SSH on Raspberry Pi

## Prerequisites
- Raspberry Pi with operating system installed
- Ethernet cable or Wi-Fi adapter (for internet connectivity)
- Keyboard, mouse and monitor (for initial setup)
- Computer with terminal (for accessing Raspberry Pi remotely)

## Steps
1. Connect your Raspberry Pi to a network (either Ethernet or Wi-Fi) and power it on.
2. Login to the Raspberry Pi with the default credentials (username: pi, password: raspberry).
3. Open terminal on Raspberry Pi and update the package list: 
   ```sudo apt-get update```
4. Install SSH server on Raspberry Pi:
   ```sudo apt-get install openssh-server```
5. Confirm that SSH service is running:
   ```sudo systemctl status ssh```
6. Obtain the IP address of the Raspberry Pi:
   ```hostname -I```
7. Open terminal on your computer and SSH into the Raspberry Pi using the IP address:
   ```ssh pi@<ip_address>```
8. Enter the password (raspberry) to log in.

## Additional notes
- To access the Raspberry Pi remotely without a password, you can set up SSH keys.
- If you're connecting to the Raspberry Pi over the internet, you'll need to forward the SSH port (22) in your router's firewall settings.
- For increased security, it is recommended to change the default password and limit SSH access to specific IP addresses.

# Installing Python on Raspberry Pi

## Prerequisites
- Raspberry Pi with operating system installed
- Ethernet cable or Wi-Fi adapter (for internet connectivity)

## Steps
1. Open terminal on Raspberry Pi and update the package list: 
   ```sudo apt-get update```
2. Install Python 3:
   ```sudo apt-get install python3```
3. Verify the installation by checking the version of Python:
   ```python3 --version```

## Additional notes
- The Raspberry Pi OS comes with Python 2 pre-installed, but it is recommended to use Python 3 for development.
- To install additional packages, you can use the `pip3` package manager: 
  ```pip3 install <package_name>```
- To switch between Python 2 and Python 3, use the following commands:
  ```python2``` or ```python3```

# Creating a Directory and Downloading Code from github

## Prerequisites
- Raspberry Pi with operating system installed
- Ethernet cable or Wi-Fi adapter (for internet connectivity)

## Steps
1. Open terminal on Raspberry Pi.
2. Install Git: 
  ```sudo apt-get install git```
3. Clojne source code:
   ```git clone ```
4. Enter the directory:
   ```cd RPI_games```
5. Run the Python game using:
   ```python3 snake.py```


