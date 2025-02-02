# Taiko Master外挂 🎮

## 简介
这个程序是一个用于《太鼓达人》的外挂工具，旨在帮助玩家在游戏中实现更高效的操作。用户可以通过该工具获取判定区域，并通过按键来操控游戏。该程序使用了屏幕捕捉和颜色检测技术，以便在游戏中实现自动化操作。✨

## 原理
该外挂的核心原理是利用屏幕捕捉技术实时监测游戏画面，并通过颜色检测算法识别特定颜色的像素。程序首先要求用户选择一个区域，该区域是游戏中需要监测的判定区域。然后，程序会不断地抓取该区域的屏幕图像，并分析图像中的像素颜色。

- **屏幕捕捉**: 使用 `mss` 库进行高效的屏幕捕捉，能够快速获取指定区域的图像数据。
- **颜色检测**: 通过 `PIL` 库将捕获的图像转换为可操作的格式，并使用简单的条件判断来检测特定颜色（如红色、黑色和蓝色）。当检测到特定颜色时，程序会模拟按键操作，从而实现自动化的游戏控制。

## 功能
- **选择判定区域**: 程序启动后，用户可以通过鼠标选择需要侦测的区域。🖱️
- **按键控制**: 用户可以通过按下特定的键来开始、暂停或退出程序。
  - 按 `p` 开始检测 🔍
  - 按 `o` 暂停检测 ⏸️
  - 按 `i` 退出程序 ❌

## 注意事项 ⚠️
- 该程序在侦测蓝色时可能存在漏洞，可能会导致误判或漏判。请用户在使用时保持警惕，并根据实际情况进行调整。🔧
- 使用外挂可能会影响游戏体验，并可能导致账号被封禁，请谨慎使用。

## 使用方法
1. 运行程序。🚀
2. 按照提示选择侦测区域。📏
3. 使用指定的按键进行控制。🎹

## 免责声明
使用本程序可能会违反游戏的使用条款，请谨慎使用。⚖️
