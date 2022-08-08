from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('192.168.1.132', 9999)

t = threading.Thread(target=sender.start_stream())
t.start()

while True:
    continue

# sender.stop_stream()
