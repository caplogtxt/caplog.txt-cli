

Caplog.txt-cli is a simple python-based command line tool to manage your caplog.txt formatted log file.  

# Requirement 

Requires Python3 and libraries - os, sys, pyyaml, python-dateutil, datetime

# Config

config.yml is used to specify the following settings.

```shell
DATE_FORMAT: "%Y-%m-%d"
TIMESTAMP_FORMAT: "%Y-%m-%dT%H:%M:%S"
```
For file-specific configuration,  the config file is placed in the same directory as the log file. 
For system-wide configuration, the config file is placed in the same directory as the python script.

In the absence of config.yml in any level, the default values are used.

# Usage

Pass the path of the log file as the argument in the command line.

```python
python3 caplog.py /home/user/caplog.txt
```

A new log file is created if it does not already exist. If the log file already exists, it is validated for any syntax errors and loaded into memory. A new entry is received from the user interactively in the command line and is written into the log file. 

```
Enter the entry date (Press enter to accept the default 2022-09-18) :
Enter the entry message (empty line to exit) :Hello World!
This is my first log entry.
I am going to maintain my logs in caplog.txt format
```



# License

Refer LICENSE file for license information. 
