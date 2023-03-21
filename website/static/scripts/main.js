// Function to hide alerts
function Hide(HideID) {
    HideID.style.display = 'none';
}

// Function to send a delete post request
function deleteNote(noteId) {
    // Send it to the correct route
    fetch('/delete-note', {
        // POST request
        method: 'POST',
        // Send the object we wish to delete in JSON
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        // Finally refresh the page
        window.location.href ='/';
    });
}
