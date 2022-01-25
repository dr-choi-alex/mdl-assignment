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
  data: CartProductInfo[];
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
  //   this.dataService.editShoppingCartItem(item);
  //   this.getOrderSummary();
  // }

  // removeItem(item: ShoppingCartItemList) {
  //   this.dataService.deleteShoppingCartItem(item);
  //   this.data = this.dataService.shoppingCartData;
  //   this.getOrderSummary();
  // }

  getProductPrice(item: CartProductInfo , index:number) {
    if (item.price) {
      return this.subTotal = this.cart_data[index].quantity * +item.price;
    } else {
      return this.subTotal = this.cart_data[index].quantity * +item.price;
    }
  }

  getTotalPrice(item:CartProductInfo, index:number){

  }
  

  getOrderSummary() {

    let b = this.authService.getUser();
    console.log(b)
    
    this._api.postTypeRequest('shopping-cart', b).subscribe((res: any) => {
      console.log(res.product_info)
      console.log(res.cart_info)
      this.data = res.product_info
      this.cart_data = res.cart_info

      this.subTotal = 0;
    
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

      console.log(this.total)
    }, err => {
      console.log(err)
    });

  }

  onCheckOut() {
    alert("결제가 완료되었습니다.");
  }
}
