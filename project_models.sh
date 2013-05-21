#!/bin/sh
python ./manage.py project_models 2> "$(date +"%d_%m_%Y")_models.dat" 