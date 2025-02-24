# Wikipedia Summarizer Flask App

This Flask app allows users to search for Wikipedia articles, scrape the content, and generate a concise summary using OpenAI's GPT model.

## Features

- Search Wikipedia using Google Custom Search API  
- Scrape Wikipedia content with BeautifulSoup  
- Summarize articles using OpenAI's GPT  
- Simple Flask web UI  

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/wikipedia-summarizer.git
cd wikipedia-summarizer
```

### Step 2: Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## API Keys Setup

This app requires three API keys:

- **Google Custom Search API Key**
- **Google Custom Search Engine ID (CX ID)**
- **OpenAI API Key**

### Step 1: Get Google API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the **Custom Search JSON API**.
3. Click **"Credentials"** → **"Create API Key"**.
4. Copy your API key.

### Step 2: Get Google Custom Search Engine (CX ID)

1. Go to [Google Programmable Search](https://programmablesearchengine.google.com/)
2. Click **"New Search Engine"**.
3. Set **Sites to Search** as `wikipedia.org`.
4. Click **"Create"** → Copy the **CX ID** from the Control Panel.

### Step 3: Get OpenAI API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/signup/)
2. Create an account (if you don’t have one).
3. Go to [API Keys](https://platform.openai.com/api-keys)
4. Click **"Create API Key"** and copy it.
5. OpenAI requires a billing setup. **Ensure you add credits** to your OpenAI account.


## Setting Up the `.env` File

Create a `.env` file in the root directory and add your API keys:

```
GOOGLE_API_KEY=your-google-api-key
SEARCH_ENGINE_ID=your-cx-id 
OPENAI_API_KEY=your-openai-api-key
```

Flask will automatically load these values when the app runs.



## Runnin the Flask App
### Step 1: Activate Virtual Environment
```bash
source venv/bin/activate
```
### Step 2: Run the Flask App
```bash
python3 app.py
```
### Step 3: Open in Browser
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Example Usage

1. Enter a search term (e.g., **"Bill Gates"**).
2. Click **"Search"** → The app fetches the best Wikipedia article.
3. View the summary → The scraped content is summarized with OpenAI.

---

## Troubleshooting

### Issue: "The view function for 'index' did not return a valid response."
Ensure `app.py` returns a response for all routes.

### Issue: "API key invalid or missing"
Double-check your `.env` file and ensure Flask loads it.

### Issue: OpenAI API not working
Ensure your OpenAI account has funds (OpenAI requires a billing setup).

---

## Author

Developed by [Martik Aghajanian](www.linkedin.com/in/martik-aghajanian)

Feel free to contribute or reach out for any questions.

