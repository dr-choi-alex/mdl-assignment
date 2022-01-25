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
  usertype : string;

  private setSessionStorage(key: string, value: any) {
    sessionStorage.setItem(key, JSON.stringify(value));
  }

  private getSessionStorage(key: string) {
    return JSON.parse(sessionStorage.getItem(key));
  }

  private removeSessionStorage(key: string) {
    sessionStorage.removeItem(key);
  }
  
  constructor(
  ) {}
  
  getUserDetails() {
      return sessionStorage.getItem('userInfo') ? JSON.parse(sessionStorage.getItem('userInfo')||'{}') : null;
  }
  
  setDataInLocalStorage(variableName: string, data: string) {
    sessionStorage.setItem(variableName, data);
  }


  getUser(): any {
    const userID = window.sessionStorage.getItem(USER_INFO_KEY);
    if (userID) {
      //console.log(userID)
      return JSON.parse(userID);
    }

    return {};
  }

  getUserInfo(){
    return this.getSessionStorage(USER_INFO_KEY);
  }

  saveUserInfo(data: UserInfo){
    this.removeSessionStorage(USER_INFO_KEY);
    this.setSessionStorage(USER_INFO_KEY, data);
  }

  logout() :void{
    this.removeSessionStorage(USER_INFO_KEY);
    this.isloggedin = false;
  }

}
