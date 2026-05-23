# 🎧 AI Audiobook Engine v1.0

An intelligent AI-powered audiobook generation system that transforms PDF books into emotionally adaptive narrated audio experiences.

---

# 🚀 Features

## 📚 Smart PDF Processing
- Extracts text from PDF books
- Detects story starting point
- Removes front matter noise
- Semantic section splitting

## 🧠 AI Narrative Understanding
- Emotion detection
- AI-generated section titles
- Semantic content chunking
- Dynamic narration flow

## 🎙 Adaptive Audiobook Generation
- Emotion-aware voice selection
- AI narration using Edge TTS
- Multi-section audiobook output
- Interactive audiobook generation

## 💾 Progress Tracking
- Save listening progress
- Resume generation automatically
- Persistent audiobook sessions

## 🎮 Interactive CLI Interface
- Generate intro
- Generate next section
- Generate full audiobook
- Resume progress

---

# 🏗 Project Architecture

```plaintext
PDF
↓
Text Extraction
↓
Story Detection
↓
Semantic Parsing
↓
Emotion Analysis
↓
AI Narration
↓
Audiobook Generation
```

---

# 📂 Project Structure

```plaintext
ai-audiobook/
│
├── app.py
├── audiobook_menu.py
├── audio_director.py
├── book_parser.py
├── emotion.py
├── metadata_detector.py
├── narrator.py
├── pdf_reader.py
├── progress_tracker.py
├── story_detector.py
├── title_generator.py
│
├── books/
├── output/
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repo-link>
cd ai-audiobook
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Place your PDF inside:

```plaintext
books/book.pdf
```

Then run:

```bash
python app.py
```

---

# 🎯 Current Version

## ✅ v1.0 Complete
- Smart PDF parsing
- Emotion-aware narration
- Interactive audiobook generation
- Persistent progress tracking

---

# 🚀 Planned Future Upgrades

- 🎵 Dynamic ambience engine
- 🎭 Character voice system
- 🌐 Web application
- 📱 Mobile interface
- 🧠 AI narrative structure model
- ☁️ Cloud audiobook generation
- ▶️ Built-in audio player

---

# 🛠 Technologies Used

- Python
- Edge TTS
- HuggingFace Transformers
- Sentence Transformers
- PDFPlumber
- Scikit-learn

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Built by Mayur 🚀