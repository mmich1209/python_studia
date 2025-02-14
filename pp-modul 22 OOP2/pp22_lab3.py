class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print(f"tytuł: {self.__title} author: {self.__author}")

    def show_full_info(self):
        print(f"tytuł: {self.__title} author: {self.__author} wydawca: {self.__publisher} rok wydania: {self.__year}")


ksiazka = Book("Dzieci z Bulerbyn", "Adam Mickiewicz", "ksiegarnia Rybnik", "1999")
ksiazka.show_short_info()

ksiazk2 = Book("Moby Dick", "Herman Meville", "Wydawnictwo Ameryka", "2000")
ksiazk2.show_full_info()

