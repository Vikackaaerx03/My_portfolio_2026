from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Маршруты для всех 8 страниц
@app.route('/education.html')
def education():
    return render_template('pages/education.html')

@app.route('/courses.html')
def courses():
    return render_template('pages/courses.html')

@app.route('/commercial.html')
def commercial():
    return render_template('pages/commercial.html')

@app.route('/my-projects.html')
def my_projects():
    return render_template('pages/my-projects.html')

@app.route('/python.html')
def python_page():
    return render_template('pages/python.html')

@app.route('/cpp-csharp.html')
def cpp_csharp():
    return render_template('pages/cpp-csharp.html')

@app.route('/web-dev.html')
def web_dev():
    return render_template('pages/web-dev.html')

@app.route('/others.html')
def others():
    return render_template('pages/others.html')

if __name__ == '__main__':
    app.run(debug=True)
