def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    count = 0
    prime_number = []
    for n in range(100, 200):
        if is_prime_number(n):
            print(n)
            count += 1
            prime_number.append(n)
    print(count)
    print(len(prime_number))






if __name__ == "__main__":
    main()