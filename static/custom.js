// custom.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Custom JS loaded');
    
    // Example: Add a smooth scroll effect to all links
    const links = document.querySelectorAll('a');
    for (const link of links) {
        link.addEventListener('click', function(event) {
            if (this.hash !== "") {
                event.preventDefault();
                const hash = this.hash;
                window.scroll({
                    top: document.querySelector(hash).offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    }
});
