from flask import Flask, render_template, request, url_for

app3 = Flask(__name__)

# Route for the login page
@app3.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # ✅ Just show the email for now — real validation can be added later
        return f"Logged in as: {email}"

    # Show the login page
    return render_template('login.html')

# Run the app and allow access from other devices (host='0.0.0.0')
if __name__ == '__main__':
    app3.run(debug=True, host='0.0.0.0', port=5002)
