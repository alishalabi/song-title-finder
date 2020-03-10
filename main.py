class SongTitleFinder:
    def __init__(self, input, corpus):
        self.input = input.upper().split(" ")
        self.corpus = set()
        for key in corpus:
            self.corpus.add(key.upper())
        self.output = []

    def recursive_search(self, current_index=0, current_combo=None, all_combinations=None):
        """
        Perform a nested recursive search for each combinaiton of words in input
        """
        if all_combinations == None:
            all_combinations = []
        if current_combo == None:
            current_combo = []
        # Exit condition: no more items to iterate
        # Iterate through each first word in remaining array
            # Add word to current combo
            # Add combo to all combos
            # Recursively iterate through each remaining word in remaining array


sample_input1 = "Hey ma I though that I told you I like the way you move"
sample_song_dict1 = {"HEY MA", "I Like the way YOU move",
                     "happy days", "Is a good show"}
test1 = SongTitleFinder(sample_input1, sample_song_dict1)
# Seeing if sample input and sample dict are properly converted
print(f"Converted sample input: {test1.input}")
print(f"Converted sample dict: {test1.corpus}")
