from collections import defaultdict

def get_anagram(word_list):
    """The logic to group words by their sorted characters."""
    anagram = defaultdict(list)
    for word in word_list:

        key = ''.join(sorted(word))
        anagram[key].append(word)
    return list(anagram.values())

def start_anagram():
    """Recursive function to handle user input and output."""
    
    #i/p
    print("\nAnagram Grouper")
    user_input = input("Enter words separated by spaces('exit' to quit): ").strip()

    #base case
    if user_input.lower() == 'exit':
        print("end program")
        return 

    if user_input:
        word_list = user_input.split()
        result = get_anagram(word_list)
        
        #o/p
        print(f"Grouped Anagrams: {result}")
    else:
        print("Empty string")

    #recursion
    start_anagram()

start_anagram()