'''
nagios monitoring module for checking one or mulitple processes not running.
There is already a nagios plugin check_process, but it has a bug
- https://github.com/mickem/nscp/issues/587 (check_process is unexpectedly case-sensitive #587)

Version 0.12 (20191003)

Copyright Toni Feric, Belsoft Collaboration AG 
Feedback toni.feric@belsoft.ch 

Published under the legal terms of MIT license
    https://opensource.org/licenses/MIT 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import argparse, psutil, sys
from sys import exit

psCheck = []
psList = {}
psCheckRunning = []
psCheckNotRunning = []

def argsParse():
    # Parse arguments passed to this script
    parser = argparse.ArgumentParser(description='Nagios plugin to check for running/missing processes.')
    parser.add_argument('processName', metavar='N', type=str, nargs='+', help='Name of a process to be found in the system\'s process table')
    parser.add_argument("--debug", required=False, action='store_true', help='Print additional debug messages (only makes sense when this script is ran by hand)')
    args = parser.parse_args()
    return args

def getPsListLower():
    # Get process list (process table) from system (converted to lower case) and return them as a dictionary
    for ps in psutil.process_iter():
        psList[ps.name().lower()] = ''
    return psList

def isPsRunning(psCheck):
    # Check if a given string is a running process
    if psCheck in psList:
        return 1
    return 0

def checkPsNames(psList):
    # Check all strings if they are a running process or not
    for p in psCheck:
        if args.debug:
            print("DEBUG: checking process p:",p.lower())
        if isPsRunning(p.lower()):
            psCheckRunning.append(p)
        else:
            psCheckNotRunning.append(p)
    return 1

args = argsParse()

if args.debug:
    print(args)

psCheck = args.processName
getPsListLower()

# Do the checks (running/not running) and exit in a nagios manner
if checkPsNames(psList):
    if len(psCheckNotRunning) == 0:
        # All processes are running
        print("OK - all processes running.",', '.join(psCheckRunning))
        exit(0)
    elif len(psCheckNotRunning) <= len(psCheck):
        # At least one process is not running
        print("CRITICAL -",', '.join(psCheckNotRunning),"not running.")
        exit(2)
    else:
        print("UNKNOWN - Too many failed processes.")
        exit(3)

exit(0)
