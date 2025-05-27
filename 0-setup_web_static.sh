#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# create folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
<head>
 </head>
<body>
  Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server/a \\
\\n\\tlocation /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default

sudo service nginx restart

