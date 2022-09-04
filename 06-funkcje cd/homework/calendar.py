def get_days_in_month(month):
    print(month[0], '\n')
    for days in range(len(month[1])+1):
        if days > 0:
            if days < 10:
                print(f'0{days}', end=' ')
            else:
                print(days, end=' ')
            if days % 7 == 0:
                print('\n')

    print(2 * '\n')


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

    for month in data:
        get_days_in_month(month)


if __name__ == "__main__":
    main()
