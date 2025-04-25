from account import SavingsAccount, CheckingAccount
from user import BankUser

user1 = BankUser('A', 1000)

# 입출금 계좌에 $200 저축

# 현금 200$ 차감
user1.deduct_money(200)
# 입출금 계좌에 200$ 저축
account1 = CheckingAccount(user1.get_name(), 200)
# 보유 계좌 목록에 새로운 계좌 추가
user1.add_account(account1)

# 현금 800$ 차감
user1.deduct_money(800)
# 예금 계좌에 800$ 저축
account2 = SavingsAccount(user1.get_name(), 800, 0.05)
# 보유 계좌 목록에 새로운 계좌 추가
user1.add_account(account2)

# 예금 계좌에서 출금 전, 출금 가능하도록 하게 한다.
account2.unlock()

# 예금 계좌에서 $ 400 출금
account1.withdraw(400)
# 다시 사용자에게 지급
user1.add_money(400)

# 지급된 $400를 다시 빼와서
user1.deduct_money(400)
# 예금 계좌에 저축
account1.deposit(400)

# 보유한 현금과 계좌목록 출력
user1.get_assets()


