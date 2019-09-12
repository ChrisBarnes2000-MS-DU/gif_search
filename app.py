from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

apikey = ""
lmt = 10


@app.route('/')
def index():
    """Show the homepage."""
    search = request.args.get('search')
    base_url = f"https://api.tenor.com/v1/search?q={search}&key={apikey}&limit={lmt}"
    r = requests.get(base_url)

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(r.content)
        print(top_10gifs)
    else:
        top_10gifs = None

    return render_template('index.html', gif=r)


if __name__ == "__main__":
    app.run(debug=True)
