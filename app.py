from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 基础欢迎界面
    return render_template('index.html',message="Hello world")


if __name__ == '__main__':
    app.run()