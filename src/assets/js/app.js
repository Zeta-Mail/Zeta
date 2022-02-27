function myFun() {
  let arrow = document.querySelectorAll(".arrow");
  for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
      let arrowParent = e.target.parentElement.parentElement;
      arrowParent.classList.toggle("showMenu");
    });
  }
  let sidebar = document.querySelector(".sidebar");
  let sidebarBtn = document.querySelector(".bx-menu");
  console.log(sidebarBtn);
  sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
  });

  const body = document.querySelector('body'),
    modeSwitch = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");


  modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
      modeText.innerText = "Light mode";
    } else {
      modeText.innerText = "Dark mode";

    }
  });
}

function replaceContent(){
  let primary=document.querySelector('#primary');
  let from=document.querySelector('#from');
  let content=document.querySelector('#content');
  let domain=document.querySelector('#domain');
  let subject=document.querySelector('#subject');
  let addnew=document.querySelector('#addnew');
  let contentDetails=document.querySelector('#content-details');
  let p=document.querySelector('p');

  primary.addEventListener('click',()=>{
    p.innerText='Primary';
  });
  from.addEventListener('click',()=>{
    p.innerText='From';
  });
  content.addEventListener('click',()=>{
    p.innerText='Content';
  });
  domain.addEventListener('click',()=>{
    p.innerText='Domain';
  });
  subject.addEventListener('click',()=>{
    p.innerText='Subject';
  });
  addnew.addEventListener('click',()=>{
    p.innerText='Content';
  });

}
