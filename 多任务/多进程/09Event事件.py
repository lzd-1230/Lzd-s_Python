from threading import Event, Thread
import time

event = Event()
def light():
    print("红灯ing")
    time.sleep(2)
    print("绿灯了")
    event.set()

def car(name):
    print(f"{name}正在等红灯")
    event.wait()
    print(f"{name}过马路")

if __name__ == "__main__":
    t = Thread(target=light)
    t.start()
    for i in range(10):
        t = Thread(target=car, args=(i,))
        t.start()
