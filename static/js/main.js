document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    const commentInput = document.getElementById('comment-input');
    const commentsList = document.getElementById('comments-list');

    commentForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const comment = commentInput.value.trim();

        if (comment) {
            fetch('/analyze_comment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({comment: comment}),
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_hate_speech) {
                    alert(data.message || 'Comment blocked due to potential hate speech.');
                } else {
                    const li = document.createElement('li');
                    li.textContent = comment;
                    commentsList.appendChild(li);
                    commentInput.value = '';
                }
            });
        }
    });
});