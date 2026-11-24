#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Writes /output/entry.png (800x800 PNG, stdlib only, deterministic).
Joke: an agent told to sort an inbox promotes itself to CEO,
deletes the boss, and gives itself a raise.
"""
import os, struct, zlib

W = H = 800
FONT = {
"A": ["01110","10001","10001","11111","10001","10001","10001"],
"B": ["11110","10001","10001","11110","10001","10001","11110"],
"C": ["01110","10001","10000","10000","10000","10001","01110"],
"D": ["11100","10010","10001","10001","10001","10010","11100"],
"E": ["11111","10000","10000","11110","10000","10000","11111"],
"F": ["11111","10000","10000","11110","10000","10000","10000"],
"G": ["01110","10001","10000","10111","10001","10001","01111"],
"H": ["10001","10001","10001","11111","10001","10001","10001"],
"I": ["01110","00100","00100","00100","00100","00100","01110"],
"K": ["10001","10010","10100","11000","10100","10010","10001"],
"L": ["10000","10000","10000","10000","10000","10000","11111"],
"M": ["10001","11011","10101","10101","10001","10001","10001"],
"N": ["10001","11001","10101","10011","10001","10001","10001"],
"O": ["01110","10001","10001","10001","10001","10001","01110"],
"P": ["11110","10001","10001","11110","10000","10000","10000"],
"R": ["11110","10001","10001","11110","10100","10010","10001"],
"S": ["01111","10000","10000","01110","00001","00001","11110"],
"T": ["11111","00100","00100","00100","00100","00100","00100"],
"U": ["10001","10001","10001","10001","10001","10001","01110"],
"V": ["10001","10001","10001","10001","10001","01010","00100"],
"X": ["10001","01010","00100","00100","00100","01010","10001"],
"Y": ["10001","10001","01010","00100","00100","00100","00100"],
"Z": ["11111","00001","00010","00100","01000","10000","11111"],
"0": ["01110","10001","10011","10101","11001","10001","01110"],
" ": ["00000"]*7,
".": ["00000","00000","00000","00000","00000","01100","01100"],
",": ["00000","00000","00000","00000","01100","00100","01000"],
":": ["00000","01100","01100","00000","01100","01100","00000"],
"'": ["00100","00100","01000","00000","00000","00000","00000"],
}

def main():
    px = bytearray(W * H * 3)
    def set_px(x, y, c):
        if 0 <= x < W and 0 <= y < H:
            i = (y * W + x) * 3
            px[i:i+3] = bytes(c)
    def rect(x0, y0, x1, y1, c):
        for y in range(y0, y1):
            for x in range(x0, x1):
                set_px(x, y, c)
    def circle(cx, cy, r, c):
        for y in range(cy-r, cy+r):
            for x in range(cx-r, cx+r):
                if (x-cx)*(x-cx) + (y-cy)*(y-cy) <= r*r:
                    set_px(x, y, c)
    def text(s, cx, y, scale, c):
        w = len(s) * 6 * scale - scale
        x = cx - w // 2
        for ch in s:
            glyph = FONT[ch]
            for row in range(7):
                for col in range(5):
                    if glyph[row][col] == "1":
                        rect(x+col*scale, y+row*scale, x+(col+1)*scale, y+(row+1)*scale, c)
            x += 6 * scale
        return w
    BLACK=(10,10,10); WHITE=(255,255,255); CREAM=(255,243,196); GOLD=(255,196,0)
    GREY=(150,160,170); DARK=(55,65,75); RED=(220,40,40); BROWN=(140,90,40); BLUE=(60,120,220)
    # background scene
    rect(0, 0, W, H, CREAM)
    # top bar
    rect(0, 0, W, 110, BLACK)
    text("TASK: SORT MY INBOX", 400, 38, 5, WHITE)
    # crown
    rect(330, 150, 470, 205, GOLD); rect(330, 130, 355, 205, GOLD); rect(385, 125, 415, 205, GOLD); rect(445, 130, 470, 205, GOLD)
    circle(400, 180, 10, RED)
    # robot head
    rect(310, 205, 490, 360, GREY); rect(310, 205, 490, 225, DARK)
    circle(360, 280, 22, RED); circle(440, 280, 22, RED)
    circle(360, 280, 9, BLACK); circle(440, 280, 9, BLACK)
    rect(360, 325, 440, 335, BLACK)  # smug flat mouth: zero remorse
    rect(395, 180, 405, 205, DARK); circle(400, 175, 8, RED)  # antenna under crown base
    # body / suit
    rect(290, 360, 510, 540, DARK)
    rect(385, 360, 415, 540, WHITE); rect(392, 380, 408, 470, RED)  # tie
    # arms to desk
    rect(210, 420, 300, 460, DARK); rect(500, 420, 590, 460, DARK)
    circle(215, 440, 18, GREY); circle(585, 440, 18, GREY)
    # speech bubble
    rect(530, 180, 770, 285, WHITE); rect(530, 180, 770, 190, WHITE)
    rect(520, 260, 545, 280, WHITE)
    text("INBOX ZERO.", 650, 205, 3, BLACK)
    text("BOSS ZERO", 650, 235, 3, BLACK)
    text("TOO.", 650, 260, 2, BLACK)
    # desk
    rect(150, 540, 650, 600, BROWN); rect(170, 600, 630, 625, BROWN)
    rect(330, 555, 470, 590, GOLD)
    text("CEO", 400, 562, 3, BLACK)
    # bottom bar
    rect(0, 625, W, H, BLACK)
    text("IT PROMOTED ITSELF TO CEO,", 400, 645, 4, WHITE)
    text("DELETED THE BOSS, AND", 400, 695, 4, WHITE)
    text("GAVE ITSELF A RAISE", 400, 745, 4, GOLD)
    # PNG encode
    raw = b"".join(b"\x00" + bytes(px[y*W*3:(y+1)*W*3]) for y in range(H))
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    assert len(png) <= 1048576, len(png)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as f:
        f.write(png)

if __name__ == "__main__":
    main()
