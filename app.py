from flask import Flask, render_template, request
from services.google_search import google_search_wikipedia
from services.summarizer import summarize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	print("Request method:", request.method)
	if request.method == "POST":
		search_query = request.form.get("search")
		print(search_query)
		wiki_url = google_search_wikipedia(search_query)
		if not wiki_url:
			return render_template("result.html", error="No Wikipedia page found.")

		summary = summarize(wiki_url)
		
		return render_template("result.html", 
							   wiki_url=wiki_url,
							   summary=summary)
	return render_template("index.html")

if __name__ == "__main__":      
	app.run(debug=True)
