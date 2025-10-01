import math

balances = []
type_acnt = []

while True:
    account_name = input("what is the name of the account: ")
    if account_name != "quit":
        type_acnt.append(account_name)
        account_balance = float(input("What is the balance of the account:  "))
        balances.append(account_balance)
    elif account_name == "quit":
        break

for i in range(len(type_acnt)):
    name = type_acnt[i]
    balance = balances[i]
    print(f"{i}. {name} - {balance}")

total = 0
for balance in balances:
    total = total + balance

update = "yes"
while update == "yes":
    update = input("Do you want to update an acount?")
    if update == "no":
        break
    new_index = int(input("What account number do you want to update?"))
    new_balance = float(input("What is the new balance amount?"))
    type_acnt[new_index] = new_balance

num_acnt = len(type_acnt)
average = total / num_acnt

print(f"\nTotal Balance: {total}")
print(f"The Average is {average:.2f}")

max_balance = max(balances)
max_index = balances.index(max_balance)
max_acount = type_acnt[max_index]

print(f"Greatest Account: {max_acount} - ${max_balance}")