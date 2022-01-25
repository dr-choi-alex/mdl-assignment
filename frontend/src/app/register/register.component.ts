import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  constructor(
    private formBuilder: FormBuilder,
    private _api : ApiService,
  ) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      usertype: ['', Validators.required],
      username: ['', Validators.required],
      userID: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', Validators.required]
    });
  }
  onSubmit() {
    let b = this.registerForm.value
    console.log(b)
    this._api.postTypeRequest('register', b).subscribe((res: any) => {
      console.log(res)
      if(res.value == "Success")
      {
        history.back();
        alert(`Register ${res}.`)
      }
      else 
      {
        alert(`Register ${res}.`)
      }
    }, err => {
      console.log(err)
    });
  }

}
