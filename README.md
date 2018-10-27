# Activity Tracker

## How it Works
1. Run program with `bash run.sh`
2. Input username 
3. Input password (output is suppressed)
4. Choose units for length of time
5. Choose magnitude for length of time

All output is suppressed and redirected to a file `nohup.out` to prevent ssh shutdown.

Collects Data every 5 minutes. The data is appended to a csv file that is created upon initial 
run in the `Logs` directory. 

## API and Other Resources
- `life360API.py`
 - `life360.py` from https://github.com/harperreed/life360-python
