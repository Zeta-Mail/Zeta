import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  showMenu: boolean = true;
  showMore: boolean = false;
  showInbox:boolean=true;
  showSpam:boolean=false;
  showStared:boolean=false;

  constructor() {
  }

  ngOnInit(): void {


  }


  toogleMenu() {
    this.showMenu = !this.showMenu
  }

  toogleMore() {
    this.showMore = !this.showMore
  }
  toggleInbox(){
    this.showInbox=true;
    this.showSpam=false;
    this.showStared=false;
  }
  toggleSpam(){
    this.showSpam=true;
    this.showInbox=false;
    this.showStared=false;
  }
  toggleStared(){
    this.showStared=true;
    this.showSpam=false;
    this.showInbox=false;
  }
}



