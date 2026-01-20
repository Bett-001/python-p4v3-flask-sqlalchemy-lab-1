#!/usr/bin/env python3
import subprocess
import sys
import os

# Change to the project directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run pytest with Python 3
result = subprocess.run([sys.executable, '-m', 'pytest', 'server/testing/', '-v'], 
                       capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print(result.stderr, file=sys.stderr)

sys.exit(result.returncode)