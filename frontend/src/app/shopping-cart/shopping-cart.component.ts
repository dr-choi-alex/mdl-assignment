import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ShoppingCartItemList, CartProductInfo } from '../interface/ec-template.interface';
import { AuthService } from '../services/auth.service';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.scss']
})
export class ShoppingCartComponent implements OnInit {
  cart_data: ShoppingCartItemList[];
  data: CartProductInfo[] = [];
  // order summary
  subTotal = 0;
  tax = 0;
  total = 0;
  index = 0;

  constructor(
    private dataService: DataService,
    private authService: AuthService,
    private _api: ApiService
    ) {}
  ngOnInit() {
    // this.data = this.dataService.shoppingCartData;
    this.getOrderSummary();
  }

  // updateItem(item: ShoppingCartItemList) {
  //   let user_id  = item.user_id;

  //   this._api.postTypeRequest('updateItem/'+user_id, item).subscribe((res: any) => {
  //     console.log(res)
  //   }, err => {
  //     console.log(err)
  //   });
  //   this.getTotalPrice();
  // }

  removeItem(item: ShoppingCartItemList, userId : number) {
    console.log(userId)
    this._api.postTypeRequest('users/'+userId+'/Carts', item).subscribe((res: any) => {
      console.log(res)
      window.location.reload();
    }, err => {
      console.log(err)
    });
    this.getTotalPrice();
  }

  updateDB(){

  }


  getProductPrice(item: CartProductInfo , index:number) {
    if (item.price) {
      return this.subTotal = this.cart_data[index].quantity * +item.price;
    } else {
      return this.subTotal = this.cart_data[index].quantity * +item.price;
    }
  }

  getTotalPrice(){
    this.subTotal = 0;
    if(this.data != undefined){
      for (const item of this.data) {
        if (item.price) {
          this.subTotal += this.cart_data[this.index].quantity * +item.price;
          this.index = this.index +1;
        } else {
          this.subTotal += this.cart_data[this.index].quantity * +item.price;
          this.index = this.index +1;
        }
      }
      this.total = this.subTotal;
      this.index = 0;
    }
  }
  

  getOrderSummary() {

    let userId = this.authService.getUser().userID;
    console.log(userId)
    
    this._api.getTypeRequest('users/'+userId+'/Carts').subscribe((res: any) => {
      console.log(res.product_info)
      console.log(res.cart_info)
      this.data = res.product_info
      this.cart_data = res.cart_info
      this.getTotalPrice()
    

      console.log(this.total)
    }, err => {
      console.log(err)
    });

  }

  onCheckOut(user_id : number) {
    console.log(user_id)
    this._api.postTypeRequest('checkout',user_id).subscribe((res: any) => {
      console.log(res)
      if(res == "Checkout")
      {
        alert("결제가 완료되었습니다.");
      }
      this.total = 0
    }, err => {
      console.log(err)
    });

    
  }
}
