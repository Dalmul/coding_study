from user import BankUser
from account import CheckingAccount, SavingsAccount
# 고객 B는 900$ 잔액을 보유하고 있다.
user_b = BankUser('B', 900)

# 고객 B는 입출금 계좌에 $800를 저축, 예금 계좌에 $100를 저축한다.
user_b.deduct_money(800)
account1 = CheckingAccount(user_b.get_name(), 800)
"""여기서 계좌 개설과 입출금이 따로 이루어지는 것을 비효율적. 계좌 개설과 입출금이 한꺼번에 이루어지도록 develop 연구"""
user_b.deduct_money(100)
account2 = SavingsAccount(user_b.get_name(), 100, 0.06)
user_b.add_account(account1)
user_b.add_account(account2)

# 입출금 계좌에서 $800를 출금하려 했지만 출금한도에 걸려 실패
# 출금 한도를 $800로 수정 후, 출금금

# withdraw 시도했다가가
try: 
    account1.withdraw(800)
# 에러 발생시 출금한도 해제 후 재입금금
except ValueError:
    account1.update_limit(800)
    account1.withdraw(800)
finally:
    user_b.add_money(800)

# 보유한 현금과 계좌목록 출력력
user_b.get_assets()




