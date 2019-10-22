from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.giphy.com/media/9JlK8kbLeEr6NuKfOS/giphy.gif",
    "https://media.giphy.com/media/eHS3j2AOp6pQyBTjPT/giphy.gif",
    "https://media.giphy.com/media/JR27sjYKB0GeEVtzQE/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
