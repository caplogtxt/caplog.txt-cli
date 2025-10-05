

Caplog.txt-cli is a simple python-based command line tool to manage your caplog.txt formatted log file.  



# Usage

Pass the path of the log file as the argument in the command line.

```python
python main.py /home/user/caplog.txt
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
