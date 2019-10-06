assets = open("assets.txt", 'r')
liab = open("liab.txt", 'r')
oe = open("oe.txt", 'r')
assetsVSLiab = open("assets_vs_liab.txt", 'r')

a_vals = []
a_titles = []

L_vals = []
L_titles = []

oe_total = 0

assetsTotal = 0
liabTotal = 0

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