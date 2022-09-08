def main():
    total =0
    for i in range(1, 101):
        if i % 2 ==0 :
            total += i
    print(total)

    all_even = [i for i in range (1, 101) if i %2 ==0]
    print(all_even)
    print(sum(all_even))

    print(sum([i for i in range(1, 101) if i %2 ==0]))
    
if __name__ == "__main__":
    main()