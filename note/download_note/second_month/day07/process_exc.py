import time

def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("%s运行时间%.6f"%(f.__name__,end_time-start_time))
        return  res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

@timeis
def no_multi_process():
    prime = []
    for i in range(1,100001):
        if isPrime(i):
            prime.append(i)
    sum(prime)

if __name__ == '__main__':
    # no_multi_process运行时间26.246834
    no_multi_process()