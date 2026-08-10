ภาพรวม
สัปดาห์นี้เราจะก้าวข้ามการทำ web scraping แบบพื้นฐาน ไปสู่เทคนิคขั้นสูง ซึ่งรวมถึงการจัดการเนื้อหาเว็บแบบไดนามิก (dynamic web content) และการแนะนำแนวคิดพื้นฐานของ "agentic AI" ในงานอัตโนมัติ นักศึกษาจะได้เรียนรู้การสร้าง scraper ที่แข็งแรงและปรับตัวได้มากขึ้น ซึ่งสามารถทำงานตามคำสั่งจากไฟล์ configuration ได้ เสมือนเป็นการจำลอง autonomous agent

ผลลัพธ์การเรียนรู้ / การประเมินคุณลักษณะ
เชี่ยวชาญเทคนิค web scraping ขั้นสูง โดยเฉพาะเนื้อหาที่ต้องเรนเดอร์ด้วย JavaScript โดยใช้ Selenium
นำ error handling, retry mechanism และกลยุทธ์ anti-blocking ขั้นพื้นฐานมาใช้
ออกแบบและใช้ไฟล์ configuration เพื่อกำหนดพฤติกรรมการ scrape เลียนแบบแนวทาง "agentic"
เข้าใจการจัดโครงสร้างข้อมูลที่ scrape มา และจัดเก็บในรูปแบบต่าง ๆ
วิเคราะห์โครงสร้างหน้าเว็บที่ซับซ้อน และเขียน CSS selector หรือ XPath ที่มีประสิทธิภาพ
เข้าใจความรับผิดชอบด้านจริยธรรมและกฎหมายที่เกี่ยวข้องกับการ scraping แบบอัตโนมัติขั้นสูง
การประเมินคุณลักษณะ: การแก้ปัญหาขั้นสูง, การออกแบบระบบ, วิศวกรรมความแข็งแรงของระบบ (robustness), การจัดการ configuration, การตัดสินใจเชิงจริยธรรมในงานอัตโนมัติ, พื้นฐานความคิดแบบ AI
รายละเอียดเนื้อหาบทเรียน
1. ทบทวนและข้อจำกัดของการ Scraping แบบพื้นฐาน

ทบทวน requests + BeautifulSoup สำหรับ HTML แบบ static
ข้อจำกัด: จะเกิดอะไรขึ้นเมื่อเจอเนื้อหาที่โหลดด้วย JavaScript, infinite scrolling, การคลิกปุ่ม?
2. การ Scrape เนื้อหาไดนามิกด้วย Selenium

แนะนำ Selenium: คืออะไร ทำงานอย่างไร (browser automation), แนวคิด WebDriver
การติดตั้ง: pip install selenium, การดาวน์โหลดและตั้งค่า WebDriver ตามเบราว์เซอร์ (เช่น ChromeDriver, GeckoDriver)
การควบคุมเบราว์เซอร์พื้นฐาน: เปิดเบราว์เซอร์, นำทาง URL (driver.get()), ปิด
การค้นหา Element: find_element(By.ID, "id"), find_element(By.CSS_SELECTOR, "css selector"), find_element(By.XPATH, "xpath")
การโต้ตอบกับ Element: คลิกปุ่ม (.click()), พิมพ์ข้อความ (.send_keys()), ดึงข้อความ (.text)
กลยุทธ์การรอ (Waiting Strategies):
Implicit Waits — timeout แบบทั่วไปสำหรับการค้นหา element
Explicit Waits (WebDriverWait, EC) — รอเงื่อนไขเฉพาะ (เช่น element คลิกได้ มองเห็นได้) สำคัญมากสำหรับเนื้อหาไดนามิก
Headless Browsers: การรันเบราว์เซอร์แบบไม่มี UI เพื่อเพิ่มประสิทธิภาพ (--headless)
3. กลยุทธ์ความแข็งแรงของระบบและการป้องกันการถูกบล็อก

