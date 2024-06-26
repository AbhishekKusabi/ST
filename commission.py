lockPrice = 45.0
stockPrice = 30.0
barrelPrice = 25.0

totalLocks = 0
totalStocks = 0
totalBarrels = 0

locks = int(input("Enter the number of locks: "))

while locks != -1:
    stocks = int(input("Enter the number of stocks: "))
    barrels = int(input("Enter the number of barrels: "))
    
    totalLocks += locks
    totalStocks += stocks
    totalBarrels += barrels
    
    locks = int(input("Enter the number of locks: "))
    
print("Total locks: ", totalLocks)
print("Total stocks: ", totalStocks)
print("Total barrels: ", totalBarrels)

lockSales = totalLocks * lockPrice
stockSales = totalStocks * stockPrice
barrelSales = totalBarrels * barrelPrice

sales = lockSales + stockSales + barrelSales
print("Total sales: ", sales)

if sales > 1800:
    commission = 0.10 * 1000 + 0.15 * 800 + 0.20 * (sales - 1800)
elif sales > 1000:  
    commission = 0.10 * 1000 + 0.15 * (sales - 1000)
else:
    commission = 0.10 * sales
    
print("Commission: ", commission)

# Output:
# Enter the number of locks: 3
# Enter the number of stocks: 4
# Enter the number of barrels: 5
# Enter the number of locks: 2
# Enter the number of stocks: 3
# Enter the number of barrels: 4
# Enter the number of locks: -1
# Total locks:  5
# Total stocks:  7
# Total barrels:  9
# Total sales:  460.0