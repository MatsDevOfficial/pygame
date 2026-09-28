import os
import time
import sys

print("Hello " + input("What is your name?"))

print("As you wander into the old abandoned mineshaft, you hear a bang behind you")

time.sleep(3)

WIDTH = 24
HEIGHT = 13
DEPTH = 4

def render(w, click=False):
    inset_free = int(DEPTH * (WIDTH - w) / WIDTH)
    rows = []
    for r in range(HEIGHT):
        line = ""
        for c in range(WIDTH):
            if c >= w:
                line += "."
                continue
            inset = round(inset_free * c / max(w - 1, 1))
            if r < inset or r >= HEIGHT - inset:
                line += "."
            elif r == inset or r == HEIGHT - inset - 1:
                line += "="
            elif c == 0 or c == w - 1:
                line += "|"
            elif c == w - 3 and r == HEIGHT // 2 and w >= 8:
                line += "o"  # door knob
            else:
                line += " "
        rows.append("|" + line + "|")
    top = "+" + "-" * WIDTH + "+"
    out = [top] + rows + [top, "=" * (WIDTH + 2)]
    out.append("   *BANG!*" if click else "")
    return "\n".join(out)

def main():
    try:
        sys.stdout.write("\033[?25l")
        for w in list(range(2, WIDTH + 1)):
            sys.stdout.write("\033[2J\033[H" + render(w, click=(w == WIDTH)))
            sys.stdout.flush()
            time.sleep(0.08 if w < WIDTH - 4 else 0.14)
        time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\n")
        
if __name__ == "__main__":
    main()

time.sleep(0.6)

os.system('cls' if os.name == 'nt' else 'clear')


print("hello world")    