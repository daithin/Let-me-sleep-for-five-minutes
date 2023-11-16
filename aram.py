import datetime
import time
import pyttsx3
import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("何か話してください")
        audio = r.listen(source)
        print("認識中 ... ")
        try:
            return r.recognize_google(audio, language='ja-JP')
        except Exception as e:
            print("エラー :  " + str(e))


def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()


def alarm(n, nn):
    print(n, "分後にアラームを設定します。")
    time.sleep(n*60)
    print("時間です！")
    speak(nn)


def main():
    speak("何分後にアラームを設定しますか？")
    text = listen()
    try:
        n = int(text)
    except:
        speak("ごめんなさい、聞き取れませんでした。もう一度お願いします。")
        main()
        return
    print(n, "分")
    speak(str(n) + "分後にアラームを設定します。")
    speak("何を発言しましょうか？")
    text = listen()
    try:
        nn = str(text)
    except:
        speak("ごめんなさい、聞き取れませんでした。もう一度お願いします。")
        main()
        return
    speak(str(nn) + "を発言します。")
    alarm(n, nn)


if __name__ == '__main__':
    main()
