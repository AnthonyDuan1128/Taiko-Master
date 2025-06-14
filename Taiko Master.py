# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mss keyboard pillow

import mss
import keyboard
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as mg
from PIL import Image
import time

def select_region():#说明6
    print('不要关闭该运行窗口，否则将无法运行')
    mg.showinfo("说明","下面即将弹出选择窗口，请按下并滑动鼠标选择侦测区域。")
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill=tk.BOTH, expand=True)

    region = {"x1": 0, "y1": 0, "x2": 0, "y2": 0}

    def on_mouse_down(event):
        region["x1"], region["y1"] = event.x, event.y

    def on_mouse_up(event):
        region["x2"], region["y2"] = event.x, event.y
        root.quit()

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()
    root.destroy()
    mg.showinfo("按键说明", "按 'p' 开始检测，按 'o' 暂停检测，按 'i' 退出程序。")

    x1, y1, x2, y2 = region["x1"], region["y1"], region["x2"], region["y2"]
    return {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}

def detect_color_and_press_key(region):
    with mss.mss() as sct:
        running = False

        def start_detection():
            nonlocal running
            running = True
            print("Detection started")

        def pause_detection():
            nonlocal running
            running = False
            print("Detection paused")

        def bye_bye():
            quit()

        keyboard.add_hotkey('p', start_detection)
        keyboard.add_hotkey('o', pause_detection)
        keyboard.add_hotkey('i', bye_bye)

        while True:
            if not running:
                time.sleep(0.1)
                continue

            screenshot = sct.grab(region)
            img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)
            pixels = img.load()

            # 定义颜色范围
            lower_red = (100, 0, 0)
            upper_red = (255, 50, 50)
            black = (0, 0, 0)
            lower_blue = (0, 100, 100)
            upper_blue = (50, 255, 255)

            red_detected = False
            black_detected = False
            blue_pixel_count = 0

            for y in range(img.height):
                for x in range(img.width):
                    r, g, b = pixels[x, y]
                    if lower_red <= (r, g, b) <= upper_red:
                        red_detected = True
                    if (r, g, b) == black:
                        black_detected = True
                    if lower_blue <= (r, g, b) <= upper_blue:
                        blue_pixel_count += 1

            # 设定蓝色成片的阈值，如超过总像素的10%
            blue_area_threshold = 0.1 * img.width * img.height

            if red_detected and black_detected:
                print("Pressing 'f'")
                keyboard.press_and_release('f')
                time.sleep(0.1)  # 添加延迟
            elif black_detected and blue_pixel_count >= blue_area_threshold:
                print("Pressing 'd'")
                keyboard.press_and_release('d')
                time.sleep(0.1)  # 添加延迟
            else:
                print("No valid color detected")
                time.sleep(0.1)  # 添加延迟，避免频繁检测

if __name__ == "__main__":
    region = select_region()
    detect_color_and_press_key(region)
