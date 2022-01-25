import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ShoppingCartItem, CartProductInfo } from '../interface/ec-template.interface';
import { AuthService } from '../services/auth.service';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.scss']
})
export class ShoppingCartComponent implements OnInit {
  data: ShoppingCartItem[] = [];
  productList: CartProductInfo[];
  // order summary
  subTotal = 0;
  tax = 0;
  total = 0;

  constructor(
    private dataService: DataService,
    private authService: AuthService,
    private _api: ApiService
    ) {}

  ngOnInit() {
    // this.data = this.dataService.shoppingCartData;
    this.getOrderSummary();
  }

  updateItem(item: ShoppingCartItem) {
    this.dataService.editShoppingCartItem(item);
    this.getOrderSummary();
  }

  removeItem(item: ShoppingCartItem) {
    this.dataService.deleteShoppingCartItem(item);
    this.data = this.dataService.shoppingCartData;
    this.getOrderSummary();
  }

  getTotalPrice(item: ShoppingCartItem) {
    if (item.product.onSale) {
      return item.quantity * +item.product.salePrice;
    } else {
      return item.quantity * +item.product.costPrice;
    }
  }
  

  getOrderSummary() {
    this.subTotal = 0;

    let b = this.authService.getUser();
    console.log(b)
    
    this._api.postTypeRequest('shopping-cart', b).subscribe((res: any) => {
      console.log(res.product_info)
      console.log(res.cart_info)
      this.productList = res.product_info
      this.data = res.product_info

     
    }, err => {
      console.log(err)
    });


    for (const i of this.data) {
      if (i.product.onSale) {
        this.subTotal = this.subTotal + +i.product.salePrice * i.quantity;
      } else {
        this.subTotal = this.subTotal + +i.product.costPrice * i.quantity;
      }
    }
    this.total = this.subTotal;
  }

  onCheckOut() {
    alert("결제가 완료되었습니다.");
  }
}
