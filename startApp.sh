#!/bin/sh
sudo pkill "python"
sudo python /flask-app/app.py &
exit 0
