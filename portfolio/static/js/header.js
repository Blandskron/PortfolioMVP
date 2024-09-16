document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggle-dark-light');
    const body = document.body;

    toggleBtn.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        body.classList.toggle('light-mode');
        
        if (body.classList.contains('dark-mode')) {
            toggleBtn.classList.remove('fa-moon');
            toggleBtn.classList.add('fa-sun');
        } else {
            toggleBtn.classList.remove('fa-sun');
            toggleBtn.classList.add('fa-moon');
        }
    });

});
