import { Component, OnInit } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";
import { CardComponent } from "../../components/card/card.component";
import { CommonModule } from '@angular/common';
import { LoaderComponent } from "../../templates/loader/loader.component";
import { GenresService } from '../../services/genres.service';

@Component({
    selector: 'app-home-page',
    imports: [
        CommonModule,
        ManageItemComponent,
        CardComponent,
        LoaderComponent
    ],
    templateUrl: './home-page.component.html',
    styleUrl: './home-page.component.scss'
})
export class HomePageComponent implements OnInit {
    isLoading: boolean = false;
    cards: any[] = [
        {
            id: 1,
            title: 'Card 1',
            description: 'Description 1',
        },
        {
            id: 2,
            title: 'Card 2',
            description: 'Description 2',
        },
        {
            id: 3,
            title: 'Card 3',
            description: 'Description 3',
        }
    ];

    constructor(
        private _genresService: GenresService
    ) { }

    ngOnInit(): void {
        console.log('App iniciada');
        this.onGetGenres();
    }

    onGetGenres = () => {
        this.isLoading = true;
        this._genresService.onGetGenres().subscribe({
            next: (resp) => {
                console.log("RESPUESTA DEL SERVICIO");
                console.log(resp);
                this.isLoading = false;
            },
            error: (err) => {
                console.log("ERROR DEL SERVICIO", err);
                this.isLoading = false;
            }
        })
    }
}