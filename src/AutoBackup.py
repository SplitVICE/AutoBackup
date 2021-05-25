###############################################################
#     _   _   _ _____ ___  ____    _    ____ _  ___   _ ____
#    / \ | | | |_   _/ _ \| __ )  / \  / ___| |/ / | | |  _ \
#   / _ \| | | | | || | | |  _ \ / _ \| |   | ' /| | | | |_) |
#  / ___ \ |_| | | || |_| | |_) / ___ \ |___| . \| |_| |  __/
# /_/   \_\___/  |_| \___/|____/_/   \_\____|_|\_\\___/|_|
#
###############################################################
# VERSION 1.0
###############################################################
# by:
#
#██╗   ██╗██╗ ██████╗███████╗
#██║   ██║██║██╔════╝██╔════╝
#██║   ██║██║██║     █████╗
#╚██╗ ██╔╝██║██║     ██╔══╝
# ╚████╔╝ ██║╚██████╗███████╗
#  ╚═══╝  ╚═╝ ╚═════╝╚══════╝
#
###############################################################
# WEB PAGE : http://split-vice.com/
###############################################################

# CREDITS #
###########

# CREDITS:
# - Syntax provider: https://www.w3schools.com/python/
# - ASCII art: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# - Special thanks to F. and M.

##########################################
##########################################
##########################################
##########################################
##########################################

# PY FILE IMPORTS.
# .ZIP IMPORT.
import zipfile

# SLEEP FUNCTION CALL IMPORT (time.sleep([time])).
import time

# TO CREATE FOLDERS.
import os

# TO GET DATE.
import datetime

# IMPORT TO SEE IF THE FOLDER GIVEN AT CONFIG EXISTS.
import os.path

# IMPORT TO CLOSE THE PROGRAM.
import sys


#########################################################
#########################################################
#########################################################
#########################################################
# CONFIG VARIABLES CLASS#################################

class UserData:
    def __init__(self, input_file_name, output_file_name, backups_folder, seconds_delay_between_backups):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.backups_folder = backups_folder
        self.seconds_delay_between_backups = seconds_delay_between_backups

    minimum_time_delay = 15


# USER DATA OBJECT INSTANCE.
user_data = UserData('folderContentExample', 'Backup', 'Backups', 1)


# END OF CONFIG VARIABLES CLASS##########################
#########################################################
#########################################################
#########################################################
#########################################################

# LOADS DATA FROM config.ini AND STORES IT INSIDE THE UserData OBJECT.
def load_config_settings_from_ini_file():
    print('Loading settings...')
    if does_ini_file_exist():
        from configparser import ConfigParser

        config = ConfigParser()
        config_file_list = ['config.ini']
        config.read(config_file_list)

        user_data.input_file_name = config.get('userdata', 'input_file_name')
        user_data.output_file_name = config.get('userdata', 'output_file_name')
        user_data.backups_folder = config.get('userdata', 'backups_folder')
        user_data.seconds_delay_between_backups = int(config.get('userdata', 'seconds_delay_between_backups'))
        print('Settings loaded. OK.')
        print('----------------------------------------------------------')
        print('Input archive: ' + user_data.input_file_name)
        print('Output zip file archive: ' + user_data.output_file_name)
        print('Backups folder name: ' + user_data.backups_folder)
        print('Delay time between save: ' + str(user_data.seconds_delay_between_backups))
        print('----------------------------------------------------------')
    else:
        print('config.ini file was not found. Recover config.ini file or download the script again.')
        print('Press any key to close.')
        input_message_holder = input()
        close_script()


# CHECKS IF config.ini FILE EXISTS.
def does_ini_file_exist():
    from os import path
    return path.exists('config.ini')


# VALIDATIONS BEFORE THE BACKUP LOOP STARTS.
def starter_method_tree(input_file, output_file, delay_seconds, folder_name):
    print('Starting Auto Backup ...\n...')
    if input_file_exists(input_file):
        if is_minimum_time_delay_ok(delay_seconds, user_data.minimum_time_delay):
            make_backups_folder(folder_name)
            backup_loop(input_file, output_file, delay_seconds, folder_name)
    else:
        error_input_file_not_found(input_file)


# CHECKS IF THE INPUT FILE ARCHIVE EXISTS.
def input_file_exists(input_file):
    from os import path
    return path.exists(input_file)


