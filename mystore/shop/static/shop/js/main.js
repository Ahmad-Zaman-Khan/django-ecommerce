function openNav() {

  document.getElementById("mySidenav").style.width = "320px";
  document.getElementById("overlay").style.display = "block";
  document.body.style.overflow = "hidden";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("overlay").style.display = "none";
  document.body.style.overflow = "auto";
}