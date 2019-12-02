from unicodedata import normalize


class Regex(object):

    def remove_acents(self, txt: str) -> str:
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
