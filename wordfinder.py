#/Users/nathantjahjadi/words.txt

from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, source):
        """Read from a source file and store words in a list"""
        self.source = source
        self.list = []
        self.populate_list_from_source()

    def __repr__(self):
        return f"<WordFinder with {len(self.list)} number of words>"

    def populate_list_from_source(self):
        """Read file and add each line to the instance's list"""
        file = open(self.source, "r")

        #requires document to have a linebreak after the last word
        for line in file:
            self.list.append(line[:-1])

        file.close()

        print(f"{len(self.list)} words read")

    def random(self):
        """Return a random word from the instance's list"""
        return choice(self.list)
