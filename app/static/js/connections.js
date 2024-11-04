// Array of  connections data
const connections = [
    { name: "Alex Johnson", title: "Software Engineer at TechCorp" },
    { name: "Emily Davis", title: "Graphic Designer at Creatives Inc." },
    { name: "Michael Lee", title: "Marketing Manager at Marketify" },
    { name: "Sarah Brown", title: "UX Designer at DesignHub" },
    { name: "David Wilson", title: "Data Scientist at DataMinds" },
    { name: "Laura Kim", title: "Frontend Developer at WebWorks" },
    { name: "James Taylor", title: "Project Manager at BuildIt" },
    { name: "Olivia White", title: "Content Strategist at WriteRight" },
    { name: "Ethan Harris", title: "Full Stack Developer at CodeBase" },
    { name: "Sophia Garcia", title: "Art Director at Visualize" },
    { name: "Liam Martin", title: "Machine Learning Engineer at AIWorks" },
    { name: "Charlotte Brown", title: "Social Media Manager at Buzzly" },
    { name: "Henry Adams", title: "Cybersecurity Specialist at SafeNet" },
    { name: "Mia Roberts", title: "Product Designer at Craftsy" },
    { name: "Noah Clark", title: "Data Analyst at Insightful" }
];

// Function to load connections
function loadConnections() {
    const container = document.getElementById("connections-container");

    connections.forEach(connection => {
        const card = document.createElement("div");
        card.className = "connection-card";

        // Sample placeholder profile image
        const img = document.createElement("img");
        img.src = "https://via.placeholder.com/80";
        img.alt = `${connection.name}'s profile picture`;

        const name = document.createElement("h3");
        name.textContent = connection.name;

        const title = document.createElement("p");
        title.textContent = connection.title;

        const buttonContainer = document.createElement("div");
        buttonContainer.className = "button-container";

        const messageBtn = document.createElement("button");
        messageBtn.className = "message-btn";
        messageBtn.textContent = "Message";

        const scheduleBtn = document.createElement("button");
        scheduleBtn.className = "schedule-btn";
        scheduleBtn.textContent = "Schedule";

        const profileBtn = document.createElement("button");
        profileBtn.className = "profile-btn";
        profileBtn.textContent = "Profile";

        buttonContainer.appendChild(messageBtn);
        buttonContainer.appendChild(scheduleBtn);
        buttonContainer.appendChild(profileBtn);

        card.appendChild(img);
        card.appendChild(name);
        card.appendChild(title);
        card.appendChild(buttonContainer);

        container.appendChild(card);
    });
}

// Load connections when the page loads
window.onload = loadConnections;
