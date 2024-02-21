from gtts import gTTS

# Text to be converted to speech
text = input("Enter the text you want to convert to speech: ")

# Language selection
print("Select the language for text-to-speech conversion:")
print("1. English")
print("2. French")
print("3. German")
language_choice = input("Enter the language choice (1 for English, 2 for French, 3 for German): ")

# Map language choice to language code
language_codes = {
    '1': 'en',
    '2': 'fr',
    '3': 'de'
}

language = language_codes.get(language_choice, 'en')

# Pass the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")
