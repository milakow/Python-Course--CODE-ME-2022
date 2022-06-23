def check_email(email_list, my_email):
    for email in email_list:
        if email == my_email:
            return True
    return False


def main():
    email_list = ['abbc@wp.pl', 'gnfdkfkjgf@gmail.com', 'marysia@onet.pl', 'stasia123@gmail.com', 'olo442@wp.pl']
    my_mail = 'agbc@wp.pl'
    print(check_email(email_list, my_mail))


if __name__ == '__main__':
    main()

