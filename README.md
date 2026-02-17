# NCO 2015 Semantic Search Engine 🔍

This project is an end-to-end **Semantic Search Application** built using the **National Classification of Occupations (NCO) 2015 PDF dataset**.

The system extracts occupation records from a large PDF document, generates meaningful text descriptions, converts them into embeddings, stores them in a FAISS vector database, and provides a semantic search API using FastAPI. A simple HTML + JavaScript frontend is used to query the API.

---

## 📌 Features

- Extracts text from NCO 2015 PDF (1486 pages)
- Cleans and structures extracted data into occupation records
- Generates template-based occupation descriptions (no Ollama required)
- Creates embeddings using `sentence-transformers`
- Stores vectors in FAISS for fast similarity search
- FastAPI backend with semantic search endpoint
- HTML + JS frontend for user-friendly searching
- Returns top-k most relevant occupations with similarity scores

---

## 🛠 Tech Stack

### Backend / ML
- Python 3.12
- FastAPI
- FAISS (Vector Store)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Pandas, NumPy
- PDFPlumber / PDFMiner

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📂 Project Structure


NCO_semantic_search/
│
├── backend/
│ ├── main.py
│ ├── search.py
│ └── ...
│
├── notebooks/
│ ├── pdf_extraction.ipynb
│ ├── data_cleaning.ipynb
│ ├── embedding_generation.ipynb
│ └── ...
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── data/
│ ├── occupations.csv
│ └── ...
│
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/NCO_semantic_search.git
cd NCO_semantic_search

python -m venv venv
venv\Scripts\activate


pip install -r requirements.txt


🧠 Data Extraction + Embedding Workflow
Step 1: Extract PDF text

Extracted all pages using pdfplumber

Stored page-wise text into a dataframe

Step 2: Find occupation records

Used regex to detect occupation codes

Extracted structured occupation entries

Total extracted occupation records: 3599

After removing duplicates: 3598

Step 3: Generate descriptions

Instead of using LLM (Ollama), we generated template descriptions like:

Occupation Title: Electrician, General.
NCO 2015 Code: 7411.0100.
Equivalent NCO 2004 Code: 7411.10.
This occupation belongs to the National Classification of Occupations (NCO) 2015 dataset.

Step 4: Create embeddings + FAISS index

Used sentence-transformers/all-MiniLM-L6-v2
Stored embeddings in FAISS vector index




🚀 Running the Backend (FastAPI)

From the project root:
python -m uvicorn backend.main:app --host 127.0.0.1 --port 9000 --reload

Backend runs at:
http://127.0.0.1:9000


🌐 Running the Frontend (HTML + JS)

frontend/index.html
Double click and open in browser.

Then type any query like:

electrician

teacher

engineer

doctor

and press Search.

🔎 Example Output

Query: electrician

Top Results:

Electrician, General

Helper Electrician

Electrical Supervisor, Wiring

Electrician, Aircraft

📌 Future Improvements

Add advanced filtering (Division/Group/Family)

Add exact search + hybrid search

Improve UI using Bootstrap / Tailwind

Deploy backend to Render / Railway

Host frontend using GitHub Pages

