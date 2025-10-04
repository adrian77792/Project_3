function openMENU() {
    document.getElementById("hamburger").style.display = "none";
    const menu=document.getElementById("nav-bottom");
    menu.style.display="flex"
    menu.classList.add("open");
}

function closeMENU() {
    document.getElementById("hamburger").style.display = "block";
    const menu=document.getElementById("nav-bottom");
    menu.style.display="none"
    menu.classList.remove("open");
}

function scrollToTop() {
    window.scrollTo({
    top: 0,
    behavior: 'smooth' // płynne przewijanie
    });
  }

