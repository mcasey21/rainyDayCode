import pyttsx3

def text_to_sound_with_voice(text, voice_gender='male', voice_rate=150):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Select a voice based on gender
    for voice in voices:
        if voice_gender.lower() in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # Adjust the rate for a deeper voice
    engine.setProperty('rate', voice_rate)

    engine.say(text)
    engine.runAndWait()


total = 501

while total != 0:

    print(F"score remaining: {total}")

    score = int(input("Enter your score: "))

    total = total - score

    text_to_sound_with_voice(score, voice_gender='male', voice_rate=150)

    if total < 171 and total != 169 and total != 168 and total != 166 and total != 165 and total != 163 and total != 162 and total != 159 and total != 0:
        text_to_sound_with_voice(F"you have {total} remaining", voice_gender='male', voice_rate=150)

    if total == 0:
        text_to_sound_with_voice("game shot and the match", voice_gender='male', voice_rate=150)

again = input("play again (y/n)").lower()

