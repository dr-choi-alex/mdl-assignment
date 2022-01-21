import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {

  // public imagePath: any;
  // imgURL: any;
  // public message: string;
  
  form: FormGroup

  constructor(public fb: FormBuilder, private http: HttpClient) { }
  imageSrc: string;
  ngOnInit(): void {
    this.form = this.fb.group({
      productname: ['', Validators.required],
      productprice:[0, Validators.required],
      file:['', Validators.required],
      fileSource:['', Validators.required]
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
          fileSource: reader.result
        });
   
      };
   
    }
  }

  

  onSubmit(){

    const body = {}
    
    this.http.get('http://localhost:5000/products')
    .subscribe(res => {
        console.log(res)
    });

    this.http.post('http://localhost:5000/products', body, {
      params: new HttpParams().set('price', this.form.value.productprice),
    })
    .subscribe(res => {
      console.log(res)
    });

  }
   
  // preview(files: any){
  //   if(files.length ===0)
  //     return;
  //   var mimeType = files[0].type;
  //   if (mimeType.match(/image\/*/) == null) {
  //     this.message = "Only images are supported.";
  //     return;
  //   }
  
  //   var reader = new FileReader();
  //   this.imagePath = files;
  //   reader.readAsDataURL(files[0]); 
  //   reader.onload = (_event) => { 
  //     this.imgURL = reader.result; 
  //   }
  // }

}
