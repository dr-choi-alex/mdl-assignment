import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  loginForm: FormGroup;

  constructor(
    private authService : AuthService,
    private formBuilder: FormBuilder,
    private _api : ApiService,


  ) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      userID: ['', Validators.required],
      password: ['', Validators.required]
    });
 
  }

  onSubmit() {
    // Backend로 데이터를 주고 받는 부분
    let b = this.loginForm.value
    console.log(b)
    this._api.postTypeRequest('login', b).subscribe((res: any) => {
      console.log(res)
     
      window.location.replace("./")
      this.authService.isloggedin = true;
      console.log("is loggedin = {}", this.authService.isloggedin)
      alert('login successful');
      
    //Local Storige에 정보를 저장하는 부분
      this.authService.saveUserInfo(res);
     
    }, err => {
      console.log(err)
      alert('login failed');
    });
  }

  }