# CHECK IF THE TIME BETWEEN DOING BACKUPS IF EQUALS OR OVER minimum_time_delay variable. BY DEFAULT, IT IS SET AS 15
# SECONDS.
def is_minimum_time_delay_ok(delay_seconds, minimum_time_delay):
    if delay_seconds >= minimum_time_delay:
        print('Time between backup equals or over ' + str(minimum_time_delay) + ' second/s. OK.')
        return True
    else:
        print('Delay between making a backup cannot be below ' + str(minimum_time_delay) + ' seconds for security.')
        print('Please, check your config settings.')
        print('Press any key to close.')
        input_message_holder = input()
        close_script()
        return False


# MAKES THE FOLDER WHERE THE BACKUPS WILL BE STORED.
def make_backups_folder(folder_name):
    print('Building backups folder...\n...')
    try:
        os.mkdir(folder_name)
        print('Backups folder: OK.')
    except:
        print('Backups folder already exists. OK.')


# ERROR MESSAGE THAT WILL BE DISPLAYED ON CONSOLE IF THE INPUT FILE ARCHIVE DOES NOT EXIST.
def error_input_file_not_found(input_file):
    input_type_temp = check_if_input_is_file_or_folder(input_file)
    if input_type_temp == 'dir':
        print('Folder name given not found. Please check your config settings')
        print('Press any key to close.')
        input_holder = input()
        sys.exit()
    else:
        print('File name given not found. Please check your config settings')
        print('Press any key to close.')
        input_holder = input()
        sys.exit()


# METHOD TO BUILD THE DATE STRING.
def build_date():
    now = datetime.datetime.now()
    return str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(
        now.minute) + '-' + str(now.second)


# .ZIP FILE BUILDER LOOP METHOD.
def backup_loop(input_file, output_file, delay_seconds, folder_name):
    print('...\nConfiguration: OK.\n...')
    print('AutoBackup initiated.')
    backup_cont = 1
    input_file_type = check_if_input_is_file_or_folder(input_file)
    while True:
        time.sleep(delay_seconds)
        now = build_date()
        if input_file_type == 'dir':
            backup_zip_folder(folder_name, output_file, now, input_file)
        else:
            backup_zip_file(folder_name, output_file, now, input_file)
        backup_message_alert(now, backup_cont)
        backup_cont += 1


# RETURNS "dir" IF THE ARCHIVE IS FOLDER. RETURNS "file" IF IT IS SOME KIND OF FILE.
def check_if_input_is_file_or_folder(input_file):
    # is it dir of file.
    from os import path
    if path.isdir(input_file):
        return 'dir'
    else:
        return 'file'


# IF THE ARCHIVE TO BACKUP IS A FILE, THIS METHOD IS CALLED.
def backup_zip_file(folder_name, output_file, now, input_file):
    jungle_zip = zipfile.ZipFile(folder_name + '\\' + output_file + now + '.zip', 'w')
    jungle_zip.write(input_file, compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()


# IF THE ARCHIVE TO BACKUP IS A FOLDER, THIS METHOD IS CALLED.
def backup_zip_folder(folder_name, output_file, now, input_file):
    zf = zipfile.ZipFile(folder_name + '\\' + output_file + now + '.zip', "w")
    for dirname, subdirs, files in os.walk(input_file):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()


# CONSOLE MESSAGE TO DISPLAY WHEN A BACKUP WAS MADE.
def backup_message_alert(now, backup_cont):
    print(str(backup_cont) + '. ' + now + '. ' + user_data.input_file_name + ' backed up.')
    backup_cont += 1


# METHOD TO CLOSE THE SCRIPT.
def close_script():
    sys.exit()


# WELCOME CONSOLE MESSAGE.
def console_initiation_print():
    str = '''
   db    88   88 888888  dP"Yb  88""Yb    db     dP""b8 88  dP 88   88 88""Yb
  dPYb   88   88   88   dP   Yb 88__dP   dPYb   dP   `" 88odP  88   88 88__dP
 dP__Yb  Y8   8P   88   Yb   dP 88""Yb  dP__Yb  Yb      88"Yb  Y8   8P 88"""
dP""""Yb `YbodP'   88    YbodP  88oodP dP""""Yb  YboodP 88  Yb `YbodP' 88
'''
    print(str)
    print('-------------------------------------------------------------------------------------------------------------')


# INITIALIZATION METHOD.
def RUN_SCRIPT():
    console_initiation_print()
    load_config_settings_from_ini_file()
    starter_method_tree(user_data.input_file_name
                        , user_data.output_file_name
                        , user_data.seconds_delay_between_backups
                        , user_data.backups_folder)


RUN_SCRIPT()
