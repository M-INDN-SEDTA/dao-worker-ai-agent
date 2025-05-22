#!/bin/bash
# Simple script to run Flask backend

export FLASK_APP=backend/app.py
export FLASK_ENV=development

flask run
