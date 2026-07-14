# ResearchMate AI 📄

AI-powered research paper analysis system using OpenAI GPT-4o and Streamlit.

## Features ⚡

- **PDF Upload & Processing** - Load research papers instantly
- **Quick Summaries** - 2-3 second paper summaries with OpenAI
- **Paper Comparison** - Compare 2+ papers with AI analysis
- **Q&A Interface** - Ask questions about your papers
- **Professional UI** - Clean, modern Streamlit interface
- **OpenAI Powered** - Uses latest GPT-4o model

## Installation 🚀

### 1. Clone/Download
```bash
cd ResearchMate-AI
```

### 2. Create .env file
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-proj-your_actual_key_here
```

### 3. Install dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt
```

### 4. Run
```bash
streamlit run app.py
```

App opens at: http://localhost:8501

## Usage 📖

1. **Dashboard** - Overview and info
2. **Upload Papers** - Add your PDF files
3. **Summaries** - Generate quick paper summaries
4. **Comparison** - Compare 2+ papers
5. **Chat** - Ask questions about papers
6. **Settings** - Configure model & parameters

## Configuration ⚙️

Edit `.env` file to change:
- `OPENAI_API_KEY` - Your OpenAI API key
- `PRIMARY_MODEL` - Default: gpt-3.5-turbo
- `TEMPERATURE` - Default: 0.3
- `MAX_TOKENS` - Default: 2048

## Requirements 📋

- Python 3.8+
- OpenAI API key
- 4GB RAM minimum

## File Structure 📁

```
ResearchMate-AI/
├── app.py                 # Main application
├── src/
│   ├── config.py         # Settings
│   ├── models.py         # Data models
│   ├── llm.py           # OpenAI integration
│   └── pdf_loader.py    # PDF processing
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
└── README.md             # This file
```

## Troubleshooting 🔧

### Slow Performance
- Use `gpt-3.5-turbo` instead of `gpt-4o`
- Reduce `MAX_TOKENS` in .env

### API Key Issues
- Verify key in `.env` file
- Check OpenAI account has credits
- Try creating new API key

### PDF Upload Fails
- Ensure PDF file is valid
- Check file size < 50MB
- Try different PDF

## Support 💬

- Check `.env` configuration first
- Verify OpenAI API key works
- Review settings in Settings page

## License 📄

MIT License - Feel free to use and modify!

---

**Powered by OpenAI GPT-4o** ⚡
**Built with Streamlit** 🎨
