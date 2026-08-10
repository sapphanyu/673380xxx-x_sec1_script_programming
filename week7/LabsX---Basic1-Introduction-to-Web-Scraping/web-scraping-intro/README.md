# Lab: การแนะนำ Web Scraping ด้วย Python

## 🎯 วัตถุประสงค์การเรียนรู้

หลังจากทำ Lab นี้เสร็จ นักศึกษาจะสามารถ:
- เข้าใจแนวคิดพื้นฐานของ Web Scraping และข้อพิจารณาด้านจริยธรรม/กฎหมาย
- ใช้ไลบรารี `requests` เพื่อดาวน์โหลดเนื้อหาเว็บเพจ
- ใช้ไลบรารี `BeautifulSoup4` เพื่อแปลง (parse) และดึงข้อมูลจาก HTML
- เขียนสคริปต์ scraper พื้นฐานที่ดึงข้อมูลจากเว็บไซต์จริง
- แก้ปัญหา (debug) ที่พบทั่วไปในการทำ web scraping

## ⚠️ ข้อพิจารณาด้านจริยธรรมและกฎหมาย (อ่านก่อนเริ่ม)

ก่อนทำ scraping เว็บไซต์ใดๆ ต้องตรวจสอบเสมอ:

1. **robots.txt** — ไฟล์ที่ระบุว่าเว็บไซต์อนุญาตให้ bot เข้าถึงส่วนใดได้บ้าง
   ตรวจสอบได้ที่ `https://[ชื่อเว็บไซต์]/robots.txt`
2. **Terms of Service (ข้อกำหนดการให้บริการ)** — บางเว็บไซต์ห้าม scraping โดยชัดแจ้ง
3. **Rate Limiting** — ไม่ควรส่ง requests รัวๆ จนเป็นภาระต่อเซิร์ฟเวอร์
4. **ทรัพย์สินทางปัญญา** — ข้อมูลที่ scrape มาอาจมีลิขสิทธิ์ ห้ามนำไปใช้ในทางละเมิด

> ในเว็บไซต์ที่มี API ให้ใช้งาน **ควรใช้ API แทนการ scrape เสมอ** เพราะเสถียรกว่าและถูกต้องตามกฎกว่า

Lab นี้ใช้เว็บไซต์ [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) 
ซึ่งเป็นเว็บไซต์เพื่อการศึกษาและอนุญาตให้เข้าถึงเนื้อหาได้แบบเปิด เหมาะสำหรับการฝึกฝนโดยไม่มีปัญหาด้านจริยธรรม

---

## เริ่มทำตั้งแต่ตรงนี้ ใครที่มี github desktop และ vscode ที่มี python สามารถข้าม Prerequisites (สิ่งที่ต้องมีก่อนเริ่ม) ได้

## 🛠️ Prerequisites (สิ่งที่ต้องมีก่อนเริ่ม)

- Python 3.8 หรือสูงกว่า ([ดาวน์โหลด](https://www.python.org/downloads/))
- Git ([ดาวน์โหลด](https://git-scm.com/downloads))
- Text Editor เช่น VS Code

ตรวจสอบเวอร์ชัน Python:
```bash
python --version

## เปิด repo อันเก่ามาทำต่อ สร้างโฟลเดอร์ week 7

📦 ขั้นตอนการ Setup
1. Clone หรือสร้างโปรเจกต์
bash
git clone https://github.com/[YOUR_USERNAME]/web-scraping-intro.git
cd web-scraping-intro


2. สร้าง Virtual Environment
การใช้ virtual environment ช่วยแยก dependencies ของโปรเจกต์นี้ออกจากโปรเจกต์อื่นในเครื่อง

Windows (PowerShell):
powershell
python -m venv venv
venv\Scripts\Activate.ps1


⚠️ หากเจอ error:

... cannot be loaded because running scripts is disabled on this system


ให้เปิด PowerShell แบบ Run as Administrator แล้วรัน (แนะนำให้เปิดก่อนรัน venv\Scripts\Activate.ps1 ทุกครั้ง เพื่อความสะดวกและไม่ error):

powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
พิมพ์ Y ยืนยัน แล้วเปิด PowerShell ใหม่และลอง activate อีกครั้ง

macOS / Linux:
bash
python3 -m venv venv
source venv/bin/activate


เมื่อ activate สำเร็จ จะเห็น (venv) ปรากฏหน้า prompt


3. ติดตั้ง Dependencies
bash
pip install requests beautifulsoup4


ตรวจสอบว่าติดตั้งสำเร็จ:

bash
pip list


ควรเห็น requests และ beautifulsoup4 ในรายการ

4. โครงสร้างไฟล์ที่ต้องมี (สร้างเป็นไฟล์เปล่าไว้ก่อน)
web-scraping-intro/
├── src/
│   ├── __init__.py
│   └── scraper.py
├── main.py
├── .gitignore
└── README.md