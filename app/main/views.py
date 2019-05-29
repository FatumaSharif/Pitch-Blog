from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import Pitch, User, Comment
from .forms import PitchForm, UpdateProfile, CommentForm
from flask_login import login_required,current_user
from .. import db, photos


@main.route('/')
def index():
  pitch = Pitch.get_pitch()
  title = f'Pitch'
  return render_template('index.html', title=title, pitch=pitch) 


@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def post_pitch():
  pitch_form = PitchForm()
  if pitch_form.validate_on_submit():
    name = pitch_form.name.data
    category = pitch_form.category.data
    pitch = pitch_form.pitch.data

    new_pitch = Pitch(name=name, category=category, pitch=pitch)
    new_pitch.save_pitch()
    return redirect(url_for('main.index'))
  
  title = f'Post a Pitch'
  return render_template('pitch.html', title=title, pitch_form=pitch_form)


@main.route('/user/<uname>')
@login_required
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user=user)


@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', uname=user.username))
  
  return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/comment', methods=['GET','POST'])
@login_required
def comment():
  comment_form = CommentForm()
  # pitch_id = Pitch.get_pitch(id)

  if comment_form.validate_on_submit():
    username = comment_form.username.data
    comment = comment_form.comment.data

    new_comment = Comment(username=username, comment=comment)

    new_comment.save_comment()
    return redirect(url_for('main.index'))
  
  title = f'Pitch Review'
  return render_template('comment.html', title=title, comment_form=comment_form)