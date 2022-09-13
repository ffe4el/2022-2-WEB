def input_with_check(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if 2 <= value <= 9:
                return value

        except ValueError as e:
            print(e)
            print("2-9까지 자연수를 입력하세요.")

def main():
    # dan =int(input("단을 입력하세요. => "))
    dan = input_with_check("단을 입력하세요. => ")

    for i in range(9):
        print("{} * {} = {}" .format(dan, i+1, dan*(i+1)))

if __name__ == "__main__":
    main()