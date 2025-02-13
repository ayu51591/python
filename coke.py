# $ python coke.py                                                                
# Amount Due: 50                                                                  
# Insert Coin: 25                                                                 
# Amount Due: 25                                                                  
# Insert Coin: 10                                                                 
# Amount Due: 15                                                                  
# Insert Coin: 10                                                                 
# Amount Due: 5                                                                   
# Insert Coin: 10                                                                 
# Change Owed: 5 

amount_due = 50
accepted_coins = [25, 10, 5]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        amount_due -= coin

change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
    
    
    
    
