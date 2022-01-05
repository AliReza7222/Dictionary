import json


class Config:

    file = open("vocabs.json", "r")
    vocabs = json.loads(file.read())

    def forget_vocab(self):
        forget_vocab = self.vocabs["forget_vocabs"]
        return forget_vocab

    def old_vocabs(self):
        old_vocabs = self.vocabs["vocabs"]
        return old_vocabs
