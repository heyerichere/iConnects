function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');

    sidebar.classList.toggle('hidden');
    
    if (sidebar.classList.contains('hidden')) {
        mainContent.style.marginLeft = '30px';
    } else {
        mainContent.style.marginLeft = '250px'; 
    }
}