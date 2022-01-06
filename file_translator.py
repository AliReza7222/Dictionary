import translators


def translator(text):
    translate = translators.google(text, from_language="en", to_language="fa")
    return translate
