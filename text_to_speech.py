from gtts import gTTS
import os

text = "Fırat Üniversitesi Yazılım Mühendisliği Programı."
ses = gTTS(text, lang="tr", slow=False)

ses.save("ses.mp3")
os.system("start ses.mp3")