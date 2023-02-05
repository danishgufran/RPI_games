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
