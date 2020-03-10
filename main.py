class SongTitleFinder:
    def __init__(self, input, corpus):
        self.input = input.upper()
        self.corpus = set()
        for key in corpus:
            self.corpus.add(key.upper())
        # Converted input will come from convert_input()
        self.converted_input = None

    def convert_input(self):
        """
        Convert string into array
        """

        # for letter
        pass

    def recursive_search(self):
        """
        """
        pass


sample_input1 = "Hey ma, I though that I told you I like the way you move"
sample_song_dict1 = {"HEY MA", "I Like the way YOU move",
                     "happy days", "Is a good show"}
test1 = SongTitleFinder(sample_input1, sample_song_dict1)
# Seeing if sample input and sample dict are properly converted
print(f"Converted sample input: {test1.input}")
print(f"Converted sample dict: {test1.corpus}")
