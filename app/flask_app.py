from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        if request.form['action'] == 'Generate':
            # Perform action on Generate button click (send POST request)
            # Replace 'some_url' with the actual URL where you want to send the request
            # Example: requests.post('http://example.com', data={'text': request.form['text']})
            return redirect(url_for('index'))
        elif request.form['action'] == 'Clear':
            # Perform action on Clear button click (clear text area)
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
