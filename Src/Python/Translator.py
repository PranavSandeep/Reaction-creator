from translate import translate

__author__ = "Pranav Sandeep"

translate.Translator(to_lang="hi", from_lang="en-in")


class Trans:  # IK this is a weird way to put it, but I don't have any other options. All others are over shadowed
    # by other classed ;-;

    def __init__(self):
        self.Translator = ""

    def InitializeTranslator(self, ToLang, FromLang='en-in'):
        self.Translator = translate.Translator(to_lang=ToLang, from_lang=FromLang)

    def Translate(self, TranslateList):
        a = " ".join(TranslateList)

        b = self.Translator.translate(a)

        print(b)

        return b
