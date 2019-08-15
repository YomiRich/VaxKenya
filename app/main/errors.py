from flask import render_template
from ._init_ import main

# Error handler decorator
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = '404 page'
    return render_template('fourOwfour.html', title=title),404