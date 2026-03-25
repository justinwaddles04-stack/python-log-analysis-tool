## Python Log Analysis Tool

## Overview
This project is a Python-based log analysis tool designed to detect suspicious authentication activity and identify potential security risks from login data.

## Objective
The goal of this project is to analyze authentication logs and identify abnormal patterns such as repeated failed login attempts and potential brute-force or unauthorized access activity.

## Tools Used
- Python

## Project Contents
- `log_analysis.py` – log analysis script
- `log-analysis-output.png` – example output

## Key Features
- Parses authentication logs to extract timestamps, usernames, and login outcomes
- Aggregates failed login attempts by user account
- Identifies top suspicious accounts based on repeated login failures
- Generates alerts for potential brute-force or suspicious login activity
- Calculates total failed login attempts for overall visibility

## Methodology
Log entries are processed using Python to identify failed login events. The script aggregates failures by username, ranks accounts based on failed attempts, and applies thresholds to flag suspicious activity.

## Example Output

Authentication Log Analysis Report
========================================

Failed Login Summary:
mbrown: 3 failed login attempts
jsmith: 3 failed login attempts

Total Failed Login Attempts: 6

Top Suspicious Accounts:
mbrown: 3 failed login attempts
jsmith: 3 failed login attempts

Suspicious Activity Alerts:
ALERT: mbrown has 3 failed login attempts
ALERT: jsmith has 3 failed login attempts


## Outcome
This project demonstrates the ability to analyze authentication logs, detect suspicious patterns, and generate actionable security insights using Python. It reflects foundational skills in security monitoring and threat detection aligned with security analyst and GRC workflows.
