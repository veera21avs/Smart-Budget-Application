from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect("budget.db")
    cursor = conn.cursor()

    cursor.execute("SELECT total_amount, daily_budget FROM budgets ORDER BY id DESC LIMIT 1")
    budget = cursor.fetchone()

    conn.close()

    total_amount = budget[0] if budget else 0
    daily_budget = budget[1] if budget else 0

    return render_template('dashboard.html', total_amount=total_amount, daily_budget=daily_budget)

@app.route('/register', methods=['POST'])
def register():

    fullname = request.form['fullname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("budget.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(fullname,email,username,password)
    VALUES(?,?,?,?)
    """, (fullname, email, username, password))

    conn.commit()
    conn.close()

    return redirect('/dashboard')


@app.route('/save_budget', methods=['POST'])
def save_budget():

    total_amount = request.form['totalAmount']
    daily_budget = request.form['dailyBudget']

    conn = sqlite3.connect("budget.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO budgets(total_amount,daily_budget)
    VALUES(?,?)
    """, (total_amount, daily_budget))

    conn.commit()
    conn.close()

    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)