from datetime import date


today_mo = date.today().month
today_day = date.today().day
today_str = str(today_mo) + str(today_day)

msg_id = int(today_str)

# pull the motd from the db

# connect to the slack channel

# post the message of the day

