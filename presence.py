presence_indicators = ["now", "stillness", "presence", "awareness", "observer", "breath"]

def get_score(text_to_check):
    # Everything inside the function is indented
    clean_text = text_to_check.lower()
    words = clean_text.split()
    
    current_score = 0 
    
    for i in words:
        word = i.strip(".,!?;") 
        if word in presence_indicators:
            current_score = current_score + 1
            
    return current_score  # This "gives back" the final number

# Now we use the function
score_yesterday = get_score("I was not in the now.")
score_today = get_score("I am in the stillness of the now.")

print(f"Yesterday's Score: {score_yesterday}")
print(f"Today's Score: {score_today}")

if score_today > score_yesterday:
    print("Presence is increasing! Well done.")

user_entry = input("How was your day? Type your journal entry here: ")
final_score = get_score(user_entry)

print(f"Your Presence Score for this entry is: {final_score}")