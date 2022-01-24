import { Component, OnInit } from '@angular/core';
import { DataService } from './services/data.service';
import { AuthService } from './services/auth.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  private roles: string[] = [];
  isLoggedIn = false;
  showAdminBoard = false;
  showModeratorBoard = false;
  username?: string;

  constructor(
    public dataService: DataService,
    private authService : AuthService,
    ) {}

  ngOnInit() {
    
  }
}
