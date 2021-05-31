from django.core import management

def my_cron_job():
    try:
        management.call_command("mycommand")
    except:
        print('error with cron job')