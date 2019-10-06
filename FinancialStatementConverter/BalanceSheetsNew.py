import csv


with open('Financial_Statements\BalanceSheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0

    assets = open("assets.txt", 'w')
    liab = open("liab.txt", 'w')
    oe = open("oe.txt", 'w')
    assetsVSLiab = open("assets_vs_liabOld.txt", 'w')

    asset_titles = []
    asset_values = []
    liab_titles = []
    liab_values = []
    oe_titles = []
    oe_values = []
    oe_total = 0
    liab_total = 0
    oe_total = 0

    for row in csv_reader:
        if count > 4 and count < 17:
            asset_titles.append(row[0])
            asset_values.append(row[1])
        elif count == 18:
            asset_total = row[1]
        elif count > 20 and count < 28:
            liab_titles.append(row[0])
            liab_values.append(row[1])
        elif count == 28:
            liab_total = row[1]
        elif count == 33:
            oe_total = row[1]
        count += 1

    for x in range(0,asset_values.__len__()):
        print(asset_titles[x]+': '+asset_values[x])
        assets.write(asset_titles[x]+'\n')
        assets.write(asset_values[x]+'\n')
    for x in range(0,liab_values.__len__()):
        print(liab_titles[x]+': '+liab_values[x])
        liab.write(liab_titles[x] + '\n')
        liab.write(liab_values[x] + '\n')
    print("Assets Total: ", asset_total)
    print("Liabilities Total: ", liab_total)
    print("OE Total: ", oe_total)

    assetsVSLiab.write('Assets' + '\n')
    assetsVSLiab.write(asset_total + '\n')
    assetsVSLiab.write('Liabilities' + '\n')
    assetsVSLiab.write(liab_total)

    oe.write('Owner\'s Equity' + '\n' + oe_total)

    assets.close()
    liab.close()
    oe.close()
    assetsVSLiab.close()
