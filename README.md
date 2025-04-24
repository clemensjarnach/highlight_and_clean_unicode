# 🕵️‍♂️ Hidden Unicode Cleaner

A Python script to **detect**, **highlight**, and **clean invisible Unicode characters** (e.g. zero-width spaces, non-breaking spaces) from text files.

---

## 📌 What is this?

This utility scans plain-text files for **non-printable or invisible Unicode characters** that can cause subtle issues in data processing, text rendering, or string comparison. It identifies characters like:

- `U+00A0` – Non-breaking space
- `U+200B` – Zero-width space
- `U+200C` – Zero-width non-joiner
- `U+200D` – Zero-width joiner
- `U+FEFF` – Byte Order Mark (BOM)

It then:
- Highlights their presence in the console (with line/column info),
- Replaces problematic "space-like" characters with standard spaces,
- Removes others entirely,
- And writes a cleaned version of the file.

---

## 👥 Who is this for?

- **Developers** handling inconsistent text inputs from APIs, UIs, or third-party services.
- **Data scientists** cleaning messy inputs from surveys, user submissions, or web scraping.
- **Researchers** preparing text for NLP or corpus analysis.
- **Writers or editors** seeing weird spacing in documents from copy-paste operations.

---

## 💡 Why is this useful?

Invisible Unicode characters frequently sneak into:

- **User input** (especially from mobile or copy-paste from Word/Google Docs)
- **AI-generated text**
- **JSON / CSV data from APIs or databases**
- **Text copied from websites or PDFs**

These characters can:
- Break string comparisons or tokenisation
- Cause subtle layout bugs in UI rendering
- Disrupt search/indexing in databases
- Confuse NLP tools

This tool makes them **visible** and then **cleans them up** — safely and reproducibly.

---

## 🚀 Usage

```bash
python3 highlight_and_clean_unicode.py path/to/yourfile.txt
```

It will output a cleaned version to:

```bash
yourfile.txt.cleaned.txt
```

---

## 📝 License

MIT — free to use, modify, and distribute.

---

## 📬 Feedback or contributions?

PRs and issues welcome!

