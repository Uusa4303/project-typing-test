import time

def typing_test():
    print("Welcome to the Typing Test!")
    print("You will be given a random sentence to type.")
    input("Press Enter to continue...")

    sentence = "The quick brown fox jumps over the lazy dog"
    print("Type the following sentence:\n")
    print(sentence)

    start_time = time.time()
    user_input = input("\n")
    end_time = time.time()

    time_taken = end_time - start_time

    correct_chars = 0
    incorrect_chars = []
    for i in range(len(user_input)):
        if i >= len(sentence):
            break
        if user_input[i] == sentence[i]:
            correct_chars += 1
        else:
            incorrect_chars.append(user_input[i])

    accuracy = correct_chars / len(sentence) * 100
    words_per_minute = len(user_input.split()) / (time_taken / 60)

    print(f"\nTime taken: {round(time_taken, 2)} seconds")
    print(f"Accuracy: {round(accuracy, 2)}%")
    print(f"Words per minute: {round(words_per_minute, 2)}")

    if len(incorrect_chars) > 0:
        print("\nYou made the following mistakes:")
        for char in incorrect_chars:
            print(char, end=" ")

typing_test()
