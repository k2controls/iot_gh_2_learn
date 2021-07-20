#!/bin/bash
echo "Starting greenhouse services..."
sudo pigpiod
python3 gh_startup.py
