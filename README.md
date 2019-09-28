# check_processes2 for NSClient++ and Nagios
nagios monitoring module that can check on one or mulitple processes, and return CRITICAL if one of them is not running.
There is already a nagios plugin **check_process**, but there is a bug regarding case sensitivity on Windows:
- https://github.com/mickem/nscp/issues/587 (check_process is unexpectedly case-sensitive #587)  

# Usage
`check_processes2 process1.exe process2.exe process3.exe`
