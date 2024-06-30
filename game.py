ser = ["soy", "eres", "es", "somos", "sois", "son"]


sentence_example = "Yo ___ Galina"

def main():
    print(sentence_example)
    print("a. soy     b. es     c. son")
    user_input = input("answer: ")
    if user_input.lower() == "a":
        print("Bien")
    else: 
        print("Mal")
main() 
