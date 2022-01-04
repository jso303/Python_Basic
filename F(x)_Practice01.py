def open_account():
    print("새로운 계좌가 생성되었습니다")
    
def deposit(balance, money):    # balance : 잔액 / money : 입금액
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money

balance = 0         # 잔액
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않있습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100    # 수수료 100원
    print("출금이 완료되었습니다. 잔액은 {0} 원 입니다. 저녁 수수료는 {1} 원 입니다."\
        .format(balance-money-commission, commission))  # \를 사용하면 두줄을 한줄 처럼 사용가능
    return commission, balance-money-commission

balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 500)
print(balance)
balance = deposit(balance, 2000)
print(balance)
balance = withdraw_night(balance, 1000)
print(balance)