from text_cleaner import keep
from text_cleaner.processor.common import ASCII
from text_cleaner.processor.misc import URL, ESCAPED_WHITESPACE
import re

text = '#FETISH 💅👅💄 Jetzt " dsd |  " @asd $asdf auf Spotify ►► http://spoti.fi/1NRkIwE'

k = keep(
    text,
    [ASCII],
)
k = URL.remove(k)

expression = '(\#[a-zA-Z0-9]+)|(\@[A-Za-z0-9]+)|\$(\w+)|([#@$"|])'

k = ' '.join(re.sub(expression, " ", k).split())

print(k)
