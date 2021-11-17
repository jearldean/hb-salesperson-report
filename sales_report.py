"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
"""
salespeople and melons sold are parallel arrays.
It's clutch to not mess up the indexing, though this solution appears to work fine.
Might be less risky to use a dictionary next time.
""" 

f = open('sales-report.txt')
"""
Open the sales-report text file. Entries are in this format:
first_name: str last_name: str|order_total: float|total_melons_sold: int
"""

for line in f:  # Each line is one ORDER
    line = line.rstrip()  # Drop trailing whitespace
    entries = line.split('|')
    # Now you have a list: ['first_name last_name', 'order_total', 'total_melons_sold']

    salesperson = entries[0]  # 'first_name last_name'
    melons = int(entries[2])  # int(total_melons_sold)

    if salesperson in salespeople:  # Already an entry; update record.
        position = salespeople.index(salesperson)  # Get the index of the salesperson

        melons_sold[position] += melons  # Add the order melons to their total.
    else:  # No entry for this salesperson. Make a new entry.
        salespeople.append(salesperson)
        melons_sold.append(melons)

for i in range(len(salespeople)):  # Print the report
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
