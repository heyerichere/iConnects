document.addEventListener("DOMContentLoaded", function() {
    const submitButton = document.getElementById("submitPost");

    submitButton.addEventListener("click", function(event) {
        event.preventDefault();
        const title = document.getElementById("postTitle").value;
        const content = document.getElementById("postText").value;

        fetch("/posts/create_ajax", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title, content: content })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert(data.message);
                // Clear the form fields
                document.getElementById("postTitle").value = "";
                document.getElementById("postText").value = "";

                // Optionally, append the new post to the posts feed
                const newPost = document.createElement("div");
                newPost.classList.add("post");
                newPost.innerHTML = `
                    <div class="post-header">
                        <img src="/static/images/profilepicture1.webp" alt="Profile Picture" class="profile-picture">
                        <div class="post-info">
                            <strong>${data.post.title}</strong><br>
                            <span>${data.post.timestamp}</span>
                        </div>
                    </div>
                    <div class="post-content">
                        <p>${data.post.content}</p>
                    </div>
                    <div class="post-actions">
                        <button onclick="likePost()">Like</button>
                        <button onclick="commentPost()">Comment</button>
                        <button onclick="sharePost()">Reshare</button>
                    </div>
                `;
                document.querySelector(".feed-container").appendChild(newPost);
            }
        })
        .catch(error => console.error("Error:", error));
    });
});