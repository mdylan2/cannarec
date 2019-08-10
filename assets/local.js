window.addEventListener('scroll', function(event) { // To listen for 
    
    var nav = document.querySelector('.main-navbar'); // Identify target
    var bottom_right = document.querySelector('.scroll-top-wrapper')

    event.preventDefault();

    if (window.scrollY <= 100) { // Just an example
        this.console.log("here")
        nav.classList.remove("bg-colored")
        nav.classList.add("bg-transparent")
        bottom_right.classList.remove("show")
    } else {
        this.console.log("in here")
        nav.classList.remove("bg-transparent")
        nav.classList.add("bg-colored")
        bottom_right.classList.add("show")
    }
});