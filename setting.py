from easygui import EgStore


class Settings(EgStore):

    def __init__(self, filename):
        self.author = ""
        self.book = ""

        self.filename = filename
        self.restore()


settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = '小甲鱼'
book = '《零基础》'

settings.author = author
settings.book = book
settings.store()
print('保存完毕')

settingsFilename = "settings.txt"
settings = Settings(settingsFilename)
print(settings)