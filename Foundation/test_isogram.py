from unittest import TestCase, mock, main
from Assessment2 import is_isogram


class TestIsIsogram():

#testing to see if an isogram returns true
    def test_1(self):
        string = "abcdefg"
        expected = True
        actual = is_isogram(string)
        self.assetEqual(actual, expected)


#testing to see if a string that is not an isogram returns false
    def test_1(self):
        string = "abcdefgabc"
        expected = False
        actual = is_isogram(string)
        self.assetEqual(actual, expected)

#an empty string should return false
    def test_1(self):
        string = ""
        expected = False
        actual = is_isogram(string)
        self.assetEqual(actual, expected)


TestIsIsogram()

