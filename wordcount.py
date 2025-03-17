###########################################################
###   Copy and paste your word frequency code here      ###
###   into two new functions:                           ###
###      text_to_word_list()                            ###
###      count_frequencies()                            ###
###   OR add your word frequency code to thie repo as   ###
###   a separate file and import it                     ###
###########################################################
import Frequency
# remove these if you are going to import your frequency module
# def text_to_word_list():
#   pass

# def count_frequencies():
#   pass

word_list = Frequency.text_to_wordlist('sample.txt')
word_freq_dict = Frequency.count_frequencies(word_list)

print(word_freq_dict)
###########################################################
###   Write your new functions here:                    ###
###      find_max_valued_key()                          ###
###########################################################

def find_max_valued_key(word_dict):
  max = 0
  max_key = ''
  for word in word_dict:
    if word_dict[word] > max:
       max = word_dict[word]
       max_key = word
  return (max_key, max)



###########################################################
###   Write your loop to find the top                   ###
###   five most frequent words                          ###
###########################################################

for i in range(5):
  biggest = find_max_valued_key(word_freq_dict)
  print(f"{biggest[0]} appears {biggest[1]} times.")
  word_freq_dict.pop(biggest[0])



