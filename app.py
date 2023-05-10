from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
# from dateutil import parser



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
db = SQLAlchemy(app)

app.app_context().push()


def format_time(forms):
    elapsed_time = []
    s='s'
    for form in forms:
        
        i = (datetime.datetime.now() - form.timestamp)
        i = i.total_seconds()
        print(i)
        print(type(i))
        
        if i>86400:
            et = int(i/86400)
            et_type = 'day'
        elif i>3600:
            et = int(i/3600)
            et_type='hour'
        elif i>60:
            et=int(i/60)
            et_type = 'minute'
        else:
            et = i
            et_type = 'second'
        if et==1:
            s=""
        elapsed_time.append(str(et)+" "+str(et_type)+s+" ago.")
    return(elapsed_time)
# class User(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
#     # email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username
    
class Form(db.Model):
    

    title = db.Column(db.String(100),primary_key=True,nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    technical_tags = db.Column(db.String(1000))
    business_tags = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime,default=datetime.datetime.now)
    def __repr__(self):
        return '<User %r>' % self.title
    
@app.route("/home")
def index():

    return(render_template("index.html",Posts=Form.query.all(),elapsed_time = format_time(Form.query.all())))


@app.route("/post",methods=['GET','POST'])
def post():
    if request.method=='POST':
        title = request.form.get("project-title")
        description = request.form.get("description")
        technical_tags = request.form.get("technical-tags")
        business_tags = request.form.get("business-tags")
        # print(title,description)
        form = Form(title = title,description = description,technical_tags = technical_tags,business_tags = business_tags)
        # db.
        db.session.add(form)
        print(form)
        db.session.commit()

    
    return(render_template("post.html"))

# @app.route("/Register")
# def registed():
#     return(render_template("Register.html"))

if __name__ == "__main__":
    app.run(debug=True)