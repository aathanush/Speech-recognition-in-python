import speech_recognition as sr
sound="Recording (13).wav"
r=sr.Recognizer()
with sr.AudioFile(sound) as source:
    r.adjust_for_ambient_noise(source,duration=0.001)
    print("Loading...")
    audio=r.listen(source)
    try:
        print(r.recognize_google(audio))
    except Exception as e:
        print(e)