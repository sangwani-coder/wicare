// function readMoreReadLess() {
//     var dots = document.getElementById("dots");
//     var moreText = document.getElementClass("more");
//     var btnText = document.getElementByClass("moreBtn");
  
//     if (dots.style.display === "none") {
//       dots.style.display = "inline";
//       btnText.innerHTML = "Read more";
//       moreText.style.display = "none";
//     } else {
//       dots.style.display = "none";
//       btnText.innerHTML = "Read less";
//       moreText.style.display = "inline";
//     }
//   }

function readMoreReadLess(id) {
    var dots = document.getElementsByClassName("dots")[id - 1];
    var moreText = document.getElementsByClassName("more")[id - 1];
    var btnText = document.getElementsByClassName("myBtn")[id - 1];
    
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  