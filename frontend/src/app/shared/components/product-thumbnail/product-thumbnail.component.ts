import { Component, OnInit, Input } from '@angular/core';
import { ProductInfo } from 'src/app/interface/ec-template.interface';
import { Router } from '@angular/router';
import { ApiService } from '../../../services/api.service'
import { AuthService } from '../../../services/auth.service';


@Component({
  selector: 'app-product-thumbnail',
  templateUrl: './product-thumbnail.component.html',
  styleUrls: ['./product-thumbnail.component.scss']
})
export class ProductThumbnailComponent implements OnInit {
  @Input()
  data: ProductInfo;
  @Input()
  width = '300';
  @Input()
  height = '320';

  defaultImage = './assets/images/default-image.png';

  constructor(private router: Router, private _api : ApiService, private authService : AuthService,) {}

  ngOnInit() {}

  detailInfoOn() {
    alert(" name : " + this.data.name + "\n price : " + this.data.price + "\n description : " + this.data.description)
    //this.router.navigate([`/category/product/${this.data.id}`]);
  }

  addCart() {
    // console.log("=====================check=====================")
    // console.log("product Info")
    // console.log(this.data)

    //const userLoginID = this.authService.getUser().userID;
    const userID = this.authService.getUser().id;
    const ProductID = this.data.id
    const body = {productID : ProductID, quantity : 1}

    const url = 'users/' + userID + "/Carts" 

    // console.log("User Info")
    // console.log(this.authService.getUser())
    // console.log("productID : " + userID + "  / userID : " + ProductID)

    // console.log(body)

    //=========================[ 확인 ]======================
    //post임 수정해야함, API 수정 후 다시 skeleton 만들어서 하기
    //=======================================================
    this._api.postTypeRequest(url, body).subscribe((res: any) => {
      console.log(res.msg)

      alert(res.msg)

    }, err => {
      console.log(err)
    });

  }
}
