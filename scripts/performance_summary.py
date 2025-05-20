import csv
from datetime import datetime

open_issues = 0
closed_issues = 0
total_days = 0

with open('data/service_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['status'] == 'Open':
            open_issues += 1
        if row['date_closed']:
            closed_issues += 1
            days = (datetime.strptime(row['date_closed'], "%Y-%m-%d") - datetime.strptime(row['date_opened'], "%Y-%m-%d")).days
            total_days += days

print(f"Open tickets: {open_issues}")
print(f"Resolved tickets: {closed_issues}")
if closed_issues > 0:
    print(f"Average resolution time: {round(total_days / closed_issues, 2)} days")
