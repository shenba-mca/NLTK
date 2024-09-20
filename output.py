import csv
# Read the text file and convert to CSV
with open('output.txt', 'r') as txt_file:
    with open('output.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Iterate through each line in the text file
        for line in txt_file:
            # Split the line into fields (adjust the delimiter if needed)
            fields = line.strip().split()
            writer.writerow("Inspirational Quotes")# Default delimiter is whitespace
            writer.writerow(fields)


