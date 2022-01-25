import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ProductInfo } from '../interface/ec-template.interface';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.scss']
})
export class FrontPageComponent implements OnInit {
  productList: ProductInfo[];
  constructor(private dataService: DataService, private _api : ApiService) {}

  ngOnInit() {
    this.dataService.productList$.subscribe(data => {
      this.productList = data;
      console.log("this is")
      console.log(data)
    });

    this._api.getTypeRequest('products').subscribe((res: any) => {
         console.log(res)
         this.productList = res
      }, err => {
         console.log(err)
      });
  }

      // //get products
    // this._api.getTypeRequest('products').subscribe((res: any) => {
    //    console.log(res)
    //    //this.imageSrc = res
    // }, err => {
    //    console.log(err)
    // });
}
