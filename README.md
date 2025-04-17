# 📝 FastAPI + React To-Do Uygulaması

Bu proje, FastAPI (Python) ve React (JavaScript) teknolojilerini kullanarak geliştirilmiş tam işlemsel bir To-Do uygulamasıdır. Görev ekleme, listeleme, tamamlama ve silme işlemlerini destekler.

## 🚀 Özellikler

- Görev ekleme ve listeleme
- Görev tamamlama (işaretleme)
- Tamamlanan görevleri ayrı listeleme
- Responsive sidebar tasarımı
- Profil menüsü (giriş/çıkış vb. için örnek yapı)
- FastAPI backend + React frontend entegrasyonu

## 💠 Kullanılan Teknolojiler

### Backend (FastAPI)

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

### Frontend (React)

- React.js
- Axios
- Font Awesome (ikonlar için)
- CSS (özelleştirilmiş responsive tasarım)

## 🔧 Kurulum

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Frontend

```bash
cd frontend
npm install
npm start
```

> 📌 React varsayılan olarak `http://localhost:3000`, FastAPI ise `http://localhost:8000` adresinde çalışır.

## 📂 Proje Yapısı

```
📆project-root
 ├ 📆backend
 ┃ ├ main.py
 ┃ ├ crud.py
 ┃ ├ models.py
 ┃ ├ schemas.py
 ┃ ├ database.py
 ┃ └ requirements.txt
 ├ 📆frontend
 ┃ ├ public/
 ┃ ├ src/
 ┃ ┃ ├ components/
 ┃ ┃ │ ├ AddTodo.jsx
 ┃ ┃ │ ├ TodoList.jsx
 ┃ ┃ │ ├ CompletedList.jsx
 ┃ ┃ │ └ ProfileMenu.jsx
 ┃ ┃ ├ layout/
 ┃ ┃ │ └ Sidebar.jsx
 ┃ ┃ ├ App.jsx
 ┃ ┃ └ style.css
 ┃ └ package.json
 └ README.md
```

---

## ✅ Lisans

MIT License
