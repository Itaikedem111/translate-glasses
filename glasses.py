#להוריד את הספרייה speech_recognition: pip install SpeechRecognition
#להוריד את הספרייה pyaudio: pip install pyaudio
#אפשר להשתמש בpip3 אם pip רגיל לא עובד
import speech_recognition as sr



def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("אני שומע, אני מחכה לפקודת 'סיום' לסיים")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language='he-IL')
                print(f"{text}")

                if text == "סיום":
                    print("אוקיי, עוצר")
                    break

            except sr.UnknownValueError:
                print("לא הצלחתי לזהות שום מלל ,אנא נסה לדבר ברור יותר.")
            except sr.RequestError as e:
                print(f" יש בעיה עם החיבור לשירות: {e}")

if __name__ == "__main__":
    main()
