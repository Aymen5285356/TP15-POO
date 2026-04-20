from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            celsius = float(request.form.get('celsius'))
            fahrenheit = (celsius * 9/5) + 32
            return render_template('result.html', c=celsius, f=fahrenheit)
        except:
            error = "Veuillez entrer un nombre valide."
            return render_template('index.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)