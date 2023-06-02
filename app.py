from flask import Flask, render_template, request, redirect

app = Flask(__name__)
students = [
    {'name': 'King', 'math': '62', 'art': '8381', 'other': '100'},
    {'name': 'eden', 'math': '612', 'art': '8128', 'other': '100'},
    {'name': 'jo', 'math': '622', 'art': '828', 'other': '100'},
]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', stud=students)


@app.route('/delete')
def delete():
    name = request.args.get('name')
    for item in students:
        if item['name'] == name:
            students.remove(item)
    return redirect('/admin')


@app.route('/modify', methods=['GET', 'POST'])
def modify():
    if request.method == 'POST':
        name = request.form.get('name')
        math = request.form.get('math')
        art = request.form.get('art')
        other = request.form.get('other')
        for item in students:
            if item['name'] == name:
                item['math'] = math
                item['art'] = art
                item['other'] = other
        return redirect('/admin')
    name = request.args.get('name')
    for item in students:
        if item['name'] == name:
            return render_template('modify.html', student=item)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        math = request.form.get('math')
        art = request.form.get('art')
        other = request.form.get('other')
        print(name, math, art, other)
        students.append({'name': name, 'math': math, 'art': art, 'other': other})
        return redirect('/admin')
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
