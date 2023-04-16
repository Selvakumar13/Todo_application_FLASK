from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,DateField,SubmitField,SelectField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    first_name=StringField('First Name',validators=[DataRequired()])
    last_name=StringField('Last Name', validators=[DataRequired()])
    email=EmailField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Register')
    
class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Sign In')
                     
class TodoForm(FlaskForm):
    task_name=StringField('Name',validators=[DataRequired()])
    due_date=DateField('Due Date',validators=[DataRequired()])
    status=SelectField('Status',choices=[('Complete','Complete'),('Not Started','Not Started')])
    submit=SubmitField('Add Task')

class EditTodoForm(FlaskForm):
    task_name=StringField('Name',validators=[DataRequired()])
    due_date=DateField('Due Date',validators=[DataRequired()])
    status=SelectField('Status',choices=[('Complete','Complete'),('Not Started','Not Started')])
    submit=SubmitField('Add Task')