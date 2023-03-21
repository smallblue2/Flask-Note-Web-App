# Import the required libraries
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website import db
from website.models import Note
import json

# Create a blueprint for views
views = Blueprint('views', __name__)

# Define the route for the home page with GET and POST methods, and require user authentication.
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # If the request method is POST, process the submitted form
    if request.method == 'POST':
        # Get the 'note' field from the form
        note = request.form.get('note')
        
        # Check the note is more than 1 character long.
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # Create a new Note, containing the note data, mapped to the current user.
            new_note = Note(data=note, user_id=current_user.id)
            # Add it to the database
            db.session.add(new_note)
            # Commit it to the database
            db.session.commit()
            # Signal that the note has been created
            flash('Note added!', category='success')
    
    # Render the home template as the current user
    return render_template("home.html", user=current_user)

# Define the route for deleting a note with the POST method.
@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Parse the JSON data form the request
    note = json.loads(request.data)

    # Get the note ID from the parsed data
    noteId = note['noteId']
    # Check if the note exists and that the current user is the owner
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            # Delete the note from the database
            db.session.delete(note)
            # Commit the change to the database
            db.session.commit()

    # Return an empty JSON response
    return jsonify({})
