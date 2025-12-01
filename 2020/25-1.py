def main():
    test_1 = 5764801

    public_key_1 = 10441485
    public_key_2 = 1004920

    current = 1
    num = 7
    count = 0
    while True:
        count += 1
        current = current * num
        current = current % 20201227
        if current == public_key_1:
            loop_size = count
            break

    current = 1
    num = public_key_2

    for i in range(loop_size):
        current = current * num
        current = current % 20201227

    print(current)


if __name__ == "__main__":
    main()
