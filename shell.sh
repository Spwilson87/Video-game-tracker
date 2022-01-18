#!/bin/bash

docker exec -i dbsql bash -l
mysql -u root -proot
use database_games
show tables;
describe Games;
...
...
EOF