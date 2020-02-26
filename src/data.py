import os


class Dataset:
    def __init__(self):
        self.__readCsv()

    def __readCsv(self):
        root = '/data'
        fileNames = os.listdir(root)


if __name__ == "__main__":
    pass
