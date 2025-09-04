from bank_accounts import *

Khayyal=Bank_account(100,"khayyal")
sara=Bank_account(230,"sara")

Khayyal.getBalance()
sara.getBalance()

sara.deposit(205)

Khayyal.withdaw(2999)
Khayyal.withdaw(29)

Khayyal.transfor(102,sara)

khalid=IntersetRewardAccount(100,"khaild")

khalid.getBalance()

khalid.deposit(100)

khalid.transfor(20,Khayyal)

Blaze=SavingsAcount(1000,"Blaze")

Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfor(100,sara)
Blaze.withdaw(100)

