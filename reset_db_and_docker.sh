#! /bin/bash

sudo docker stop $(sudo docker ps -a -q)
echo y | sudo docker system prune --all
sudo rm -rf mysql/