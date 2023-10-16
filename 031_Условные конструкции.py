def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question

def normalize_url(adr: str):

    if adr.startswith("https://"):
        adr_norm = adr
    elif adr.startswith("http://"):
        adr_norm = "https://" + adr[7:]
    else:
        adr_norm = "https://" + adr

    return adr_norm

print(normalize_url('https://ya.ru'))
print(normalize_url('google.com'))
print(normalize_url('http://ai.fi'))