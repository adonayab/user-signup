from flask import Flask, render_template, request, redirect


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
    
    if len(username) < 3 or len(username) > 20:
      username_error = 'Username must be (3-20) characters!'
      return render_template('/index.html', username_error=username_error)
    else:
      if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be (3-20) characters!'
        return render_template('/index.html', password_error=password_error)
      
      if password != pass_confirm:
        pass_confirm_error = "Password don't match"
        return render_template('/index.html', pass_confirm_error=pass_confirm_error)
      
      if email == '':
        redirect('/welcome?username={}'.format(username))
      elif ('@' not in email) and ('.' not in email):
        email_error = 'Invalid email address!'
        return render_template('/index.html', email_error=email_error)
    
    
      return redirect('/welcome?username={}'.format(username))
    
      
  return render_template('index.html')


@app.route('/welcome')
def welcome():
  username = request.args.get('username')
  return render_template('welcome.html', username=username)

app.run()
