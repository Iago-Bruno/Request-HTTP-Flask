import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def redirectToFormResponse():
    form = 'none'
    return redirect(url_for('formResponse', form=form))

@app.route("/formResponse/<string:form>", methods=['GET', 'POST'])
def formResponse(form):
    if(form != 'none'):
        form = form.replace("\'", "\"")
        form = json.loads(form)

    return render_template('formResponse.html', form=form)

@app.route("/formPage", methods=['GET', 'POST'])
def formPage():
    request_method = request.method

    if(request_method == 'POST'):
        formData = {
            "produto#1": request.form["produto#1"],
            "produto#2": request.form["produto#2"],
            "produto#3": request.form["produto#3"],
            "quantidade#1": request.form["quantidade#1"],
            "quantidade#2": request.form["quantidade#2"],
            "quantidade#3": request.form["quantidade#3"]
        }
        
        return redirect(url_for('formResponse', form=formData))

    return render_template('formPage.html')

if __name__ == "__main__":
    app.run(debug=True)
