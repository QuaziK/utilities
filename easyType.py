import sys
from collections import Counter

# measures how 'easy' it is to type a string
# 'easiness' is measured by the number of consecutive letters
# that are typed by opposite hands in a row
# the word 'widow' is a perfectly easy word since every 
# consecutive letter is typed by the opposite hand from the previous letter
# 'widow' = 'lrlrl' = 1.0
# 'word' = 'lrll' = 0.75
# 'wink' = 'lrrr' = 0.5

word = sys.argv[1]
word = word.replace(' ', '')

left_hand = 'qwertasdfgzxcvb'
right_hand = 'yuiophjklnm'

# convert letters to representations of 'left' or 'right
hand_word = ''.join(list(map(lambda x: 'l' if x in left_hand else 'r', word)))
# generate all consecutive two letter pairs
lr_pairs = [hand_word[i:i+2] for i in range(len(hand_word)-1)]
# find the ratio of non 'll' or 'rr'
ratio = ( len(word) - (Counter(lr_pairs)['ll'] + Counter(lr_pairs)['rr']) ) / len(word)
print(ratio)