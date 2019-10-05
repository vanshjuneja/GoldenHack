import csv

with open('Financial_Statements\BalanceSheet2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0

    asset_titles = []
    asset_values = []
    asset_total = 0

    for row in csv_reader:
        if count > 4 and count < 17:
            asset_titles.append(row[0])
            asset_values.append(row[1])
        elif count == 18:
            asset_total = row[1]
        count += 1

    for x in range(0,12):
        print(asset_titles[x]+': '+asset_values[x])
    print("Assets Total: ", asset_total)