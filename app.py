from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/') #直接进到页面
def index():
    # 基础欢迎界面
    return render_template('index.html',message="Hello world")

@app.route('/login') # 登录路由
def login():
    # 处理登录逻辑...
    return "This is the login page"

# if __name__ == '__main__':
#     app.run()