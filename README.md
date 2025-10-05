

Caplog.txt-cli is a simple python-based command line tool to manage your caplog.txt formatted log file.  

# Requirement 

Requires Python3 and libraries - os, sys, yaml, dateutil, datetime

# Config

Config file 'config.yml' must be provided in the same directory as the caplog.py python script. 

This has two important settings - format for the DATETIME and TIMESTAMP field. Here is an example config file. DATETIME field can either be a date or datetime depending on the period of time for each log entry. 

```shell
format:
   datetime_format: "%Y-%m-%d"
   timestamp_format: "%Y-%m-%dT%H:%M:%S"
```
# Usage

Pass the path of the log file as the argument in the command line.

```python
python3 caplog.py /home/user/caplog.txt
```

A new file file is created if it does not exist. If the given file already exists, the file is validated and parsed into a dict object. A new entry is received from the user interactively in the command line and is written into the log file. 

```
Enter the entry date (Press enter to accept the default 2022-09-18) :
Enter the entry message (empty line to exit) :Hello World!
This is my first log entry.
I am going to maintain my logs in caplog.txt format
```



# License

Refer LICENSE file for license information. 
