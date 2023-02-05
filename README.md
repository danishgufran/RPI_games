# RPI_games
Setup Python on Raspberry Pi and evaluate its performance with a simple Terminal game.

Setting up SSH on Raspberry Pi
Prerequisites
Raspberry Pi with operating system installed
Ethernet cable or Wi-Fi adapter (for internet connectivity)
Keyboard, mouse and monitor (for initial setup)
Computer with terminal (for accessing Raspberry Pi remotely)
Steps
Connect your Raspberry Pi to a network (either Ethernet or Wi-Fi) and power it on.
Login to the Raspberry Pi with the default credentials (username: pi, password: raspberry).
Open terminal on Raspberry Pi and update the package list:
sudo apt-get update
Install SSH server on Raspberry Pi:
sudo apt-get install openssh-server
Confirm that SSH service is running:
sudo systemctl status ssh
Obtain the IP address of the Raspberry Pi:
hostname -I
Open terminal on your computer and SSH into the Raspberry Pi using the IP address:
ssh pi@<ip_address>
Enter the password (raspberry) to log in.
