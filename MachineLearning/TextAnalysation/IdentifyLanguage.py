def identify_language_using_inltk(text):
    from inltk.inltk import identify_language
    return identify_language(text)

def detect_language_using_langdetect(text):
    from langdetect import detect
    try:
        return detect(text)
    except:
        return None

def isocode_to_langname(isocode):
    import pycountry
    lang = pycountry.languages.get(alpha_2=isocode)
    return lang.name

def detect_language_using_googletrans(text):
    from googletrans import Translator
    translator = Translator()
    try:
        return translator.detect(text).lang
    except:
        return None