import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from 'express';
import { UserInfo } from '../interface/ec-template.interface';

const USER_INFO_KEY = 'user-info'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  isloggedin = false;

  private setLocalStorage(key: string, value: any) {
    localStorage.setItem(key, JSON.stringify(value));
  }

  private getLocalStorage(key: string) {
    return JSON.parse(localStorage.getItem(key));
  }

  private removeLocalStorage(key: string) {
    localStorage.removeItem(key);
  }
  
  constructor(
  ) {}
  
  getUserDetails() {
      return localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo')||'{}') : null;
  }
  
  setDataInLocalStorage(variableName: string, data: string) {
      localStorage.setItem(variableName, data);
  }


  getUser(): any {
    const userID = window.localStorage.getItem(USER_INFO_KEY);
    if (userID) {
      console.log(userID)
      this.isloggedin = true;
      return JSON.parse(userID);
    }

    return {};
  }

  getUserInfo(){
    return this.getLocalStorage(USER_INFO_KEY);
  }

  saveUserInfo(data: UserInfo){
    this.removeLocalStorage(USER_INFO_KEY);
    this.setLocalStorage(USER_INFO_KEY, data);
  }

  logout() :void{
    this.removeLocalStorage(USER_INFO_KEY);
    this.isloggedin = false;
  }

}
