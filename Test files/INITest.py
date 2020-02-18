from configparser import ConfigParser

#OBJECT INSTANCE.
parser = ConfigParser()

#TO READ VALUES INSIDE INIFILE.

#You can add two configuration file instances.
config_file_list = ['/home/jerry/config_file_1.ini', '/home/jerry/config_file_2.ini']

#Assign the two config ini files to the same parse object.
parser.read(config_file_list)['/home/jerry/config_file_1.ini', '/home/jerry/config_file_2.ini']

#Field inside first IniFile
print(parser.get('oracle_conn', 'host'))
#Field inside second IniFile
print(parser.get('account', 'user_name'))

#TO WRITE VALUES INSIDE INIFILE.

#TEST IF SECTIONS EXIST
parser.has_section('mysql_conn')
parser.has_option('mysql_conn', 'port')

#Source: https://www.dev2qa.com/how-to-use-python-configparser-to-read-write-configuration-file/