// Dark mode toggle functionality
const darkModeToggle = document.getElementById('darkModeToggle');
const root = document.documentElement;

darkModeToggle.addEventListener('change', () => {
    if (darkModeToggle.checked) {
        document.body.style.backgroundColor = '#1a1a1a';
        document.querySelectorAll('.event-card').forEach(card => {
            card.style.backgroundColor = '#2d2d2d';
            card.style.color = '#ffffff';
        });
        document.querySelectorAll('.event-description').forEach(desc => {
            desc.style.color = '#cccccc';
        });
        document.querySelectorAll('.event-title, .section-title').forEach(title => {
            title.style.color = '#ffffff';
        });
    } else {
        document.body.style.backgroundColor = '#f5f6fa';
        document.querySelectorAll('.event-card').forEach(card => {
            card.style.backgroundColor = '#ffffff';
            card.style.color = '#000000';
        });
        document.querySelectorAll('.event-description').forEach(desc => {
            desc.style.color = '#666666';
        });
        document.querySelectorAll('.event-title').forEach(title => {
            title.style.color = '#1a4971';
        });
        document.querySelectorAll('.section-title').forEach(title => {
            title.style.color = '#1a4971';
        });
    }
});