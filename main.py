from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/year', methods=["GET", "POST"])
def year():
    if request.method == "POST":
        idade = 100 - int(request.form['idade'])
        return render_template("result.html", anos=idade)
    return render_template("100.html")


if __name__ == '__main__':
    app.run(debug=True)

