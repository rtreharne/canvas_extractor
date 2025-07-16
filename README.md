# 🎓 Canvas Extractor

**Canvas Extractor** is a Python tool for downloading and parsing educational content from Canvas LMS via the REST API. It extracts and serializes key course resources into clean `.json` files for downstream use in semantic search, AI-powered assistants, or content indexing systems like Curricura.

---

## 🔧 Features

- ✅ Extract all course **files** (`.pdf`, `.docx`, `.pptx`) and convert them to plain text
- ✅ Extract **Canvas Pages**, clean the HTML, and preserve inline links
- ✅ Extract **Assignments** and serialize them as-is
- ✅ Saves each resource as a `.json` file in a designated folder
- ✅ Uses `.env` file for secure API configuration

---

## 📁 Output Structure

```
extracted_files/
  ├─ 123456.json       # Text extracted from Lecture1.pdf
extracted_pages/
  ├─ 123456_intro.json # Canvas page content with links preserved
extracted_assignments/
  ├─ 123456_assign.json # Full assignment object
```

---

## 📦 Requirements

```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**
```
requests
python-docx
PyMuPDF
python-pptx
beautifulsoup4
python-dotenv
```

---

## 🗝️ .env Configuration

Create a `.env` file in the root folder:

```
CANVAS_API_URL=https://your.canvas.domain
CANVAS_API_TOKEN=your_canvas_access_token
```

---

## 🚀 Usage

Each extractor is a standalone script. Run them from the command line:

### 🔹 Extract Files
```bash
python extract_canvas_files.py
```

### 🔹 Extract Pages
```bash
python extract_canvas_pages.py
```

### 🔹 Extract Assignments
```bash
python extract_canvas_assignments.py
```

You’ll be prompted to enter the Canvas Course ID.

---

## 🧠 Next Steps

This tool is designed to integrate with vector-based semantic search systems. Suggested follow-up tasks:

- Chunk and embed text using OpenAI or HuggingFace models
- Store embeddings in a vector database (e.g., pgvector, FAISS)
- Implement a semantic search interface for querying course materials

---

## 👤 Author

Built by [Dr. Robert Treharne](mailto:R.Treharne@liverpool.ac.uk), University of Liverpool  
Part of the **Curricura** AI-powered curriculum tools initiative.

---

## 📄 License

MIT License — use freely, modify responsibly.
