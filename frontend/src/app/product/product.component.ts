import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {
  
  form: FormGroup
  imageSrc: string

  constructor(public fb: FormBuilder, private _api : ApiService,) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      name: ['', Validators.required],
      price:[0, Validators.required],
      description:['', Validators.required],
      image:['', Validators.required]
    });
  }

  onFileChange(event) {
    const reader = new FileReader();
    
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
    
      reader.onload = () => {
   
        this.imageSrc = reader.result as string;
     
        this.form.patchValue({
          image: reader.result
        });
   
      };
   
    }
  }

  onSubmit() {

    if (this.form.invalid) {
      alert('check your form')
    } else{
      const body = this.form.value

      //console.log(body)
  
      if(this.form.value.name !== ''){
        this._api.postTypeRequest('products', body).subscribe((res: any) => {
          console.log(res)
          alert('db update')
          window.location.reload(); //page reload
        }, err => {
          console.log(err)
        });
      }
    }

  
    
    // //get products
    // this._api.getTypeRequest('products').subscribe((res: any) => {
    //    console.log(res)
    //    //this.imageSrc = res
    // }, err => {
    //    console.log(err)
    // });
  }

   

}
