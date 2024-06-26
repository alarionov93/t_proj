#!/bin/zsh

init_db=$1

# web service
export FLASK_APP='app'
export FLASK_DEBUG=1

[[ $1 == "--init-db" ]] && export INIT_FLASK_DB_USER=1

flask run --host '0.0.0.0' --port 5000 --no-debug 
