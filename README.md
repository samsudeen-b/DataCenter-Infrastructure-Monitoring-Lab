# Data Center Infrastructure Monitoring & Diagnostics Lab

A Python-based infrastructure monitoring and diagnostics lab designed to simulate fundamental data center operational monitoring workflows.

## Overview

This project monitors system resource utilization, evaluates infrastructure health, detects abnormal conditions, and maintains operational logs for troubleshooting and incident analysis.

The project was developed as a hands-on lab to strengthen practical knowledge of infrastructure monitoring, system diagnostics, incident detection, and data center operational concepts.

## Features

- CPU utilization monitoring
- Memory utilization monitoring
- Disk utilization monitoring
- Network traffic statistics
- Host identification
- Timestamped health checks
- Threshold-based incident detection
- Monitoring history logging
- Incident logging
- HEALTHY / CRITICAL status classification

## Technologies

- Python
- psutil
- socket
- datetime
- Windows system monitoring

## Project Structure

DataCenter-Monitoring-Lab/
├── monitor.py
├── monitoring.log
├── incidents.log
├── requirements.txt
├── .gitignore
└── README.md

## How It Works

1. Collects CPU, memory, disk, and network statistics.
2. Identifies the monitored host.
3. Compares resource utilization against defined thresholds.
4. Classifies resources as HEALTHY or CRITICAL.
5. Records monitoring results in `monitoring.log`.
6. Records detected incidents in `incidents.log`.

## Incident Simulation

The incident-detection workflow was validated by temporarily lowering the CPU alert threshold in a controlled test environment.

After successful validation, the production threshold was restored to 90%.

This allowed the incident logging workflow to be tested without intentionally stressing the system.

## Run the Project

Install the dependency:

```bash
pip install -r requirements.txt