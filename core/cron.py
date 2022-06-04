from django.core.management import call_command


def database_backup():
   try:
      call_command('dbbackup')
   except Exception as e:
      print(e)
      pass
    

