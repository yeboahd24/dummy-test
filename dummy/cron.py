import os

def database_backup():
    print("database_backup")
    os.system("python3 manage.py dbbackup")