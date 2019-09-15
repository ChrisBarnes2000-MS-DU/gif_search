from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

apikey = "RXN4HC41NO0K"
limit = 10


@app.route('/')
def index():
    """Show the homepage."""
    # TODO: Extract the query term from url using request.args.get()
    search = request.args.get('search')

    # TODO: Make 'params' dictionary containing:
    params = {
        # a) the query term, 'q'
        "q": search,
        # b) your API key, 'key'
        "apikey": "RXN4HC41NO0K",
        # c) how many GIFs to return, 'limit'
        "limit": 10
    }
    button_request = request.args.get('button')

    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    #base_url = f"https://api.tenor.com/v1/search?q={search}&key={apikey}&limit={lmt}"
    #r = requests.get(base_url)
    r = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    if button_request == "random":
        params["q"] = "random"
        r = requests.get("https://api.tenor.com/v1/random?",
                         params)

    if button_request == "trending":
        params["q"] = "trending"
        r = requests.get("https://api.tenor.com/v1/trending?", params)

    print(r.status_code)

    gifs = json.loads(r.content)['results']

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'
    return render_template('index.html', gifs=gifs)


if __name__ == "__main__":
    app.run(debug=True)
