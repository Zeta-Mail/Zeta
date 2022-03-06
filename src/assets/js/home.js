/*-----------------------------ADD-----------------------------*/

function openNav_1() {
	document.querySelector(".overlay").style.width = "80%";  
}

document.addEventListener('mousedown',function(event){
        var side_dom    = document.querySelector(".overlay")
        if(side_dom.style.width == '80%'){
                if(!side_dom.contains(event.target)){
                        document.querySelector(".overlay").style.width = "0";
                }
        }       
})

/*================================Dialog Box================================*/

function creating() {
	document.querySelector(".modal").style.display = "block";
	document.querySelector(".overlay").style.width = "0";
}


var modal1 = document.getElementById("myModal1");
var modal2 = document.getElementById("myModal2");
var modal3 = document.getElementById("myModal3");
var modal4 = document.getElementById("myModal4");


var filter = document.getElementById("Filter");
filter.onclick = function() {
  FilterO.style.display = "block";
}


var filterO = document.getElementById("FilterO");

var from = document.getElementById("From");
var content = document.getElementById("Content");
var subject = document.getElementById("Subject");
var domain = document.getElementById("Domain");


var back1 = document.getElementById("back1");
var create1 = document.getElementById("create1");
var back2 = document.getElementById("back2");
var create2 = document.getElementById("create2");
var back3 = document.getElementById("back3");
var create3 = document.getElementById("create3");
var back4 = document.getElementById("back4");
var create4 = document.getElementById("create4");


var span1 = document.getElementsByClassName("close1")[0];
var span2 = document.getElementsByClassName("close2")[0];
var span3 = document.getElementsByClassName("close3")[0];
var span4 = document.getElementsByClassName("close4")[0];



from.onclick = function() {
  modal1.style.display = "block";
  myModal.style.display = "none";
  filterO.style.display = "none";
}

content.onclick = function() {
  modal2.style.display = "block";
  myModal.style.display = "none";
  filterO.style.display = "none";
}

subject.onclick = function() {
  modal3.style.display = "block";
  myModal.style.display = "none";
  filterO.style.display = "none";
}

domain.onclick = function() {
  modal4.style.display = "block";
  myModal.style.display = "none";
  filterO.style.display = "none";
}


back1.onclick = function() {
  myModal.style.display = "block";
  modal1.style.display = "none";
  filterO.style.display = "none";
}

create1.onclick = function() {
  myModal.style.display = "none";
  modal1.style.display = "none";
  filterO.style.display = "none";
}


back2.onclick = function() {
  myModal.style.display = "block";
  modal2.style.display = "none";
  filterO.style.display = "none";
}

create2.onclick = function() {
  myModal.style.display = "none";
  modal2.style.display = "none";
  filterO.style.display = "none";
}

back3.onclick = function() {
  myModal.style.display = "block";
  modal3.style.display = "none";
  filterO.style.display = "none";
}

create3.onclick = function() {
  myModal.style.display = "none";
  modal3.style.display = "none";
  filterO.style.display = "none";
}

back4.onclick = function() {
  myModal.style.display = "block";
  modal4.style.display = "none";
  filterO.style.display = "none";
}

create4.onclick = function() {
  myModal.style.display = "none";
  modal4.style.display = "none";
  filterO.style.display = "none";
}


function closing() {
	document.querySelector(".modal").style.display = "none";
	filterO.style.display = "none";
}


span1.onclick = function() {
  modal1.style.display = "none";
  modal.style.display = "none";
  filterO.style.display = "none";
}

span2.onclick = function() {
  modal2.style.display = "none";
  modal.style.display = "none";
  filterO.style.display = "none";
}

span3.onclick = function() {
  modal3.style.display = "none";
  modal.style.display = "none";
  filterO.style.display = "none";
}

span4.onclick = function() {
  modal4.style.display = "none";
  modal.style.display = "none";
  filterO.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it

window.onclick = function(event) {
  if (event.target == modal) {
    filterO.style.display = "none";
  }
}

/*===========================================================================*/


function settingsWindow() {
	document.querySelector(".settingsOverlay").style.width = "100%";  
	document.querySelector(".overlay").style.width = "0";
}

function settingsWindowClose() {
	document.querySelector(".settingsOverlay").style.width = "0%";  
}

/*===========================================================================*/


const body = document.querySelector('body'),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");




modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");

    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
    }else{
        modeText.innerText = "Dark mode";

    }
});
