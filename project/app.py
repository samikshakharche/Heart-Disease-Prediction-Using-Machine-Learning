from flask import Flask, render_template, request
from prediction import prediction
app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route('/predict',methods = ['POST'])
def predict(): 
    return render_template("index.html",res = prediction(request.form.get("age"),request.form.get("sex"),request.form.get("cp"),request.form.get("trestbps"),request.form.get("chol"),request.form.get("fbs"),request.form.get("restecg"),request.form.get("thalach"),request.form.get("exang"),request.form.get("oldpeak"),request.form.get("slope"),request.form.get("ca"),request.form.get("thal"))
)


if __name__ == "__main__":
	app.run()
