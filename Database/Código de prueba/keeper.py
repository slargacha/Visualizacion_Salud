# import libraries necessaries
from csv import DictReader
from pymongo import MongoClient

# Reading files: realPowerLabs, mechanismPowerLabs, costHour, costPlayer
# betaYear, incentivesHour, incentivesPlayer, realPowerLoads, mechanismPowerLoads
# paymentHour, paymentPlayer, price
mechanismPowerLabs = DictReader(open('Docs/labs_power_real.csv','r'))
mechanismPowerLoads = DictReader(open('Docs/load_power_real.csv','r'))
incentivesPlayer = DictReader(open('Docs/I_player.csv','r'))
price_loads_DR = DictReader(open('Docs/price_loads_DR.csv','r'))
price_loads_real = DictReader(open('Docs/price_loads_real.csv','r'))
PowerLabsDR = DictReader(open('Docs/labs_power_DR.csv','r'))
PowerRenewable = DictReader(open('Docs/gen_B.csv','r'))
Price = DictReader(open('Docs/price.csv','r'))
ConsumptionHora = DictReader(open('Docs/labs_power_real_database.csv','r'))
#client connection
client = MongoClient('localhost', 27017)  
mdiDb = client.mdi

# Creation of collections
mechanismPowerLabsYearCollection = mdiDb.mechanismPowerLabsYear #1
mechanismPowerLoadsYearCollection = mdiDb.mechanismPowerLoadsYear #2
incentivesPlayerYearCollection = mdiDb.incentivesPlayerYear #3
price_loads_DRYearCollection = mdiDb.price_loads_DRYear #4
price_loads_realYearCollection = mdiDb.price_loads_realYear #5
PowerLabsDRYearCollection = mdiDb.powerLabsDRYear #6
PowerRenewableYearCollection = mdiDb.powerRenewableYear #7
PriceYearCollection = mdiDb.priceYear #8
ConsumptionHoraCollection = mdiDb.ConsumptionHoraYear #9

# Save collection
def saveLine(line):
    for key, value in line.items():
        #print(key)
        #print(value)
       
        if(key != "Time" and key != ""):  #remove spaces
            if(num==1):
                mLabPower = {
                    'type': key,
                    'kw': float(value),
                    'datetime': line['Time']
                }
                mechanismPowerLabsYearCollection.insert(mLabPower)
            elif(num==2):
                mLoadPower = {
                    'type': key,
                    'kw': float(value),
                    'datetime': line['Time']
                }
                mechanismPowerLoadsYearCollection.insert(mLoadPower)
            if(num==3):
                incentives = {
                    'type': key,
                    'pesos': float(value),
                    'datetime': line['Time']
                }
                incentivesPlayerYearCollection.insert(incentives)
            elif(num==4):
                price_DR = {
                    'type': key,
                    'pesos': float(value),
                    'datetime': line['Time']
                }
                price_loads_DRYearCollection.insert(price_DR)
            elif(num==5):
                price_real = {
                    'type': key,
                    'pesos': float(value),
                    'datetime': line['Time']
                }
                price_loads_realYearCollection.insert(price_real)
            elif(num==6):
                mLabsPower_DR = {
                    'type': key,
                    'kw': float(value),
                    'datetime': line['Time']
                }
                PowerLabsDRYearCollection.insert(mLabsPower_DR)
            elif(num==7):
                renew = {
                    'type': key,
                    'kw': float(value),
                    'datetime': line['Time']
                }
                PowerRenewableYearCollection.insert(renew)
            elif(num==8):
                price = {
                    'type': key,
                    'pesos': float(value),
                    'datetime': line['Time']
                }
                PriceYearCollection.insert(price)
            elif(num==9):
                chora = {
                    'type': key,
                    'kw': float(value),
                    'datetime': line['Time']
                }
                ConsumptionHoraCollection.insert(chora)
            
for line1 in mechanismPowerLabs:
    num=int(1)
    saveLine(line1)
   
for line2 in mechanismPowerLoads:
    num=int(2)
    saveLine(line2)

for line3 in incentivesPlayer:
    num=int(3)
    saveLine(line3)

for line4 in price_loads_DR:
    num=int(4)
    saveLine(line4)

for line5 in price_loads_real:
    num=int(5)
    saveLine(line5)

for line6 in PowerLabsDR:
    num=int(6)
    saveLine(line6)

for line7 in PowerRenewable:
    num=int(7)
    saveLine(line7)

for line8 in Price:
    num=int(8)
    saveLine(line8)

for line9 in ConsumptionHora:
    num=int(9)
    saveLine(line9)
    
