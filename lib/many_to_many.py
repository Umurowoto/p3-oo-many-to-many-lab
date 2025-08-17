class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of related contracts"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of related books using Contract as intermediary"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return total royalties from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of related contracts"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of related authors using Contract as intermediary"""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with the same date"""
        return [contract for contract in cls.all if contract.date == date]
