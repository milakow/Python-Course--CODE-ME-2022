import webbrowser

class URLError(Exception):
    ''' custom error for url'''

try:
    url = str(input('Podaj adres www: '))
    if not (url.startswith('https://', 'http://', 'www') and url.endswith('.pl', '.com')):
        raise URLError('Url jest nieprawidłowy')

finally:
    webbrowser.open(url)


