from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(4)

class YearForm(FlaskForm):
    year = IntegerField('Введіть рік', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Перевірити рік')

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    form = YearForm()
    if form.validate_on_submit():
        year = form.year.data
        if is_leap_year(year):
            flash(f'{year} це - високосний рік', 'success')
        else:
            flash(f'{year} це - не високосний рік', 'danger')
        return redirect(url_for('result', year=year))
    return render_template('home.html', form=form)

@app.route('/result/<int:year>')
def result(year):
    is_leap = is_leap_year(year)
    return render_template('result.html', year=year, is_leap=is_leap)