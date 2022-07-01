class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')


class Watch(UsefulStuff):
    def __init__(self, watch_name):
        print(watch_name, "is small and convenient")
        super().__init__(watch_name)


class Phone(UsefulStuff):
    def __init__(self, phone_name):
        print(phone_name, "can make a call")
        super().__init__(phone_name)


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is great!')
        super().__init__('Smartwatch')


sw = SmartWatch()

print("********************")

class UsefullStuff:
    def __init__(self, name):
        print(name, 'is very useful')

class Watch(UsefullStuff):
    def __init__(self, brand):
        print(f'Watch {brand}', '-> wear on hand')
        super().__init__()

    def check_time(self):
        print('TIME')

class Phone(UsefullStuff):
    def __init__(self):
        print('Phone', '-> call with it')
        # super().__init__('-- phone --')

    def call(self):
        print('Calling....')

class SmartWatch(Watch, Phone):
    def __init__(self):
        print('SmartWatch is practical')
        super().__init__('SmartWatch')

sw = SmartWatch()
# print(SmartWatch.__mro__)