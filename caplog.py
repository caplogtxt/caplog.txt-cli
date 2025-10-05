#!/usr/bin/python3
import os
import sys
import datetime
from dateutil import parser
import yaml

try:
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
except Exception as e:
    print("Config file not found or improper. Hit error "+str(e))
    sys.exit(1)


DATETIME_FORMAT=cfg['format']['datetime_format']
TIMESTAMP_FORMAT=cfg['format']['timestamp_format']

def validate_log(log):
    """
    Validates a log file and return True if there is no error in the format
    Otherwise raises an exception with the error message and returns False
    """
    try:
        if not os.path.exists(log):
            raise Exception("File error: log file not found") 
        with open(log,'r') as f:
            contents=f.readlines() 
        preceding_blank=True
        preceding_date=False
        for line in contents:
            if line == '\n': 
                preceding_blank = True
                preceding_timestamp = False
                continue
            if preceding_blank == True: # expect a Date
                preceding_blank = False
                preceding_date = True
                parser.parse(line.strip())
                continue
            if preceding_date == True: #except a timestamp
                preceding_date = False
                preceding_timestamp = True
                parser.parse(line.strip()) 
                continue
            if preceding_timestamp == True: #except a message
                continue
    except Exception as e:
        print(str(e))
        return False
    return True

def read_log(log):
    """
    Parse a validated log file and return a dictionary of logs
    """
    with open(log,'r') as f:
        contents=f.readlines()
    log_dict={} 
    preceding_blank=True
    
    for line in contents:
        if line == '\n':
            # encountered a blank line
            preceding_blank=True
            preceding_timestamp=False
        elif preceding_blank==True:
            # encountered a date
            preceding_blank=False
            date=parser.parse(line.strip('\n'))
            date=date.strftime(DATETIME_FORMAT)
            log_dict.setdefault(date,[])
            preceding_date=True
        elif preceding_date==True:
            # encountered an entry timestamp
            preceding_date=False
            timestamp=parser.parse(line.strip('\n'))
            timestamp=timestamp.strftime(TIMESTAMP_FORMAT)
            #Update the timestamp
            if log_dict[date] == []:
                log_dict[date]=[timestamp,'']
            else:
                new_timestamp=datetime.datetime.strptime(timestamp.strip(),TIMESTAMP_FORMAT)
                old_timestamp=datetime.datetime.strptime(log_dict[date][0].strip(),TIMESTAMP_FORMAT)
                latest_timestamp=max(new_timestamp,old_timestamp)
                log_dict[date][0]=latest_timestamp.strftime(TIMESTAMP_FORMAT)
            preceding_timestamp=True
        elif preceding_timestamp==True:
            # encountered entry message
            log_dict[date][1]=log_dict[date][1]+line
    return log_dict




def add_entry(date,timestamp,message,log_dict):
    """
    validates and add an entry to a log_dict object
    """
    try:
        date_obj=datetime.datetime.strptime(date.strip(),DATETIME_FORMAT)
        timestamp_obj=datetime.datetime.strptime(timestamp.strip(),TIMESTAMP_FORMAT)
        log_dict.setdefault(date,['',''])
        if log_dict[date][0] != '': #indicates an entry without an existing date
            old_timestamp_obj=datetime.datetime.strptime(log_dict[date][0].strip(),TIMESTAMP_FORMAT)
            latest_timestamp_obj=max(timestamp_obj,old_timestamp_obj)
            log_dict[date][0]=latest_timestamp_obj.strftime(TIMESTAMP_FORMAT)
        else:
            log_dict[date][0]=timestamp
        log_dict[date][1]=log_dict[date][1]+message+'\n'
    except Exception as e:
        print("Error: invalid date format "+str(e)) 
        return False
    return True

def write_log(log_dict,log):
    """
    Write the log dictionary into a caplog.txt log file 
    """
    log_dict = dict(sorted(log_dict.items()))
    with open(log, 'w') as f:
        for date,entry in log_dict.items():
            f.write(date+'\n')
            f.write(entry[0]+'\n')
            f.write(entry[1]+'\n') 
            #f.write('\n')

        
if __name__ == '__main__':
    """ 
    specify the path to the log file as a command line argument
    """
    if len(sys.argv) != 2: 
        print("Invalid arguments. Please specify the path to the log file") 
        sys.exit()
    LOG_FILE=sys.argv[1]

    #create file if it does not exist
    if not os.path.exists(LOG_FILE):
        print("Log file doesn't exist. creating one..")
        with open(LOG_FILE,'w+') as f:
            pass 
    
    if not validate_log(LOG_FILE):
        exit(1)
    try:
        today_date=datetime.datetime.now().strftime(DATETIME_FORMAT)
        entry_date=input(f"Enter the entry date ({today_date}) :")
        if entry_date == '':
            entry_date = today_date
        else:
            entry_date=parser.parse(entry_date).strftime(DATETIME_FORMAT)
        entry_timestamp=datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
        entry_message=[]
        print("Enter your Message (press Enter on an empty line to finish)")
        while True:
            line=input()
            if line=='':
                break
            entry_message.append(line)
        entry_message = '\n'.join(entry_message)

        log_dict=read_log(LOG_FILE)
        add_entry(entry_date,entry_timestamp,entry_message,log_dict)
        write_log(log_dict,LOG_FILE)
    except Exception as e:
        print(str(e))
        print("Log entry failed")
        sys.exit(1)
    print('Log entry successful')
    





    



