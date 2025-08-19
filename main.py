import requests
from datetime import datetime, timedelta
import time

# --- Config ---
TOKEN = "8343725186:AAEiecB-HbepEyy4ySt-B8dsjqiyLRKBypM"
CHAT_ID = "6028322101"
START_DATE = datetime(2025, 8, 15)

def send_message():
    today = datetime.now()
    day_count = (today - START_DATE).days + 1

    weekdays = {
        0: "Thứ Hai", 1: "Thứ Ba", 2: "Thứ Tư",
        3: "Thứ Năm", 4: "Thứ Sáu", 5: "Thứ Bảy", 6: "Chủ nhật"
    }
    weekday = weekdays[today.weekday()]
    date_str = today.strftime("%d/%m/%Y")

    text = f"Hôm nay là {weekday} ngày {date_str}, ngày {day_count}/365 ngày thành Đấng 🐗🔥💪🚀"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

# --- Loop chờ tới 0:00 hàng ngày ---
while True:
    now = datetime.now()
    next_run = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    sleep_time = (next_run - now).total_seconds()

    print(f"Sleeping {sleep_time/3600:.2f} hours until next run...")
    time.sleep(sleep_time)
    send_message()
