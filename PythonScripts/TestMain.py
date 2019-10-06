import CompareAssetsVsLiabilties as ca
import AssetsVsAssets as aa
import EquityVsEquity as ee
import AssetsSplit as asp
import LiabilitiesSplit as lsp
import RevenueVsExpenses as re
import RevenueVsRevenue as rr
import BalanceSheets as bs

# INITIALIZATION
bs.oldBalanceSheet()
bs.newBalanceSheet()

########## VARIABLES ##########
old_assets = open("assetsOld.txt", 'r')
old_liab = open("liabOld.txt", 'r')
old_oe = open("oeOld.txt", 'r')
old_assetsVSLiab = open("assets_vs_liabOld.txt", 'r')
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


########## ######### ##########


# TextExtractor Methods
def getVals():
    global oe_total
    global assetsTotal
    global liabTotal
    global old_oe_total
    global old_assetsTotal
    global old_liabTotal
    line = old_assets.readline().replace('\n', '')

    while line:
        old_a_titles.append(line)
        line = old_assets.readline().replace('\n', '').replace(',', '')
        old_a_vals.append(int(line))
        line = old_assets.readline().replace('\n', '').replace(',', '')

    line = old_liab.readline().replace('\n', '')

    while line:
        old_L_titles.append(line)
        line = old_liab.readline().replace('\n', '').replace(',', '')
        old_L_vals.append(int(line))
        line = old_liab.readline().replace('\n', '').replace(',', '')

    old_oe.readline()
    old_oe_total = old_oe.readline().replace('\n', '')

    line = old_assetsVSLiab.readline()
    old_assetsTotal = old_assetsVSLiab.readline().replace('\n', '').replace(',', '')
    old_assetsVSLiab.readline()
    old_liabTotal = old_assetsVSLiab.readline().replace('\n', '').replace(',', '')

    line = assets.readline().replace('\n', '')

    while line:
        a_titles.append(line)
        line = assets.readline().replace('\n', '').replace(',', '')
        a_vals.append(int(line))
        line = assets.readline().replace('\n', '').replace(',', '')

    line = liab.readline().replace('\n', '')

    while line:
        L_titles.append(line)
        line = liab.readline().replace('\n', '').replace(',', '')
        L_vals.append(int(line))
        line = liab.readline().replace('\n', '').replace(',', '')

    oe.readline()
    oe_total = int(oe.readline().replace('\n', '').replace(',', ''))

    assetsVSLiab.readline()
    assetsTotal = int(assetsVSLiab.readline().replace('\n', '').replace(',', ''))
    assetsVSLiab.readline()
    liabTotal = int(assetsVSLiab.readline().replace('\n', '').replace(',', ''))


# c1 = ca.CompareAssetsVsLiabilities(assets=5, liabilties=10)
# c2 = aa.AssetsVsAssets(30, 5, 40, 3)
# c3 = ee.EquityVsEquity(15,12)
# c4 = asp.AssetsSplit(
#     ['hi', 'my', 'name', 'is', 'bill', 'bil2l', 'bi3ll', 'bil4l', 'bi5ll', 'bill6', 'bi7ll', 'bi8ll', 'bill9', 'billw9',
#      'beill9', 'birll9'],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
# c5 = lsp.LiabilitiesSplit(
#     ['hi', 'my', 'name', 'is', 'bill', 'bil2l', 'bi3ll', 'bil4l', 'bi5ll', 'bill6', 'bi7ll', 'bi8ll', 'bill9', 'billw9',
#      'beill9', 'birll9'],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
# c6 = re.RevenueVsExpenses(100, 5)
# c7 = rr.RevenueVsRevenue(1003.24,2382.54, 1200, 2000)

getVals()

print('______________________________')
print('______________________________')
print('______________________________')

print(a_titles)
print(a_vals)
print(L_titles)
print(L_vals)
print(oe_total)
print(assetsTotal)
print(liabTotal)

print('______________________________')
print('______________________________')
print('______________________________')

print(old_a_titles)
print(old_a_vals)
print(old_L_titles)
print(old_L_vals)
print(old_oe_total)
print(old_assetsTotal)
print(old_liabTotal)
