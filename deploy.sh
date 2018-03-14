#!/bin/bash

export FLASK_APP='run.py'
export FLASK_CONFIG='development'
python -m flask run
