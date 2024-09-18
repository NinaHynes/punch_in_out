The Punchcard System is a simple time-tracking application built using BeeWare's Toga framework. 
It allows users to check in and check out while logging the current day, time, and a user-defined "plan" (action). 
This app is designed to be extended for personal or organizational use to track work hours or activities.

Features
Check In: Users can log their check-in time, date, and the day of the week.
Check Out: Logs the check-out time and the corresponding information.
Plan: Users can input a custom plan (action) for their check-in, making it more flexible for tracking different activities.
Logs: All check-in and check-out activities are logged in a text file.

Installation
Requirements
Python 3.7+
Toga: A Python native, OS-native GUI toolkit.
BeeWare Briefcase (for development and packaging)

The app currently logs information to a text file. Future versions may support database integration for better data management.
Example log:
Checked in on Monday at 09:00:00 with plan: Start Work (2024-09-18)
Checked out on Monday at 17:00:00 with plan: End Work (2024-09-18)

Run locally:
python run.py

Running in Development Mode
Install the development dependencies:

Running in development mode:
Install developmental dependencies:
pip install briefcase toga

Use briefcase dev to run the app in development mode:
briefcase dev

Building the app:
briefcase build

If you'd like to package the app using Briefcase, run:
briefcase build
