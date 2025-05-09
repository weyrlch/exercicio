from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/year', methods=["GET", "POST"])
def year():
    if request.method == "POST":
        idade = 100 - int(request.form['idade'])
        return render_template("result100.html", anos=idade)
    return render_template("100.html")

@app.route('/double', methods=["GET", "POST"])
def double():
    if request.method == "POST":
        num = int(request.form['number'])
        rdouble = 2 * int(request.form['number'])
        return render_template("resultdouble.html", number=rdouble, num=num)
    return render_template("double.html")

@app.route('/hobbies', methods=["GET", "POST"])
def hobbies():
    if request.method == "POST":
        nome = request.form['name'].strip()
        hobbies = [request.form.get(f"hobby{i}", "").strip() for i in range(1, 4) if request.form.get(f"hobby{i}", "").strip()]
        return render_template("yourshobbies.html", hobbies=hobbies, nome=nome)
    return render_template("hobbies.html")



if __name__ == '__main__':
    app.run(debug=True)

