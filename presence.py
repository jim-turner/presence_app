presence_indicators = ["now", "stillness", "presence", "awareness", "observer", "breath"]


sentence = "The Power of NOW stillness"
clean_sentence = sentence.lower()  # "the power of now"
words = clean_sentence.split()     # ["the", "power", "of", "now"]

presence_score = 0


for i in words:
    if i in presence_indicators:
        # 1. Update the score here
        presence_score = presence_score + 1
        print("Match found:", i)

# 2. Move this print to the very left margin
print("Total Presence Score:")
print(presence_score)