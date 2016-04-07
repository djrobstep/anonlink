
"""


"""
import bloommatcher as bm


class IdentifierType:
    """
    Base class used for all identifier types.

    Required to provide a mapping of schema to hash type
    uni-gram or bi-gram.
    """

    def __init__(self, unigram=False, weight=1, **kwargs):
        """

        :param unigram: Use uni-gram instead of using bi-grams
        :param int weight: How many times to include this identifier.
        Can be set to zero to skip
        """
        self.weight = int(weight)
        self.tokenizer = bm.unigramlist if unigram else bm.bigramlist
        self.kwargs = kwargs

    def __call__(self, entry):
        result = []
        for i in range(self.weight):
            for token in self.tokenizer(entry, **self.kwargs):
                result.append(token)

        return result

basic_types = {
    'index': IdentifierType(weight=0),
    'dob': IdentifierType(unigram=True, toremove='/'),
    'name': IdentifierType(),
    'gender': IdentifierType()
}