Delays: ใช้ time.sleep() สำหรับการหน่วงพื้นฐาน แต่แนะนำให้ใช้ explicit waits เพื่อความน่าเชื่อถือที่ดีกว่า
User-Agent Spoofing: ตั้งค่า User-Agent แบบกำหนดเองใน Selenium options
Retry Mechanisms พื้นฐาน: ใช้ loop กับ try-except สำหรับข้อผิดพลาดชั่วคราว
IP Rotation (แนวคิด): กล่าวถึง proxy และ VPN โดยสังเขป (ซับซ้อนเกินระดับนี้)
4. การจัดโครงสร้างและการจัดเก็บข้อมูล

กำหนด Python class หรือ dictionary เพื่อแสดงข้อมูลที่ scrape มา (เช่น Product ที่มี name, price, description)
บันทึกข้อมูลที่จัดโครงสร้างแล้วเป็นไฟล์ CSV (ใช้ csv module) และ JSON (ใช้ json module)
5. แนะนำแนวคิดการ Scraping แบบ "Agentic"

Agent คืออะไร? นิยาม: มีเป้าหมาย, รับรู้สภาพแวดล้อม, ดำเนินการ, ปรับตัวได้
Configuration-Driven Agents: จำลองพฤติกรรมแบบ agent โดยกำหนดกฎ (แผน) ในไฟล์ configuration
การกำหนด "กฎ" การ scraping (.json config):
start_url
pagination_selector (CSS/XPath สำหรับปุ่ม/ลิงก์ "หน้าถัดไป")
item_container_selector (selector สำหรับบล็อกสินค้า/บทความหนึ่งรายการ)
item_data_selectors (dictionary ของ selector สำหรับฟิลด์ต่าง ๆ: name_selector, price_selector, description_selector)
Automation Loop: agent (scraper ของคุณ) อ่าน config, นำทาง, ดึงข้อมูล, หาหน้าถัดไป, ทำซ้ำจนไม่มีหน้าเหลือ
6. เจาะลึกจริยธรรมและกฎหมายสำหรับการ Scraping ขั้นสูง

ย้ำเรื่อง robots.txt และ Terms of Service
ความเสี่ยงจากการถูกบล็อก IP, การถูกดำเนินคดี (จดหมาย Cease and Desist)
ความสำคัญของ rate limiting และการ scrape อย่างมีความรับผิดชอบ
เจ้าของเว็บไซต์อาจมองการใช้ Selenium แตกต่างออกไปอย่างไร
ต้นแบบ: Config-Driven Product Scraper Agent
เราจะสร้าง "Agentic Product Scraper" ที่อ่านไฟล์ configuration เพื่อ scrape ข้อมูลสินค้าจากหน้ารายการสินค้าอีคอมเมิร์ซ (สมมติหรือหน้าสาธารณะที่เรียบง่ายมาก) จัดการ pagination และบันทึกข้อมูล

หมายเหตุ: เพื่อการสาธิต เราจะสมมติโครงสร้างเว็บไซต์เป้าหมายแบบง่าย การใช้เว็บไซต์เชิงพาณิชย์ที่ซับซ้อนและใช้งานจริงอาจนำไปสู่การถูกบล็อกหรือปัญหาทางกฎหมาย แนะนำให้ใช้ mock site หรือหน้า directory สาธารณะที่เรียบง่ายมากสำหรับแบบฝึกหัดของนักศึกษา เราจะใช้ example_site_config.json ที่เป็นแนวคิดซึ่งอธิบายโครงสร้างหน้าอีคอมเมิร์ซโดยทั่วไป

เป้าหมายของ Agent:

1.อ่าน configuration ที่เฉพาะเจาะจงกับไซต์
2.นำทางไปยัง URL เริ่มต้น
3.ดึงรายละเอียดสินค้าที่กำหนดไว้ล่วงหน้าจากหน้าปัจจุบัน
4.ค้นหาและคลิกปุ่ม/ลิงก์ "หน้าถัดไป"
5.ทำซ้ำจนไม่พบหน้าเพิ่มเติม หรือถึงขีดจำกัดที่กำหนด
6.บันทึกข้อมูลทั้งหมดที่ดึงมาลงไฟล์ JSON

