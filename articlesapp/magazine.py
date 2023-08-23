class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        self._all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name() == name:
                return magazine

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls._all_magazines:
            titles.extend([article.title() for article in magazine._articles])
        return titles

    def contributors(self):
        return self._contributors

    def add_contributor(self, author):
        self._contributors.append(author)