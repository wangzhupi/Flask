from flask import Flask, url_for, render_template

app = Flask(__name__)

# 加入姓名和电影名称
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



@app.route('/') #直接进到页面
def index():
    # 基础欢迎界面
    return render_template('index.html',name=name,movies=movies)

@app.route('/login') # 登录路由
def login():
    # 处理登录逻辑...
    return "This is the login page"
