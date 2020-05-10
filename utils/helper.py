import os
import shlex
import subprocess
import sys


def cmd_exec(str):
    logger.debug("\n------------------------ Executing Command: Start ------------------------")
    logger.debug("\n$>>" + str)    
    output = os.popen(str).read().strip()
    logger.debug("\n$>>" + output)
    logger.debug("\n------------------------ Executing Command: END ------------------------")
    return output


def get_system_type():
    platform = sys.platform;
    logger.debug("Platform : " + platform)
    system_name = "NA";
    if platform == "linux" or platform == "linux2":
       system_name = const.LINUX_OS
    elif platform == "darwin":
        system_name = const.MAC_OS
    elif platform == "win32":
        system_name = const.WINDOWS_OS
        
    logger.debug("System Name : " + system_name)
    return system_name;
