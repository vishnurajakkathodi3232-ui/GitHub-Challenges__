def rotate_right(word, positions):
    
    positions = positions % len(word)  
    return word[-positions:] + word[:-positions]

def rotate_left(word, positions):
    
    positions = positions % len(word)
    return word[positions:] + word[:positions]

def encode_sentence(sentence):
    words = sentence.split()
    encoded_words = []
    for i, word in enumerate(words, start=1):
        encoded_word = rotate_right(word, i)
        encoded_words.append(encoded_word)
    return " ".join(encoded_words)

def decode_sentence(encoded_sentence):
    words = encoded_sentence.split()
    decoded_words = []
    for i, word in enumerate(words, start=1):
        decoded_word = rotate_left(word, i)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)

# Taking input sentence
input_sentence = input("Enter the sentence to encode: ").strip().upper()

# Encoding
encoded_message = encode_sentence(input_sentence)
print("Encoded Message:", encoded_message)

# Decoding (Extra challenge)
decoded_message = decode_sentence(encoded_message)
print("Decoded Message:", decoded_message)
