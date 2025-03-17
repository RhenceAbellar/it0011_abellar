excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

def analyze_text(text):

    clear = "".join(char if char.isalnum() or char.isspace() else " " for char in text)

    word_list = clear.split()
    
    word_count = {}
    filtered_total = 0

    for word in word_list:
        word_lower = word.lower()
        if word_lower not in excluded_words:
            word_count[word] = word_count.get(word, 0) + 1
            filtered_total += 1

    lowercase_words = [word for word in word_count if word.islower()]
    uppercase_words = [word for word in word_count if not word.islower()]

    lowercase_words.sort()
    uppercase_words.sort()
    
    print("\n")
    for word in lowercase_words + uppercase_words:
        print(f"{word:<10} - {word_count[word]}")
    print("\n============================")
    
    print(f"Total words filtered: {filtered_total}")
    print("============================")

text_input = input("Enter a string statement\n: ")
analyze_text(text_input)
