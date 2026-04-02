# KIT-8137: Buddhadasa Indapanno E-Books Finder
### (IIIF-Like Viewer Experiment)

โครงการทดลองระบบค้นหาและแสดงผลหนังสืออิเล็กทรอนิกส์ (E-Book) ของท่านพุทธทาสภิกขุ โดยใช้เทคโนโลยีการแสดงผลภาพความละเอียดสูงแบบ Tile-based Rendering ซึ่งช่วยให้การซูมอ่านเนื้อหาจากไฟล์ภาพขนาดใหญ่ทำได้อย่างรวดเร็วและลื่นไหล

---

## 🇹🇭 ภาษาไทย

### รายละเอียดโครงการ
โปรเจกต์นี้ถูกสร้างขึ้นเพื่อทดสอบการนำแนวคิด **IIIF (International Image Interoperability Framework)** มาประยุกต์ใช้ในการเผยแผ่ธรรมะในรูปแบบดิจิทัล โดยเน้นที่ความรวดเร็วในการเข้าถึงเนื้อหา (Performance) และประสบการณ์การใช้งานที่ดี (User Experience) ผ่านหน้าเว็บเบราว์เซอร์

### คุณสมบัติหลัก
- **High-Resolution Viewer**: ใช้ **OpenSeadragon** ร่วมกับ **Leaflet.js** เพื่อให้ผู้ใช้สามารถซูมดูรายละเอียดตัวอักษรได้ชัดเจนโดยไม่ต้องโหลดภาพทั้งไฟล์
- **Smart Search**: ระบบค้นหาที่รองรับทั้งรหัสหนังสือ (เช่น T01, DK001) และชื่อตอน ผ่านตัวเลือก Select2 ที่ใช้งานง่าย
- **Direct PDF Link**: เชื่อมโยงไปยังไฟล์ PDF ต้นฉบับเพื่อการดาวน์โหลดหรืออ่านแบบออฟไลน์
- **Metadata Driven**: จัดการข้อมูลทั้งหมดผ่านไฟล์ `meta.js` ทำให้ง่ายต่อการแก้ไขและเพิ่มรายการหนังสือใหม่

### โครงสร้างไฟล์
- `index.html`: ส่วนการแสดงผลหลัก (Frontend) และการจัดการเหตุการณ์ต่างๆ
- `meta.js`: ฐานข้อมูล JSON ที่เก็บรายชื่อหนังสือ, รหัสอ้างอิง และลิงก์ไฟล์
- `assets/`: รวมไลบรารีที่จำเป็น (Leaflet, OpenSeadragon, jQuery, Select2)
- `make-tile.py`: สคริปต์ Python สำหรับแปลงภาพต้นฉบับให้เป็น Deep Zoom Tiles (DZI)

### วิธีการติดตั้งและใช้งาน
1. คัดลอกโฟลเดอร์โครงการไปยัง Web Server หรือใช้งานผ่าน Local Server
2. เตรียมภาพหนังสือและใช้ `make-tile.py` ในการประมวลผลภาพ
3. แก้ไข `meta.js` เพื่อกำหนดเส้นทางภาพ (`iaurl`) และไฟล์ PDF (`iapdf`) ให้ตรงกับตำแหน่งจัดเก็บไฟล์ข้อมูล

---

## 🇺🇸 English

### Project Overview
An experimental platform designed for searching and viewing the e-books of Buddhadasa Indapanno. It utilizes **Tile-based Rendering** (similar to IIIF standards) to ensure high-performance viewing of high-resolution digitized manuscripts and books.

### Key Features
- **Deep Zoom Capability**: Powered by **OpenSeadragon**, allowing users to zoom into high-quality images without high bandwidth consumption.
- **Enhanced Navigation**: Uses **Leaflet.js** for coordinate and layer management, providing a map-like navigation experience for book pages.
- **Efficient Search**: Integrated **Select2** search engine for quick access via Book ID or Title.
- **Responsive & Lightweight**: Designed to work seamlessly across both desktop and mobile devices.

### File Components
- `index.html`: The main interface and viewer logic.
- `meta.js`: The central metadata repository for book mapping and file paths.
- `assets/`: Contains local dependencies (Leaflet, OpenSeadragon, jQuery, Select2).
- `make-tile.py`: A utility script to convert standard images into zoomable tiles.

### Setup
1. Deploy the project files to your web server.
2. Process your high-res images using the provided `make-tile.py`.
3. Update the `iaurl` and `iapdf` constants in `meta.js` to point to your image and PDF storage.

---

**หมายเหตุ (Note):** โครงการนี้เป็นเพียงการทดลองเชิงเทคนิคเพื่อการศึกษาและการเผยแผ่ธรรมะ ข้อมูลและลิขสิทธิ์เนื้อหาทั้งหมดเป็นของหอจดหมายเหตุพุทธทาส อินทปัญโญ
(This project is a technical experiment for educational and Dhamma dissemination purposes. All content rights belong to the Buddhadasa Indapanno Archives.)
