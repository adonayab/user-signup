from flask import Flask, render_template, request, redirect
import re


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
def index():
  
  empty_form_error = 'Please fill in the required fields!'
  username_error = ''
  password_error = ''
  pass_confirm_error = ''
  email_error = ''

  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    email = request.form['email']
    
    if username == '' and password == '' and pass_confirm == '':
      username_error = 'Username is required'
      password_error = 'Password is required'
      pass_confirm_error = "Password don't match"
      
      return render_template('/index.html', empty_form_error=empty_form_error, username_error=username_error, password_error=password_error, pass_confirm_error=pass_confirm_error)
    


    pattern = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    valid_username = re.findall(pattern, username)
    if username not in valid_username:
        username_error = 'Invalid username'
    if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid Password'
    if password != pass_confirm:
        pass_confirm_error = "Password don't match"
        
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    valid_email = re.findall(pattern, email)
    if email == '':
      pass
    elif email not in valid_email:
        email_error = 'Invalid email address'
        return render_template('/index.html', username_error=username_error, password_error=password_error, pass_confirm_error=pass_confirm_error, email_error=email_error)



    pattern = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    valid_username = re.findall(pattern, username)
    if username not in valid_username:
    # if len(username) < 3 or len(username) > 20:
      username_error = 'Invalid username'
      return render_template('/index.html', username_error=username_error)
    else:
      if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid Password'
      if password != pass_confirm:
        pass_confirm_error = "Password don't match"
        return render_template('/index.html', password_error=password_error, pass_confirm_error=pass_confirm_error)
      


      if password != pass_confirm:
        pass_confirm_error = "Password don't match"
        return render_template('/index.html', pass_confirm_error=pass_confirm_error)
      

      pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
      valid_email = re.findall(pattern, email)
      if email == '':
        pass
        # redirect('/welcome?username={}'.format(username), code=302)
      elif email not in valid_email:
        email_error = 'Invalid email address'
        return render_template('/index.html', email_error=email_error)
    
    
      # return redirect('/welcome?username={}'.format(username))
      return redirect('/welcome?username={}'.format(username))
    
      
  return render_template('index.html')


@app.route('/welcome')
def welcome():
  username = request.args.get('username')
  return render_template('welcome.html', username=username)

app.run()
