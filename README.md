# sqlite-database-builder

Builds an SQLite database from relational txt or csv files contained in a zip file. 

## Description

Run SQL queries in vscode using the SQLite extension by alexcvzz. 

## How To Install

*Make sure you have paired SSH keys with Github*

From the main repository page click the green Code button dropdown, then copy the SSH URL and run the following command from the command line in your chosen location:
```
git clone [SSH URL]
```
Move into the repository folder that has just been created and run:
```
pip install -r requirements.txt
```
If you're using a Linux distribution you may need to install sqlite3 (not necessary for mac users), for ubuntu use:
```
sudo apt install sqlite3
```
Add the zip file you want to convert into a sqlite database to the repository folder and run the command:
```
python3 create_sqlite_db.py [zipfile_name.zip] [chosen_database_name.db]
```
This will create the database. Open the repository in vscode and install the vscode SQLite extension. Open vscode command palatte:
```
CTRL + SHIFT + P
```
(cmd for mac users)

Click on `SQLite: Open Database` and choose your database. This will open SQLite Explorer in the lower left panel where you can see the table names and column headers with types. 
Create a new file ending with .sql and run queries with:
```
CTRL + SHIFT + Q
```
To change keyboard shortcuts go to `File -> Preferences -> Keyboard Shortcuts` on windows or `Code -> Settings -> Keyboard Shortcuts` on a mac 

