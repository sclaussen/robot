# Materials

- [$44.90 Robotis Dynamixel AX-12 Robot Actuator](https://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx)
- [$49.90 Robotis Dynamixel U2D2](https://www.trossenrobotics.com/dynamixel-u2d2.aspx)
- [$ 7.95 Robotis 6 Port AX/MX Power Hub](https://www.trossenrobotics.com/6-port-ax-mx-power-hub)
- [$19.95 Power Supply 12V - 5A (2.1mm Jack)](https://www.trossenrobotics.com/p/power-supply-12vdc-5a.aspx)
- [$24.95 Robotis PhantonX Parallel AX-12 Gripper](https://www.trossenrobotics.com/p/phantomx-parallel-ax12-gripper.aspx)



# Configuration

- Configure the U2D2
  - https://emanual.robotis.com/docs/en/parts/interface/u2d2

- Dynamix SDK
  - cd ~/src
  - git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
  - cd ~/src/DynamixelSDK/python
  - python3 setup.py install

- Run Tests
  - cd ~/src/DynamixelSDK/python/tests/protocol1_0
  - ls /dev/tty.usbserial*
  - Edit ping.py
    - Change DEVICENAME to proper TTY
    - Changed BAUDRATE to 1000000
  - Edit read_write.py
    - Change DEVICENAME to proper TTY
    - Changed BAUDRATE to 1000000



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
