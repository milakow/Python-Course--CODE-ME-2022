#Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www.
#Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się: 'https://'; 'http://'; 'www'
#Może się kończyć za pomocą: '.pl'; '.com'
#Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.
import webbrowser

class URLError(Exception):
    ''' custom error for url'''

def is_correct(url):
    beginning = 'https://', 'http://', 'www'
    end = '.pl', '.com'

    if not url.startswith(beginning):
        raise URLError('The prefix is incorrect.')
    if not url.endswith(end):
        raise URLError('The sufix is incorrect.')
    else:
        return url

def open_url(url_address):
    try:
        url = is_correct(url_address)
        webbrowser.open(url)
    except URLError as e:
        print('I have a problem: ', e)


def main():
    url = str(input('Enter the URL: '))
    open_url(url)


if __name__ == '__main__':
    main()

