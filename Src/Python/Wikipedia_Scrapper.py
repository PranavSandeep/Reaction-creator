import wikipedia

__author__ = "Pranav Sandeep"


def ScrapeWikipedia(Query, Sentences):
    a = " ".join(Query)

    WikiResult = wikipedia.summary(str(a), sentences=Sentences)

    return WikiResult