เนื้อหาสำคัญ
แนวคิดหลักที่สาธิต:

Selenium สำหรับเนื้อหาไดนามิก
การจัดการ WebDriver อัตโนมัติด้วย webdriver_manager
Config-Driven Automation — พฤติกรรมของ scraper กำหนดในไฟล์ JSON ภายนอก
การออกแบบ Agent แบบโมดูล
ความแข็งแรงของระบบ (Robustness)
ข้อมูลที่มีโครงสร้าง
ข้อพิจารณาด้านจริยธรรมและกฎหมาย:

ตรวจสอบ robots.txt เสมอก่อน scrape
อ่าน Terms of Service
Rate Limiting — ใช้ time.sleep() หรือ built-in waits
การใช้ข้อมูล — ระมัดระวังสิทธิ์ทรัพย์สินทางปัญญา
ความชอบด้วยกฎหมาย — แตกต่างกันตามเขตอำนาจศาล โครงการนี้มีไว้เพื่อการศึกษาเท่านั้น
เนื้อหาจาก docs/ETHICS.md (แปล)
แนวทางจริยธรรมและกฎหมายในการ Web Scraping
1. เคารพ robots.txt — ตรวจสอบเสมอก่อน scrape ที่ https://[domain]/robots.txt และปฏิบัติตามกฎ

2. ตรวจสอบ Terms of Service (ToS) — หากไซต์ห้าม scraping ชัดเจน การ scrape ถือเป็นการละเมิดสัญญา อาจนำไปสู่การดำเนินคดี

3. สุภาพ: Rate Limiting และ Delays — หน่วงเวลา 2-5 วินาทีระหว่างการโหลดหน้า หลีกเลี่ยงการส่ง request พร้อมกันจำนวนมาก

4. ระบุตัวตน (User-Agent) — ใส่ User-Agent ที่ระบุตัวตนของ scraper ชัดเจน

5. ไม่ปลอมตัวหรือซ่อนตัวในเชิงจริยธรรม — ควรมีความโปร่งใส หลีกเลี่ยงเจตนาร้าย

6. การใช้ข้อมูลและลิขสิทธิ์ — เนื้อหาที่ scrape มักมีลิขสิทธิ์ ไม่สามารถเผยแพร่ซ้ำโดยไม่ได้รับอนุญาต

7. ข้อบังคับทางกฎหมายและความเสี่ยง — รวมถึงการละเมิดสัญญา, trespass to chattels, การละเมิดลิขสิทธิ์, การละเมิดความเป็นส่วนตัวของข้อมูล

สรุป: ควรปฏิบัติอย่างมีความรับผิดชอบ สุภาพ และถูกกฎหมายเสมอ หากไม่แน่ใจ ควรขออนุญาตจากเจ้าของเว็บไซต์โดยชัดเจน

โครงสร้างโค้ด (สร้างเป็นไฟล์เปล่าไว้ก่อน)
agentic-web-scraper/
├── src/
│   ├── __init__.py          # ทำให้ 'src' เป็น Python package
│   ├── scraper_agent.py     # ตรรกะหลักของ agent (อ่าน config, ควบคุม selenium)
│   ├── config_parser.py     # จัดการการอ่านและตรวจสอบความถูกต้องของ configuration
│   ├── data_models.py       # Python class/dataclass สำหรับข้อมูลที่ scrape (เช่น Product)
│   ├── utils.py              # ฟังก์ชันช่วยเหลือ (เช่น waits, error handling)
│   └── driver_manager.py    # จัดการการตั้งค่า Selenium WebDriver (ใหม่)
├── configs/
│   └── example_site_config.json  # ไฟล์ config JSON สำหรับไซต์เฉพาะ
├── data/
│   └── scraped_products.json     # ข้อมูล output
├── main.py
├── .gitignore
├── README.md



## เริ่มจากตรงนี้
คู่มือการ Setup โปรเจกต์ Agentic Web Scraper ใน VS Code

