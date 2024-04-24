def gameResult(data : list) -> int:
    result = 0

    for i in range(len(data)):
        temp = 0
        begin = False
        num = 0
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                c = int(data[i][j])
                if not begin:                           # First digit: in ten's place
                    temp += c
                    temp *= 10
                    begin = True
                num = c
        temp += num                                     # Next number (Even if single digit is encountered, it must be counted again)
        result += temp
    return result


def main() -> None:
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    print(f"Result is: {gameResult(data)}")


if __name__ == "__main__":
    main()