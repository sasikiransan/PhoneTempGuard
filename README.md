# 📱 PhoneTempGuard - Phone Battery Temperature Notifier 🔥

This project monitors your Android phone's battery temperature via USB using ADB and shows desktop notifications when it gets too hot. Ideal for USB tethering and charging sessions.

---

## ✅ Features

- Monitors phone temperature every 10 minutes
- Shows desktop notifications if temp ≥ 38°C
- Works silently in background
- Auto-starts with Windows (optional)

---

## 🧰 Requirements

### 🔧 On Your PC:
- Python 3 installed
- ADB installed and added to PATH
- `plyer` Python package

```bash
pip install plyer
```

---

## 📱 On Your Android Phone:

1. Enable **Developer Options**
   - Go to Settings → About Phone → Tap **Build Number** 7 times

2. Enable **USB Debugging**
   - Settings → Developer Options → Turn on **USB Debugging**

3. When prompted on USB connection:  
   - Choose “**File Transfer**” or “**USB Tethering**”  
   - Allow USB debugging when asked  
   - (Optional) You can select “Allow this computer always”

---

## 🚀 How to Use

1. Download and extract this project zip
2. Open a terminal in the project folder
3. Run the script manually with:

```bash
python phone_temp_alert.py
```

or double-click the `.bat` file

---

## 🖥️ Auto-Start on Windows (Optional)

1. Press `Win + R` → type `shell:startup`
2. Copy `start_temp_alert.bat` into that folder

✅ Now it auto-starts with Windows

---

## 🧪 Test ADB Connection

```bash
adb devices
```

✅ You should see your phone listed. If not:
- Try reconnecting USB
- Change cable
- Make sure debugging is enabled

---

## 🧹 To Stop Monitoring

- Press `Ctrl + C` in terminal  
- Or delete the `.bat` file from `shell:startup` folder

---

Made with ❤️ by Sasi Senpai
