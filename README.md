# nagios-check_processes2
nagios monitoring module that can check on one or mulitple processes, and return CRITICAL if one of them is not running.
There is already a nagios plugin check_process, but it has a bug:  
- https://github.com/mickem/nscp/issues/587 (check_process is unexpectedly case-sensitive #587)  

# Usage
check_processes2 process1.exe process2.exe process3.exe
