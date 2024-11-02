function likePost() {
    alert("Post Liked!");
}

function commentPost() {
    alert("Commenting on post...");
}

function sharePost() {
    alert("Post Reshared!");
}

function createEvent() {
    const eventTitle = prompt("Enter the event title:");
    if (eventTitle) alert(`Event "${eventTitle}" created!`);
}

function createArticle() {
    const articleTitle = prompt("Enter the article title:");
    if (articleTitle) alert(`Article "${articleTitle}" written!`);
}