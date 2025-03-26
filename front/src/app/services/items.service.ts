import { environment } from './../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ItemsService {

    constructor(private http: HttpClient) { }

    onGetItems = (): Observable<any> => {
        return this.http.get<any>(`http://127.0.0.1:8000/api/items/all`);
    }
}