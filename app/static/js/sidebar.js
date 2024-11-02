function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const hamburger = document.querySelector('.hamburger'); 
    sidebar.classList.toggle('hidden');
    hamburger.classList.toggle('hidden');
}