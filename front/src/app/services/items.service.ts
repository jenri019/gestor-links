import { environment } from './../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ItemResponse } from '../interfaces/items.interface';

@Injectable({
    providedIn: 'root'
})
export class ItemsService {

    constructor(private http: HttpClient) { }

    onGetItems = (): Observable<ItemResponse> => {
        return this.http.get<ItemResponse>(`http://127.0.0.1:8000/api/items/all`);
    }
}