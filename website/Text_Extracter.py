old_assets = open("assets.txt", 'r')
old_liab = open("liab.txt", 'r')
old_oe = open("oe.txt", 'r')
old_assetsVSLiab = open("assets_vs_liab.txt", 'r')
assets = open("assets.txt", 'r')
liab = open("liab.txt", 'r')
oe = open("oe.txt", 'r')
assetsVSLiab = open("assets_vs_liab.txt", 'r')

old_a_vals = []
old_a_titles = []

old_L_vals = []
old_L_titles = []

old_oe_total = 0

old_assetsTotal = 0
old_liabTotal = 0

a_vals = []
a_titles = []

L_vals = []
L_titles = []

oe_total = 0

assetsTotal = 0
liabTotal = 0

def getVals():
    line = assets.readline().replace('\n','')

    while line:
        old_a_titles.append(line)
        line = old_assets.readline().replace('\n','').replace(',','')
        old_a_vals.append(int(line))
        line = old_assets.readline().replace('\n','').replace(',','')

    line = old_liab.readline().replace('\n','')

    while line:
        old_L_titles.append(line)
        line = old_liab.readline().replace('\n','').replace(',','')
        old_L_vals.append(int(line))
        line = old_liab.readline().replace('\n','').replace(',','')

    old_oe.readline()
    old_oe_total = old_oe.readline().replace('\n','')

    line = old_assetsVSLiab.readline()
    old_assetsTotal = old_assetsVSLiab.readline().replace('\n','').replace(',','')
    old_assetsVSLiab.readline()
    old_liabTotal = old_assetsVSLiab.readline().replace('\n','').replace(',','')

    line = assets.readline().replace('\n','')

    while line:
        a_titles.append(line)
        line = assets.readline().replace('\n','').replace(',','')
        a_vals.append(int(line))
        line = assets.readline().replace('\n','').replace(',','')

    line = liab.readline().replace('\n','')

    while line:
        L_titles.append(line)
        line = liab.readline().replace('\n','').replace(',','')
        L_vals.append(int(line))
        line = liab.readline().replace('\n','').replace(',','')

    oe.readline()
    oe_total = oe.readline().replace('\n','')

    line = assetsVSLiab.readline()
    assetsTotal = assetsVSLiab.readline().replace('\n','').replace(',','')
    assetsVSLiab.readline()
    liabTotal = assetsVSLiab.readline().replace('\n','').replace(',','')



print(a_titles)
print(a_vals)
print(L_titles)
print(L_vals)
print(oe_total)
print(assetsTotal)
print(liabTotal)