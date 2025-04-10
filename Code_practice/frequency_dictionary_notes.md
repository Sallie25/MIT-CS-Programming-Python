Understanding the Frequency Dictionary Code

This readme details my understanding of the way the frequency_dictionary code operates for my future self.

"beatles" is the variable that stores the dictionary returned by lyrics_to_frequency(she_loves_you). This dictionary keeps track of how many times each word appears in the lyrics.

The function most_common_words(freqs) returns a tuple containing a list of the most frequently occurring words and their count (words, best). Basically, it finds the word(s) with the highest occurrence and returns them along with that count.

Then, words_often(freqs, minTimes) runs in a loop, grabbing the most common words, saving them as tuples ((word, best)), and deleting them from the dictionary. It keeps doing this until there are no words left that meet the minTimes condition.