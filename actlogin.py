import mechanize
import re
import platform    # For getting the operating system name
import subprocess 
import logging
import time
from systemd.journal import JournaldLogHandler
import traceback
import os
from dotenv import load_dotenv

load_dotenv()
uname = os.getenv('UNAME')
pword = os.getenv('pword')

# create logger with 'ACTLoginService'
logger = logging.getLogger('ACTLoginService')
logger.setLevel(logging.DEBUG)

journald_handler = JournaldLogHandler()

journald_handler.setLevel(logging.WARNING)

# create file handler which logs even debuimport loggingg messages
fh = logging.FileHandler('actlog.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
journald_handler.setFormatter(formatter)
logger.addHandler(journald_handler)


# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# TODO:
# 1. File Logger with timestamp and cleanup mechanism
# XXX ---- 2. Sleep Mechanism ---- XXX DONE 
# 3. Seperate Commandlet for standalong exec
# 4. Create a service
# 5. ENV variable
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def login_to_act():
    for control in br.form.controls:
            if not control.name:
                print (" - (type) =", (control.type))
                continue
            if re.match("_login_", control.name):
                br.form[control.name]=uname
                print('populated uname')
            if control.type == 'password':
                br.form['pword'] = pword
                print('populated pwd')
            print (" - (name, type, value) =", (control.name, control.type, br[control.name]))
    br.submit()
    
if __name__ == '__main__':
    while True:
        # -- This makes the process continuously running
        # -- We will create a Browser instance and fetch the page 
        # -- We will ping 8.8.8.8 to check internet reachability
        

        while ping('8.8.8.8'):
            # -- Once the ping is successful we wait for 30 secs
            time.sleep(30)
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.open('https://selfcare.actcorp.in/web/ni/home')
            logger.error('8.8.8.8 unreachable starting login sequence')
            # -- In case Ping fails we start the process of login
            # -- We select the form using login
            # -- we then call login function
            
            br.select_form(action=re.compile(".*login\?.*"))
            login_to_act()
        except mechanize.FormNotFoundError as e:
            
            # -- If Internet issue and we are not able to login then we are fucked
            # -- Check if by any chance network is available this is for some cases there is upstream connection issue            
            if not ping('8.8.8.8') :
                logger.error('Internet DOWN')
            else: 
                # -- This means Internet is available
                logger.warning('Logged IN and Internet is available')
        except Exception as e:
            logger.error(traceback.format_exc())
            print("Some Issue other Issue")

        # We will sleep for 10 minutes before we retry login
        logger.warning("Sleeping for 5 minutes")
        time.sleep(300)
