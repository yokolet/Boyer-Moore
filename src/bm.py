from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    """
    Creates a skip table from the given pattern.

    :param pattern: the pattern to create the skip table.
    :return: skip table as a dictionary.
    """
    table = dict()
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        """
        The constructor for a class Bm.

        :param text: The text to be searched
        :param pattern: The pattern to search in the text.
        """
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        """
        Based on the skip table, returns a shift width of the given character.

        :param c: The character to find the shift width
        :return: The shift width. If the character is not in the shift table, returns -1
        """
        assert len(c) == 1
        if c in self.table:
            return self.table[c]
        return -1

    def search(self) -> int:
        """
        Searches the pattern in the text.

        :return: The index of the pattern's beginning. If not found, returns -1
        """
        m, n = len(self.pattern), len(self.text)
        i = 0
        while i <= (n - m):
            j = m - 1
            while j >= 0 and self.text[i + j] == self.pattern[j]:
                j -= 1
            if j < 0:    # the pattern is found
                return i
            else:
                i += max(1, j - self.decide_slide_width(self.text[i + j]))
        return -1
