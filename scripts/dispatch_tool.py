import csv

with open('data/service_requests.csv') as f:
    reader = csv.DictReader(f)
    print("Pending Dispatch Tickets Requiring Initial Review:")
    print("-" * 60)
    for row in reader:
        if row['status'] == 'Open' and row['initial_review_done'].lower() != 'yes':
            print(f"Ticket {row['ticket_id']} at {row['site']}: {row['issue']} (Initial review missing)")
