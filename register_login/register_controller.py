from model import *
from flask import render_template,request

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        formdata=request.form
        errors=[]
        if not formdata.get('username'):
            errors.append('User name cannot be empty')
        if not formdata.get('email'):
            errors.append('email cannot be empty')
        if not formdata.get('password'):
            errors.append('password cannot be empty')

        if errors:
            return render_template('register.html',errors=errors)

        try:
            user= User( name = formdata.get('username'),
                        email = formdata.get('email'),password = formdata.get('password'))
            db.session.add(user)
            db.session.commit()
        except:
            return render_template('register.html', message='already user present please try different name...')

        return render_template('register.html',message= 'user add successfully')

    return render_template('register.html')
