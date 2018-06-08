# collaborative_editor_quill

This repository contains a django project that embodies a collaborative quilljs editor.

Steps to run the project:
1. Install dependencies
```
git clone https://github.com/aadarshsingh191198/collaborative_editor_quill.git
virtualenv collabquill -p python3
source collabquill/bin/activate
cd collaborative_editor_quill
pip install -r requirements.txt
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
npm run build && npm start
```

4.Initialising the django server
```
python manage.py runserver 0.0.0.0:4000
```
