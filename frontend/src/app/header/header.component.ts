import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { MenuInfo } from '../interface/ec-template.interface';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  menuList: MenuInfo[] = [];
  checkStatus : boolean;
  isSeller : boolean = false;
  UserIDValue :string;
  userType : string;
  
  constructor(
    public dataService: DataService,
    private authService : AuthService,) {}

  ngOnInit() {
    this.getMenuList();
    this.checkStatus = this.getUserID();
    
  }

  getMenuList() {
    this.dataService.getMenuList().subscribe((data: MenuInfo[]) => {
      this.menuList = data;
    });
  }

  getUserID() :boolean {
    if(this.authService.getUser().userID != undefined ){
      console.log(this.authService.getUser())
      console.log("true");
      
      if(this.authService.getUser().usertype == "seller"){
        this.authService.usertype = "seller";
        this.isSeller = true;
      }

      else if(this.authService.getUser().usertype == "buyer"){
        this.authService.usertype = "buyer";
        this.isSeller = false;
      }


      this.UserIDValue = this.authService.getUser().userID
      return true
    }
    else {
      console.log("false");
      return false
    }
  }

  logout() : void{
    this.authService.logout();
    window.location.replace('../');
    this.authService.isloggedin = false;
  }
}
