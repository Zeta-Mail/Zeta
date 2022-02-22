import { Component } from '@angular/core';
declare const myFun:any;
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Zeta';
  callfun(){
    myFun();
  }
}
