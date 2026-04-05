import sys
import time
import threading

def type_writer(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(text="Scanning"):
    stop_flag = {"stop": False}

    def animate():
        while not stop_flag["stop"]:
            for c in "|/-\\":
                if stop_flag["stop"]:
                    break
                sys.stdout.write(f"\r{text}... {c}")
                sys.stdout.flush()
                time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    def stop():
        stop_flag["stop"] = True
        t.join()
        sys.stdout.write("\r" + " " * 50 + "\r")

    return stop

def progress_bar(total, prefix="Progress"):
    for i in range(total + 1):
        percent = int((i / total) * 100)
        bar = "█" * (percent // 2) + "-" * (50 - percent // 2)
        sys.stdout.write(f"\r{prefix}: |{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(0.03)
    print()
