import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  showMenu: boolean = true;
  showMore: boolean = false;
  // Primary: boolean = true;
  // From: boolean = true;
  // Domain:boolean=true;
  // Content:boolean=true;
  // visible_primary: boolean = false;
  // visible_from: boolean = false;
  // visible_content=false;
  // visible_domain=false;

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

  // onClickPrimary(){
  //   this.visible_from=false;
  //   this.visible_content=false;
  //   this.visible_domain=false;
  //   this.Primary=!this.Primary;
  //   this.visible_primary=!this.visible_primary;
  //
  // }
  //
  // onClickFrom(){
  //
  //   this.From=false;
  //   this.visible_from=true;
  // }
  //
  // onClickContent(){
  //   this.visible_from=false;
  //   this.visible_domain=false;
  //   this.visible_primary=false;
  //   this.Content=!this.Content;
  //   this.visible_content=!this.visible_content;
  // }
  //
  // onClickDomain(){
  //   this.visible_from=false;
  //   this.visible_content=false;
  //   this.visible_primary=false;
  //   this.Domain=!this.Domain;
  //   this.visible_domain=!this.visible_domain;
  // }

}



