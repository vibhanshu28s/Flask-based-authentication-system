from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user for demonstration
users = {"admin": "admin"}

@app.route("/")
def home():
    return """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: Arial;">
        <h1>Welcome!</h1>
        <p>Please sign in to continue.</p>
        <a href="/login">
            <button style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 5px;">
                Go to Login
            </button>
        </a>
    </div>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            return f"Hello, {username}! You are logged in."
        else:
            return "Invalid credentials, please try again."
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
