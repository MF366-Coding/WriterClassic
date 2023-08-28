# Get the absolute path of the script
script_path = _PATH.abspath(__file__)

# Get the directory containing the script
script_dir = _PATH.dirname(script_path)

user_data = _PATH.join(script_dir, 'user_data')

import datetime # Really, bro?
now = datetime.datetime.now()

_LOG = open(f"{user_data}/log.wclassic", mode="a", encoding="utf-8")
