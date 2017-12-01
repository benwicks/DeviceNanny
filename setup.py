#!/usr/bin/env python
# Install Device Nanny

import subprocess

# TODO check preconditions (e.g. internet connection, pre-existing installations) first

print("Step 1: Download and install system updates\n")
bashCommand = "sudo apt-get update && sudo apt-get upgrade -y"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 2: Automatically configure system for Device Nanny\n")
bashCommand = "find /etc/lightdm/lightdm.conf -type f -exec sed -i " \
              "\"s/#xserver-command=X/xserver-command=X/g\" {} \;"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "find ~/.config/pcmanfm/LXDE-pi/pcmanfm.conf -type f -exec sed -i " \
              "\"s/mount_on_startup=1/mount_on_startup=0/g\" {} \;"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "find ~/.config/pcmanfm/LXDE-pi/pcmanfm.conf -type f -exec sed -i " \
              "\"s/mount_removable=1/mount_removable=0/g\" {} \;"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "find ~/.config/pcmanfm/LXDE-pi/pcmanfm.conf -type f -exec sed -i " \
              "\"s/autorun=1/autorun=0/g\" {} \;"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 3: Install MySQL server\n")
bashCommand = "sudo apt-get install mysql-server -y"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 4: Install PyMySQL\n")
bashCommand = "sudo pip3 install PyMySQL"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 5: Install Apache2\n")
bashCommand = "sudo apt-get install apache2 php5 libapache2-mod-php5 -y"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 6: Install PHPMyAdmin\n")
print("\t- Select Apache2 as the server to use\n"
      "\t- Select Yes to configure database to PHPMyAdmin\n"
      "\t- Enter the root password entered for MySQL\n"
      "\t- Enter a password for PHPMyAdmin\n")
# todo can I split this step up at all?
bashCommand = "sudo apt-get install phpmyadmin -y"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 7: Automatically Configure Apache and PHPMyAdmin\n")
bashCommand = "echo \"Include /etc/phpmyadmin/apache.conf\" | sudo tee -a /etc/apache2/apache2.conf"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "sudo /etc/init.d/apache2 restart"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 8: Create database and web user at http://localhost/phpmyadmin\n")
print("\t- Create a new database called `DeviceNanny`\n"
      "\t- Create a new user for web front end with read only privileges\n"
      "\t\t- Go to the Privileges tab\n"
      "\t\t- Click Add User\n"
      "\t\t- Create a new user with at least `Select` and `Update` privileges under Data\n")
bashCommand = "x-www-browser http://localhost/phpmyadmin"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("Step 9: Download & Configure DeviceNanny\n")
bashCommand = "cd; git clone https://github.com/hudl/DeviceNanny"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "sudo pip3 install -r ~/DeviceNanny/requirements.txt"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "cp config/DeviceNanny.ini.template config/DeviceNanny.ini"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# TODO add DB password, Slack API key, and Slack device room ID to ini file
