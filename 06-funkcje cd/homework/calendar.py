def print_days_in_month(data):
    for month in data:
        print(month[0])
        print(type(month[1]))
        for days in month[1]:
            print(days.endswith(''))
        print('\n')


def main():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
          ]

    # index = data[1].index('February')
    # print(index)
    print_days_in_month(data)

if __name__ == "__main__":
    main()
