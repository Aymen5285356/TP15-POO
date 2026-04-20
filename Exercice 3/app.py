from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route('/', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            error = "Tous les champs sont obligatoires."
            return render_template('add.html', error=error)

        contacts.append({'name': name, 'email': email})
        return redirect(url_for('list_contacts'))

    return render_template('add.html')

@app.route('/contacts')
def list_contacts():
    return render_template('contacts.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)