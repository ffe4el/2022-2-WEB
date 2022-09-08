def even_odd(a):
    if a % 2==0:
        print("{}는 짝수입니다." .format(a))
    else:
        print("{}는 홀수입니다.".format(a))

def main():
    n = int(input("값을 입력하세요. =>"))
    even_odd(n)


if __name__ == "__main__":
    main()