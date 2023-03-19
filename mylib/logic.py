import wikipedia


def wiki(name="War Goodness", length=1):
    """Wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """Search wikipedia for Names"""
    results = wikipedia.search(name)
    return results
