from datetime import datetime
from time import gtime, strftime
input_date = input(" please input date: ")
date_time = datetime.fromisoformat(input_date)
output_format = "%d-%m-%Y %H:%M:S %z"
changed_date = date_time.strftime(output_format)
print(changed_date)