# Overview

Our development environment consisted of:
- MacOS
- Python 3.x
- Dynamixel AX12-A Actuators
- The U2D2, AX/MS Power Hub, and 12V/5Amp Power Supply to connect the MacOS to the AX12-A for testing
- Raspberry Pi



# Materials

- [Robotis Dynamixel AX-12 Robot Actuator ($44.90)](https://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx)
- [Robotis Dynamixel U2D2 ($49.90)](https://www.trossenrobotics.com/dynamixel-u2d2.aspx)
- [Robotis 6 Port AX/MX Power Hub ($7.95)](https://www.trossenrobotics.com/6-port-ax-mx-power-hub)
- [Power Supply 12V - 5A (2.1mm Jack) ($19.95)](https://www.trossenrobotics.com/p/power-supply-12vdc-5a.aspx)
- [Robotis PhantonX Parallel AX-12 Gripper ($24.95)](https://www.trossenrobotics.com/p/phantomx-parallel-ax12-gripper.aspx)



# MacOS Setup

- Configure the U2D2
  - https://emanual.robotis.com/docs/en/parts/interface/u2d2
  - After installation determine the USB serial tty device that
    represents the U2D2 using `ls /dev/tty.usbserial*`

- Install the Dynamixel SDK
```
cd ~/src
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
cd src/python
python3 setup.py install
```

- Run the Dynamixel SDK Python Tests
```
cd ~/src/DynamixelSDK/python/tests/protocol1_0
```
  - Run ping.py to verify successful setup and communication with the AX-12A
    - Change DEVICENAME to proper TTY (on MacOS, /dev/tty.usbserial*)
    - Change BAUDRATE to 1000000
  - Run read_write.py to verify successful manipulation of the AX-12A
    - See the [AX-12a control table](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/#control-table-data-address) to update the following constants:
      - Change ADDR_MX_TORQUE_ENABLE to 24
      - Change ADDR_MX_GOAL_POSITION to 116
      - Change ADDR_MX_PRESENT_POSITION to 132
    - Change DEVICENAME to proper TTY
    - Change BAUDRATE to 1000000



# Raspberry Pi

- Update Packages
  - `sudo apt-get update -y`
  - `sudo apt-get upgrade -y`
  - `sudo apt dist-upgrade -y`

- Remote Desktop Sharing
  - Enable VNC
    - `sudo raspi-config`
      - Select Interfacing Options
      - Select VNC
      - For the prompt to enable VNC, select Yes (Y)
      - For the confirmation, select Ok    - Changed the password for the pi user
  - Determined the IP address of the Pi
    - `hostname -I`
  - Spotlight search for "Screen Sharing" on the Mac
    - Start the app
    - Connect to the Pi using its IP address

- Configure Github
  - Generate a public/private key pair
    - `ssh-keygen`
  - Add the key to the github account
  - `git config --global user.email "caden.claussen@gmail.com"`
  - `git config --global user.name "Caden Claussen"`

- Configure Secure Shell (ssh)
  - `sudo systemctl enable ssh`
  - `sudo systemctl start ssh`
  - On mac copy public key to the Pi
    - `cat ~/.ssh/id_rsa.pub | ssh pi@10.0.0.66 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'`
  - Created .zshrc pi function
    - `pi() { ssh pi@10.0.0.66 "$@" }`

- Install Emacs
  - `sudo apt install emacs`
  - Copy .emacs.d directory to ~/.emacs.d

- Configure Zsh
  - `sudo apt-get install zsh`
  - `chsh -s zshrc`
  - Copy .zshrc file to ~/.zshrc

- Install Nginx
  - `sudo apt install nginx`
  - `sudo /etc/init.d/nginx start`
  - /var/www/html
  - `sudo systemctl restart nginx`

- Software configuration on Raspberry Pi
  - sudo apt-get -y install python-dev python3-rpi.gpio



# Issues

- There is no status packet!

```
$ p3 ping.py
Succeeded to open the port
Succeeded to change the baudrate
Unsuccessful: [TxRxResult] There is no status packet!
```

To resolve I set the BAUDRATE to 1000000 per this [github issue](https://github.com/ROBOTIS-GIT/DynamixelSDK/issues/246).
