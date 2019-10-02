# check_process2 for NSClient++ and Nagios
nagios monitoring module that can check on one or mulitple processes, and return CRITICAL if one of them is not running.
There is already a nagios plugin **check_process**, but there is a bug regarding case-sensitivity on Windows:
- https://github.com/mickem/nscp/issues/587 (check_process is unexpectedly case-sensitive #587)  

Hence, this module may help as a workaround, until the bug in **check_process** is fixed.

# Deployment
## NSClient++
- Copy the "check_process2.exe" to your NSClient++\scripts folder.  
- Edit your nsclient.conf and add these changes:  
`[/settings/NRPE/server]
allow arguments=false

[/settings/external scripts]
allow arguments=false

[/settings/external scripts/scripts]
check_process2=scripts\check_process2.exe %ARGS%`
- Restart the NSClient++ Service  

# Nagios Server
Define a check command:  
`define command{
        command_name    check_windows_myCoreProcesses
        command_line    /usr/lib64/nagios/plugins/check_nrpe -2 -H '$HOSTADDRESS$' --command check_process2 --args process1.exe process2.exe process3.exe process4.exe
}
`
Make sure to replace the exe names with your own.  
Define a service:  
`
define service{
        service_description     MyApplicationCoreProcesses
        hostgroup_name          hgr_myservers
        use                     generic-service
        check_command           check_windows_myCoreProcesses
}
`
Restart the nagios server.  

# Usage
`check_process2.exe process1.exe process2.exe process3.exe`
