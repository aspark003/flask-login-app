from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def personnel_form():
    if request.method == 'POST':
        try:

            id = request.form.get('id')
            if id.isdigit():
                id = int(id)
            else:
                id = None

            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            gender = request.form.get('gender')
            age = request.form.get('age')
            if age.isdigit():
                age = int(age)
            else:
                age = None

            email = request.form.get('email')
            phone = request.form.get('phone')

            return (
                f"ID: {id}<br>"
                f"First Name: {first_name}<br>"
                f"Last Name: {last_name}<br>"
                f"Gender: {gender}<br>"
                f"Age: {age}<br>"
                f"Email: {email}<br>"
            f"Phone: {phone}<br>"
            )
        except ValueError:
            return ("Error")

    return render_template("personnel_form.html")  # Render the form if it's not a POST request

if __name__ == '__main__':
    app.run(debug=True, port=5000)


