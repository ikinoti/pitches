from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .pitch_form import CommentsForm, UpdateProfile, PitchForm, UpvoteForm
from ..models import Comment, Pitch, User 
from flask_login import login_required, current_user
from .. import db,photos

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    search_pitch = request.args.get('pitch_query')
    pitches= Pitch.get_all_pitches()  

    return render_template('index.html', title = title, pitches= pitches)

@main.route('/inteview/pitches/')
def interview():
    '''
    View root page function that returns the index page and its data
    '''
    pitches= Pitch.get_all_pitches()
    title = 'Home - Welcome to The best Pitching Website Online'  
    return render_template('interview.html', title = title, pitches= pitches )

@main.route('/pick_up_lines/pitches/')
def pick_up_line():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pick Up Lines'

    pitches= Pitch.get_all_pitches()

    return render_template('pick_up_lines.html', title = title, pitches= pitches )

@main.route('/promotion/pitches/')
def promotion():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Promotion Pitches'

    pitches= Pitch.get_all_pitches()

    return render_template('promotion.html', title = title, pitches= pitches )


@main.route('/product/pitches/')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    pitches= Pitch.get_all_pitches()
    return render_template('product.html', title = title, pitches= pitches )

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)

@main.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    searched_pitches = search_pitch(pitch_name)
    title = f'search results for {pitch_name}'

    return render_template('search.html',pitches = searched_pitches)

@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    Function that creates new pitches
    '''
    form = PitchForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        pitch= form.content.data
        category_id = form.category_id.data
        new_pitch= Pitch(pitch= pitch, category_id= category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form= form, category= category)