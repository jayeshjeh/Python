def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = int(input())
        data.append(num)

    print(data)

    print("Enter number to find")
    null = int(input())

    sum = 0
    for i in range(v1):
        if(data[i] == null):
            sum = sum + 1

    print("Frequency is : ", sum)


def main():
    print("Enter the length of numbers")
    no1 = int(input())

    ret = fun(no1)

if __name__ == "__main__":
    main()

