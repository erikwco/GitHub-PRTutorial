from flask import BluePrint, render_template

tutor = BluePrint('tutor', __name__, template_folder='templates')
@tutor.route('/')
def main():
    return render_template('login.html')
