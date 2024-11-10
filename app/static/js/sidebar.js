function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const connectionsContent = document.querySelector('.connections-content');
    const postsContent = document.querySelector('.post-container');

    sidebar.classList.toggle('hidden');
    
    if (sidebar.classList.contains('hidden')) {
        if (mainContent) mainContent.style.marginLeft = '30px';
        if (connectionsContent) connectionsContent.style.marginLeft = '110px';
        if (postsContent) postsContent.style.marginLeft = '30px';

    } else {
        if (mainContent) mainContent.style.marginLeft = '250px'; 
        if (connectionsContent) connectionsContent.style.marginLeft = '280px'; 
        if (postsContent) postsContent.style.marginLeft = '250px';
    }
}