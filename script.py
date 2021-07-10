from datetime import date
import datetime

today = datetime.datetime.now()
today_mo = (today_mo.strftime("%B"))
today_day = date.today().day
today_str = str(today_mo) + str(today_day)

msg_id = int(today_str)

# pull the motd from the db

# connect to the slack channel

# post the message of the day

