class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._all_articles.append(self)
        magazine._articles.append(self)
        magazine.add_contributor(author)
        author.articles().append(self)

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls._all_articles