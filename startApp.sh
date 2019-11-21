#!/bin/sh
sudo pkill "python"
sudo nohup python /flask-app/app.py
exit 0