ขั้นตอนที่ 1: ตรวจสอบและติดตั้งโปรแกรมที่จำเป็น
1.1 ติดตั้ง Python
เปิด Terminal (cmd/PowerShell) แล้วตรวจสอบว่ามี Python หรือยัง:

bash
python --version

Copy

ถ้ายังไม่มี ให้ไปโหลดที่ python.org (แนะนำเวอร์ชัน 3.10+)

สำคัญ: ตอนติดตั้ง ให้ติ๊ก ✅ "Add Python to PATH" ด้วย

1.2 ติดตั้ง VS Code
โหลดได้ที่ code.visualstudio.com (ถ้ามีอยู่แล้วข้ามได้)

1.3 ติดตั้ง Extension ที่จำเป็นใน VS Code
เปิด VS Code → กด Ctrl+Shift+X (Extensions) แล้วค้นหาติดตั้ง:

Python (โดย Microsoft)
Pylance (มักติดมาพร้อม Python extension)
ขั้นตอนที่ 2: สร้างโครงสร้างโปรเจกต์
2.1 สร้างโฟลเดอร์โปรเจกต์
bash
mkdir agentic-web-scraper
cd agentic-web-scraper


2.2 เปิดโฟลเดอร์นี้ใน VS Code
bash
code .


ขั้นตอนที่ 3: สร้าง Virtual Environment (แนะนำอย่างยิ่ง)
การใช้ virtual environment ช่วยแยก dependency ของโปรเจกต์นี้ ไม่ปนกับโปรเจกต์อื่น

เปิด Terminal ใน VS Code (Ctrl+`` `` หรือ Terminal → New Terminal):

bash
python -m venv venv



เปิดใช้งาน venv:

Windows (PowerShell):
powershell
.\venv\Scripts\Activate.ps1



ถ้าเจอ error เรื่อง execution policy ให้รัน:

powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser



macOS/Linux:
bash
source venv/bin/activate



เมื่อ activate สำเร็จ จะเห็น (venv) นำหน้าที่ prompt

เลือก Python Interpreter ให้ VS Code รู้จัก venv:

กด Ctrl+Shift+P
พิมพ์ Python: Select Interpreter
เลือกตัวที่มีคำว่า ./venv/...
ขั้นตอนที่ 4: สร้างโครงสร้างไฟล์/โฟลเดอร์
สร้างโครงสร้างตามนี้ (คลิกขวาใน Explorer panel ของ VS Code → New Folder/New File):

agentic-web-scraper/
├── src/
│   ├── __init__.py
│   ├── scraper_agent.py
│   ├── config_parser.py
│   ├── data_models.py
│   ├── utils.py
│   └── driver_manager.py
├── configs/
│   └── example_site_config.json
├── data/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md



คำสั่งสร้างแบบรวดเร็ว (Terminal):

bash
mkdir src configs data docs
type nul > src\__init__.py
type nul > src\scraper_agent.py
type nul > src\config_parser.py
type nul > src\data_models.py
type nul > src\utils.py
type nul > src\driver_manager.py
type nul > configs\example_site_config.json
type nul > main.py
type nul > requirements.txt
type nul > .gitignore
type nul > README.md



(macOS/Linux ใช้ touch แทน type nul >)

ขั้นตอนที่ 5: สร้างไฟล์ requirements.txt
เปิดไฟล์ requirements.txt แล้วเพิ่ม:

selenium
webdriver-manager



จากนั้นติดตั้ง:

bash
pip install -r requirements.txt



✅ Checkpoint: ตรวจสอบว่าติดตั้งถูกต้อง
ลองสร้างไฟล์ทดสอบ test_setup.py:

python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://books.toscrape.com/")
print("Title:", driver.title)
driver.quit()



รันด้วย:

bash
python test_setup.py



ถ้าเห็น Chrome เปิดขึ้นมา, ไปที่เว็บ, แล้ว print ชื่อหน้าเว็บออกมาใน Terminal = Setup สำเร็จ! 🎉