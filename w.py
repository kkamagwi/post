# Как получить информацию из Википедии
# установите библиотеку
# pip install wikipedia

import wikipedia


wikipedia.set_lang("ru")
print(wikipedia.page('название статьи').summary)

# @endgmPythON