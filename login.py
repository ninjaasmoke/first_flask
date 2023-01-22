from flask import render_template, redirect, url_for

def valid_login(username, password):
    print(f'{username}: {password}')
    return username == 'ninjaasmoke' and password == 'hellosai'

def log_the_user_in(username):
    return redirect(url_for('hello', name=username))