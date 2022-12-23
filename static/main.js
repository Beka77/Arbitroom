// var modal = document.getElementById("myModal");
// var btn = document.getElementById("myBtn");
// var span = document.getElementsByClassName("close")[0];

// btn.onclick = function () {
//   modal.style.display = "block";
// };
// span.onclick = function () {
//   modal.style.display = "none";
// };
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// };
let popup = document.getElementById("mypopup");
popupToggle = document.getElementById("myBtn");
popupClose = document.querySelector(".close");
popupToggle.onclick = function () {
  popup.classList.toggle("show");
};
popupClose.onclick = function () {
  popup.classList.toggle("show");
};
window.onclick = function (e) {
  if (e.taret == popup) {
    popup.classList.toggle("show");
  }
};
let popup1 = document.getElementById("mypopup1");
popupToggle = document.getElementById("myBtn1");
popupClose = document.querySelector(".close1");
popupToggle.onclick = function () {
  popup1.classList.toggle("show");
};
popupClose.onclick = function () {
  popup1.classList.toggle("show");
};
window.onclick = function (e) {
  if (e.taret == popup) {
    popup1.classList.toggle("show");
  }
};
