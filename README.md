# collaborative_editor_quill

This repository contains a django project that embodies a collaborative quilljs editor.

Steps to run the project:
1. Creation of virtualenv
```
virtualenv venv -p  python3
pip3 install django==1.11.7
```

2.Installing and initialising mongodb
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```

3. Initialising the node server
```
npm start
```

4.Initialising the django server
```
python manage.py runserver 4000
```
