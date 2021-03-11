import pyttsx3 as p
with open(r"C:\face_recognize\Numpy",'r') as f:
    # data = f.readlines()
    # print(data)
    speaker = p.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', 180)
    voices = speaker.getProperty('voices')
    print(len(voices))
    speaker.setProperty('voice', voices[1].id)
    p.speak("A, B, C, D, E, F, G, H, I,J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z")
    # p.speak(data)
    speaker.runAndWait()
    speaker.stop()
