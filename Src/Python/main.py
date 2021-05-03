"""This is the program's main file. This is where most of the main code lives. All of the crucial functions are there
in this file. """

import random  # For the random emoji thing
import keyboard as k  #
import pyautogui  # For copying the text
import pyperclip  # This is to get whatever is pasted in our clipboard
import sympy  # For doing calculations
from Translator import *
import Wikipedia_Scrapper
import SecondaryClipboard
import threading
import LoadUserSettings

__author__ = "Pranav Sandeep"

Sentences = LoadUserSettings.UserSettings.sentences  # This specifies how many sentences the wikipedia scrapper should


# fetch from wikipedia


# noinspection SpellCheckingInspection
def CleanInput():
    Translator = Trans()

    Translator.InitializeTranslator("ru")  # Initializing it with a random language

    RandomEmoticonList = [":)", ";)", ":(", ";_;", ":D", ":P", ":O", '(⌐■_■)', '༼ つ ◕_◕ ༽つ', '( ͡° ͜ʖ ͡°)', "O_O",
                          "@_@", "T_T", ":3", "<3", "(ᵔᴥᵔ)", "( ━☞´◔‿ゝ◔`)━☞", "｡◕‿‿◕｡ 🗲", "˙ ͜ʟ˙"]

    tlangdict = {
        "rus": "ru",
        "ru": "ru",
        "russian": "Russian",
        "hin": "hi",
        "hi": "hi",
        "af": "af",
        "ta": "Ta",
        "Tamil": "Ta",
        "tamil": "tamil",
        "malayalam": "Malayalam",
        "ger": "German",
        "german": "German",
        "Telugu": "Telugu",
        "Kannada": "Kannada",
        "Marathi": "Marathi",
        "greek": "Greek",
        "latin": "latin",
        "bengali": "bengali",
        "french": "french",
        "norwegian": "norwegian",
        "arabic": "Arabic"
    }  # This is a list of all the languages. The keys are the language specified by the user. You can add more
    # languages by doing what I did.

    pyautogui.hotkey("ctrl", "a")  # What this function does is presses a shortcut key(in this case, control and a)

    pyautogui.keyDown("ctrl")  # Lines 11 to 14 basically do "ctrl + c" (the previous "hotkey" function doesn't seem to
    # work for some reason.)
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")
    pyperclip.copy(pyperclip.paste())  # This pastes what ever we copied in line 11- 14

    CopyInput = pyperclip.paste()  # The value from our clipboard is stored in this variable

    CopyInput = CopyInput.replace('/sad', ':(')  # What this and all other replace commands do is they replace the
    # commands with the emoticons
    CopyInput = CopyInput.replace('/sad.', ':(')
    CopyInput = CopyInput.replace('./sad', ':(')
    CopyInput = CopyInput.replace('./sad.', ':(')
    CopyInput = CopyInput.replace(',/sad', ':(')
    CopyInput = CopyInput.replace('/sad,', ':(')
    CopyInput = CopyInput.replace(',/sad,', ':(')
    CopyInput = CopyInput.replace('/sad!', ':(')
    CopyInput = CopyInput.replace('!/sad!', ':(')

    CopyInput = CopyInput.replace('/wink', ';)')
    CopyInput = CopyInput.replace('/wink.', ';)')
    CopyInput = CopyInput.replace('./wink', ';)')
    CopyInput = CopyInput.replace('./wink.', ';)')
    CopyInput = CopyInput.replace(',/wink', ';)')
    CopyInput = CopyInput.replace('/wink,', ';)')
    CopyInput = CopyInput.replace(',/wink,', ';)')
    CopyInput = CopyInput.replace('/wink!', ';)')
    CopyInput = CopyInput.replace('!/wink!', ';)')

    CopyInput = CopyInput.replace('/happy', ':D')
    CopyInput = CopyInput.replace('/happy.', ':D')
    CopyInput = CopyInput.replace('./happy', ':D')
    CopyInput = CopyInput.replace('./happy.', ':D')
    CopyInput = CopyInput.replace(',/happy', ':D')
    CopyInput = CopyInput.replace('/happy,', ':D')
    CopyInput = CopyInput.replace(',/happy,', ':D')
    CopyInput = CopyInput.replace('/happy!', ':D')
    CopyInput = CopyInput.replace('!/happy!', ':D')

    CopyInput = CopyInput.replace('/ANGERYTABLEFLIP', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('/ANGERYTABLEFLIP.', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('./ANGERYTABLEFLIP', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('./ANGERYTABLEFLIP.', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace(',/ANGERYTABLEFLIP', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('/ANGERYTABLEFLIP,', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace(',/ANGERYTABLEFLIP,', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('/ANGERYTABLEFLIP!', '(ノಠ益ಠ)ノ彡┻━┻')
    CopyInput = CopyInput.replace('!/ANGERYTABLEFLIP!', '(ノಠ益ಠ)ノ彡┻━┻')

    CopyInput = CopyInput.replace('/lenny', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('/lenny.', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('./lenny', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('./lenny.', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace(',/lenny', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('/lenny,', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace(',/lenny,', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('/lenny!', '( ͡° ͜ʖ ͡°)')
    CopyInput = CopyInput.replace('!/lenny!', '( ͡° ͜ʖ ͡°)')

    CopyInput = CopyInput.replace('/gib', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('/gib.', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('./gib', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('./gib.', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace(',/gib', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('/gib,', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace(',/gib,', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('/gib!', '༼ つ ◕_◕ ༽つ')
    CopyInput = CopyInput.replace('!/gib!', '༼ つ ◕_◕ ༽つ')

    CopyInput = CopyInput.replace('/shrug', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('/shrug.', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('./shrug', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('./shrug.', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace(',/shrug', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('/shrug,', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace(',/shrug,', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('/shrug!', '¯\_(ツ)_/¯')
    CopyInput = CopyInput.replace('!/shrug!', '¯\_(ツ)_/¯')

    CopyInput = CopyInput.replace('/random', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('/random.', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('./random', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('./random.', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace(',/random', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('/random,', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace(',/random,', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('/random!', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])
    CopyInput = CopyInput.replace('!/random!', RandomEmoticonList[random.randint(0, len(RandomEmoticonList)) - 1])

    CopyInput = CopyInput.replace('/surprised', ':0')
    CopyInput = CopyInput.replace('/surprised.', ':0')
    CopyInput = CopyInput.replace('./surprised', ':0')
    CopyInput = CopyInput.replace('./surprised.', ':0')
    CopyInput = CopyInput.replace(',/surprised', ':0')
    CopyInput = CopyInput.replace('/surprised,', ':0')
    CopyInput = CopyInput.replace(',/surprised,', ':0')
    CopyInput = CopyInput.replace('/surprised!', ':0')
    CopyInput = CopyInput.replace('!/surprised!', ':0')

    CopyInput = CopyInput.replace('/laugh', 'XD')
    CopyInput = CopyInput.replace('/laugh.', 'XD')
    CopyInput = CopyInput.replace('./laugh', 'XD')
    CopyInput = CopyInput.replace('./laugh.', 'XD')
    CopyInput = CopyInput.replace(',/laugh', 'XD')
    CopyInput = CopyInput.replace('/laugh,', 'XD')
    CopyInput = CopyInput.replace(',/laugh,', 'XD')
    CopyInput = CopyInput.replace('/laugh!', 'XD')
    CopyInput = CopyInput.replace('!/laugh!', 'XD')

    CopyInput = CopyInput.replace('/angery', '>:(')
    CopyInput = CopyInput.replace('/angery.', '>:(')
    CopyInput = CopyInput.replace('./angery', '>:(')
    CopyInput = CopyInput.replace('./angery.', '>:(')
    CopyInput = CopyInput.replace(',/angery', '>:(')
    CopyInput = CopyInput.replace('/angery,', '>:(')
    CopyInput = CopyInput.replace(',/angery,', '>:(')
    CopyInput = CopyInput.replace('/angery!', '>:(')
    CopyInput = CopyInput.replace('!/angery!', '>:(')

    CopyInput = CopyInput.replace('/cheeky', ':P')
    CopyInput = CopyInput.replace('/cheeky.', ':P')
    CopyInput = CopyInput.replace('./cheeky', ':P')
    CopyInput = CopyInput.replace('./cheeky.', ':P')
    CopyInput = CopyInput.replace(',/cheeky', ':P')
    CopyInput = CopyInput.replace('/cheeky,', ':P')
    CopyInput = CopyInput.replace(',/cheeky,', ':P')
    CopyInput = CopyInput.replace('/cheeky!', ':P')
    CopyInput = CopyInput.replace('!/cheeky!', ':P')

    CopyInput = CopyInput.replace('/invisible', '‎')
    CopyInput = CopyInput.replace('/invisible.', '‎')
    CopyInput = CopyInput.replace('./invisible', '‎')
    CopyInput = CopyInput.replace('./invisible.', '‎')
    CopyInput = CopyInput.replace(',/invisible', '‎')
    CopyInput = CopyInput.replace('/invisible,', '‎')
    CopyInput = CopyInput.replace(',/invisible,', '‎')
    CopyInput = CopyInput.replace('/invisible!', '‎')
    CopyInput = CopyInput.replace('!/invisible!', '‎')

    UserInputLines = CopyInput.splitlines()  # Spliting the input by lines so that we don't it doesn't re-type the
    # whole thing in one paragraph

    for i in UserInputLines:
        Eq = ""

        tlist = []

        flag = 0

        TranslateWord = ""

        wikilist = []

        IndWords = i.split()

        if "!tstart" and "!tend" in IndWords:  # User has called the translate command
            TimesOfOccurrence = IndWords.count("!tstart") + IndWords.count("!tend")
            TimesOfOccurrence /= 2  # Counting how many times they have called the command(dividing by 2 because the
            # command is a 2 word - process)

            for t in range(int(TimesOfOccurrence)):
                start_index = IndWords.index("!tstart")  # Getting the index of !tstart and !tend in the IndWords
                end_index = IndWords.index("!tend")

                IndWords[start_index] = ""  # invalidating the index of !tstart and !tend in the IndWords
                IndWords[end_index] = ""

                for j in range(start_index + 1, end_index):
                    tlist.append(IndWords[j])  # Appending all the words to translate in a list(except the first one
                    # is the language specifier)

                for x in range(start_index + 1, end_index):
                    if tlist[0] in tlangdict.keys():
                        Translator.InitializeTranslator(ToLang=tlist[0])  # Initializing the translator with the
                        # language the user has specified

                        tlist[0] = " "  # Invalidating the language specifier in the list coz' we have to use this again
                        IndWords[x] = ""  # Invalidating the language specifier

                        IndWords[x + 1] = Translator.Translate(tlist)

                for j in range(start_index + 3, end_index):
                    IndWords[j] = ""  # Invalidating all the pre-translated word

                for j in range(start_index + 1, end_index):
                    TranslateWord += IndWords[j]

                for j in range(start_index + 1, end_index):  # I'm.... not sure why this is here. But I wrote this
                    # code at 11:00 pm, okay!? I don't remember anything
                    try:
                        if IndWords[j] == "":
                            print(j)
                            IndWords.remove(IndWords[j])
                    except IndexError:
                        pass

                IndWords.remove("")  # This removes all the space so that we can add it later. This fixes the bug
                # where all the words group together in one mess

                print(IndWords)

                FinalWord = " ".join(IndWords)  # This adds the spaces back

                print(FinalWord)

                UserInputLines[UserInputLines.index(i)] = FinalWord  # This updates the text to be written

                i = " ".join(IndWords)  # This updates the variable so that it can be used later

                tlist = []  # Invalidates the list in which we keep all the words so that we store the words so that
                # we can use this again

        if "!calcs" and "!calce" in IndWords:  # Basically the same as the translate thing except some changes
            # WARNING! Be explicit in the algebraic operations. For example, 2x won't work. You should type 2*x. Same
            # goes for the factorization calculator
            TimesOfOccurrence = IndWords.count("!calcs") + IndWords.count("!calce")
            TimesOfOccurrence /= 2

            for t in range(int(TimesOfOccurrence)):
                start_index = IndWords.index("!calcs")  # Getting the index of !tstart and !tend in the IndWords
                end_index = IndWords.index("!calce")

                IndWords[start_index] = ""  # invalidating the index of !tstart and !tend in the IndWords
                IndWords[end_index] = ""

                for j in range(start_index + 1, end_index):
                    Eq += str(IndWords[j])

                CalculatedWord = sympy.sympify(Eq)  # This calculates the result of the result input

                for x in range(start_index + 1, end_index):
                    if flag == 0:
                        IndWords[x] = CalculatedWord
                        flag += 1
                    else:
                        IndWords[x] = ""

                for j in IndWords:
                    IndWords[IndWords.index(j)] = str(IndWords[IndWords.index(j)])

                IndWords.remove("")

                print(str(IndWords))

                FinalWord = " ".join(IndWords)

                print(FinalWord)

                UserInputLines[UserInputLines.index(i)] = FinalWord

                i = " ".join(IndWords)

                flag = 0

                Eq = ""  # Invalidates the calculated output so that we can use this again

        if "!facs" and "!face" in IndWords:  # Literally the same as the calculations except it factorizes instead
            # of calculating
            TimesOfOccurrence = IndWords.count("!facs") + IndWords.count("!face")
            TimesOfOccurrence /= 2

            for t in range(int(TimesOfOccurrence)):
                start_index = IndWords.index("!facs")  # Getting the index of !tstart and !tend in the IndWords
                end_index = IndWords.index("!face")

                IndWords[start_index] = ""  # invalidating the index of !tstart and !tend in the IndWords
                IndWords[end_index] = ""

                for j in range(start_index + 1, end_index):
                    Eq += str(IndWords[j])

                CalculatedWord = sympy.factor(Eq)  # Here it factorizes

                for x in range(start_index + 1, end_index):
                    if flag == 0:
                        IndWords[x] = CalculatedWord
                        flag += 1
                    else:
                        IndWords[x] = ""

                for j in IndWords:
                    IndWords[IndWords.index(j)] = str(IndWords[IndWords.index(j)])

                IndWords.remove("")

                print(str(IndWords))

                FinalWord = " ".join(IndWords)

                print(FinalWord)

                UserInputLines[UserInputLines.index(i)] = FinalWord

                i = " ".join(IndWords)

                flag = 0

                Eq = ""

        if "!wikis" and "!wikie" in IndWords:  # Basically the same as the translate thing except some changes
            # WARNING! Be explicit in the algebraic operations. For example, 2x won't work. You should type 2*x.
            # Same goes for the factorization calculator
            TimesOfOccurrence = IndWords.count("!wikis") + IndWords.count("!wikie")
            TimesOfOccurrence /= 2

            print(TimesOfOccurrence)

            for t in range(int(TimesOfOccurrence)):
                start_index = IndWords.index("!wikis")  # Getting the index of !tstart and !tend in the IndWords
                end_index = IndWords.index("!wikie")

                IndWords[start_index] = ""  # invalidating the index of !tstart and !tend in the IndWords
                IndWords[end_index] = ""

                for j in range(start_index + 1, end_index):
                    wikilist.append(IndWords[j])

                for x in range(start_index + 1, end_index):
                    if flag == 0:
                        IndWords[x] = Wikipedia_Scrapper.ScrapeWikipedia(wikilist, Sentences=int(int(Sentences)))
                        flag += 1
                    else:
                        IndWords[x] = ""

                for j in IndWords:
                    IndWords[IndWords.index(j)] = str(IndWords[IndWords.index(j)])

                IndWords.remove("")

                print(str(IndWords))

                FinalWord = " ".join(IndWords)

                print(FinalWord)

                UserInputLines[UserInputLines.index(i)] = FinalWord

                i = " ".join(IndWords)

                flag = 0

                wikilist = []  # Invalidates the wiki list so that we can use this again

    for i in UserInputLines:  # This add back the lines
        if i == "":
            UserInputLines[UserInputLines.index(i)] = "\n"

    print(UserInputLines)

    CleansedInput = "".join(UserInputLines)  # This makes it so that it can be typed

    pyperclip.copy(CleansedInput)  # This copies it to our clipboard

    pyautogui.hotkey("ctrl", "v")  # This pastes it wherever you want. Make sure your software supports pasting
    # before using this


def Main():
    while True:
        k.record(until='ctrl + 0')  # This records until ctrl + 0 is pressed. Will enable the user to change this
        # later
        CleanInput()  # This calls the function


if __name__ == '__main__':  # This is the main code
    # Using threads so that the we can run the main loop of the code with the secondary clipboard.

    Thread1 = threading.Thread(target=Main)  # The main code loop
    Thread2 = threading.Thread(target=SecondaryClipboard.Copy)  # The secondary keyboard code loop for copying.
    Thread3 = threading.Thread(target=SecondaryClipboard.Paste)  # The secondary keyboard code loop for pasting

    # Starting the threads.
    Thread1.start()
    Thread2.start()
    Thread3.start()

    # Joining the threads so that we can run them simultaneously.
    Thread1.join()
    Thread2.join()
    Thread3.join()
