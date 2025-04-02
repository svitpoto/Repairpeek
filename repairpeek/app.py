from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    tickets = [
        {
            "title": "Zamenjava trdega diska",
            "status": "V teku",
            "messages": [
                "Kdaj bo končano?",
                "Napaka pri zagonu je še vedno prisotna."
            ]
        },
        {
            "title": "Namestitev sistema Windows",
            "status": "Zaključeno",
            "messages": [
                "Deluje, hvala!"
            ]
        }
    ]
    return render_template('dashboard.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
