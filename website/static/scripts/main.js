function Hide(HideID) {
    HideID.style.display = 'none';
}

function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href ='/';
    });
}