import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

declare const myFun:any;
declare const changeTheme:any;
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  Primary:boolean=true;
  From:boolean=true;
  Domain:boolean=true;
  Content:boolean=true;
  Subject:boolean=true;
  visible_primary:boolean=false;
  visible_from:boolean=false;
  visible_content:boolean=false;
  visible_domain:boolean=false;
  visible_subject:boolean=false;

  constructor() { }

  ngOnInit(): void {
    this.callfun();
    this.callChangeTheme();
    this.onClickPrimary();
    this.onClickFrom();
    this.onClickContent();
    this.onClickDomain();
    this.onClickSubject();
  }
  callfun(){
    myFun();
  }

  callChangeTheme(){
    changeTheme();
  }

  onClickPrimary(){
    this.visible_from=false;
    this.visible_content=false;
    this.visible_domain=false;
    this.visible_subject=false;
    this.Primary=!this.Primary;
    this.visible_primary=!this.visible_primary;

  }

  onClickFrom(){
    this.visible_primary=false;
    this.visible_content=false;
    this.visible_domain=false;
    this.visible_subject=false;
    this.From=!this.From;
    this.visible_from=!this.visible_from;
  }

  onClickContent(){
    this.visible_from=false;
    this.visible_domain=false;
    this.visible_primary=false;
    this.visible_subject=false;
    this.Content=!this.Content;
    this.visible_content=!this.visible_content;
  }

  onClickDomain(){
    this.visible_from=false;
    this.visible_content=false;
    this.visible_primary=false;
    this.visible_subject=false;
    this.Domain=!this.Domain;
    this.visible_domain=!this.visible_domain;
  }

  onClickSubject(){
    this.visible_from=false;
    this.visible_content=false;
    this.visible_primary=false;
    this.visible_domain=false;
    this.Subject=!this.Subject;
    this.visible_subject=!this.visible_subject;
  }

}
