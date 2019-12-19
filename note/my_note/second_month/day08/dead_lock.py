"""
    模拟死锁产生过程
"""
from time import sleep
from threading import Thread, Lock

# 账户类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 账户名
        self.balance = balance  # 存款
        self.lock = lock # 锁对象

    # 取钱，
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


#　创建两个账户
Tom = Account("Tom", 5000, Lock())
Alex = Account("ALex", 8000, Lock())

# 转账
def transfer(from_, to, amount):
    """
    :param from_:从该账户转钱 
    :param to: 给这个账户转入
    :param amount: 转账金额
    :return: None
    """
    from_.lock.acquire()  # from_上锁
    from_.withdraw(amount) # from_钱减少
    sleep(0.1)
    # 钱减少后，就立即解锁，方便其他操作使用
    from_.lock.release()  # from_解锁
    to.lock.acquire() # to上锁
    to.deposit(amount)  # to 钱增加
    to.lock.release()  # to 解锁
    # from_.lock.release()  # from_解锁


# 创建一个线程
t1 = Thread(target=transfer, args=(Tom, Alex, 1500))
t2 = Thread(target=transfer, args=(Alex, Tom, 3000))
t1.start()
t2.start()
t1.join()
t2.join()


print("TOm:", Tom.get_balance())
print("Alex:", Alex.get_balance())
























