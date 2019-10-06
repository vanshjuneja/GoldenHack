import CompareAssetsVsLiabilties as ca
import AssetsVsAssets as aa
import EquityVsEquity as ee
import AssetsSplit as asp
import LiabilitiesSplit as lsp
import RevenueVsExpenses as re
import RevenueVsRevenue as rr
import BalanceSheets as bs
import FinancialInf as fi
import Targeter as trg
import os
import sys

if os.path.exists('static/RevenueVsRevenue.html'):
    os.remove('static/RevenueVsRevenue.html')

if os.path.exists('static/AssetsSplit.html'):
    os.remove('static/AssetsSplit.html')

if os.path.exists('static/LiabilitiesSplit.html'):
    os.remove('static/LiabilitiesSplit.html')

if os.path.exists('static/RevenueVsExpenses.html'):
    os.remove('static/RevenueVsExpenses.html')

if os.path.exists('static/AssetsVsAssets.html'):
    os.remove('static/AssetsVsAssets.html')

if os.path.exists('static/EqVsEq.html'):
    os.remove('static/EqVsEq.html')

if os.path.exists('static/AssetsVsLiabilities.html'):
    os.remove('static/AssetsVsLiabilities.html')

# INITIALIZATION
bs.oldBalanceSheet()
bs.newBalanceSheet()

########## VARIABLES ##########
old_assets = open("static/assetsOld.txt", 'r')
old_liab = open("static/liabOld.txt", 'r')
old_oe = open("static/oeOld.txt", 'r')
old_assetsVSLiab = open("static/assets_vs_liabOld.txt", 'r')
assets = open("static/assets.txt", 'r')
liab = open("static/liab.txt", 'r')
oe = open("static/oe.txt", 'r')
assetsVSLiab = open("static/assets_vs_liab.txt", 'r')

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
revtt = 0


# TextExtractor Methods
def getVals():
    global oe_total
    global assetsTotal
    global liabTotal
    global old_oe_total
    global old_assetsTotal
    global old_liabTotal
    line = old_assets.readline().replace('\n', '')
    global revtt
    global revone
    global expenses
    global tg1
    global tg2

    while line:
        old_a_titles.append(line)
        line = old_assets.readline().replace('\n', '').replace(',', '')
        old_a_vals.append(int(line))
        line = old_assets.readline().replace('\n', '').replace(',', '')

    line = old_liab.readline().replace('\n', '')
    revtt = trg.revTT()
    expenses = trg.getExP()

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
    revone = trg.revOnE()
    tg1 = fi.Ta1
    tg2 = fi.Ta2

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

    c1 = ca.CompareAssetsVsLiabilities(int(assetsTotal), int(liabTotal))
    c2 = aa.AssetsVsAssets(float(old_assetsTotal), float(old_liabTotal), float(assetsTotal), float(liabTotal))
    c3 = ee.EquityVsEquity(old_oe_total, oe_total)
    c4 = asp.AssetsSplit(a_titles, a_vals)
    c5 = lsp.LiabilitiesSplit(L_titles, L_vals)
    c6 = re.RevenueVsExpenses(revtt, expenses)
    c7 = rr.RevenueVsRevenue(revone, revtt, tg1, tg2)
    sys.exit()




getVals()
