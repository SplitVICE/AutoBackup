# AutoBackup
Backup files and folders inside a .zip file with a Python script and easy setup.

### How does the script works

The script will create .zip files that stores the file you are currently working/using over time (you set a timer).

### How to use

Place the script `AutoBackup.py` and the config file `config.ini` inside the same folder where the file or folder you want to backup over time is placed.
Open the config.ini file with the notepad Windows application or relative and customize the following parameters:
```
input_file_name
output_file_name
backups_folder
seconds_delay_between_backups
```
Input File name: Type the name of the file or folder you want to backup. You must type the file extension.

Output file name: Type the name of the .zip resultant file that will store the backup. The file will also have the date at its name.

Backups folder: Type the name of the folder that will store the .zip backups files.

Seconds delay between backups: Type the seconds in-between the backups.

### Usage example
Example 1: To backup a file called "myDocument.doc" inside a .zip called "myDocument.zip" inside a folder called "My Document backups" every 2 minutes.

`config.ini` parameters:
```
input_file_name=myDocument.doc
output_file_name=myDocument
backups_folder=My Document backups
seconds_delay_between_backups=120
```
Example 2: To backups a file called "drawing.sai" inside a .zip called "backup.zip" inside a folder called "My Drawing save" every 10 minutes.

`config.ini` parameters:
```
input_file_name=drawing.sai
output_file_name=backup
backups_folder=My Drawing save
seconds_delay_between_backups=300
```
### Output .zip file
The output .zip file will always have the date at the end of its name to be able to create different backups and to be easy to know the save date.
Output file example:
`output_file_name=backup`
Output: `backup2020-2-19-22-45-59`
