import { Component, OnDestroy, OnInit } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";
import { CardComponent } from "../../components/card/card.component";
import { CommonModule } from '@angular/common';
import { LoaderComponent } from "../../templates/loader/loader.component";
import { GenresService } from '../../services/genres.service';
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState, Genres } from '../../interfaces/state.interface';
import GenresActions from '../../store/actions/genres.actions';

@Component({
    selector: 'app-home-page',
    imports: [
        CommonModule,
        ManageItemComponent,
        CardComponent
    ],
    templateUrl: './home-page.component.html',
    styleUrl: './home-page.component.scss'
})
export class HomePageComponent implements OnInit, OnDestroy {
    isLoading: boolean = false;
    genres: any[] = [];
    private genresSubscription!: Subscription;
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
        private _genresService: GenresService,
        private store: Store<AppState>
    ) { }

    ngOnInit(): void {
        this.genresSubscription = this.store.select('genres').subscribe((genres: Genres) => {
            if (genres.flag) this.onGetGenres();
            else this.genres = genres.data;
        });
    }

    ngOnDestroy(): void {
        if (this.genresSubscription) {
            this.genresSubscription.unsubscribe();
        }
    }

    onGetGenres = () => {
        this.isLoading = true;
        this._genresService.onGetGenres().subscribe({
            next: (resp) => {
                this.store.dispatch(GenresActions.set({ props: { data: resp.data, flag: false } }));
                this.isLoading = false;
            },
            error: (err) => {
                this.isLoading = false;
            }
        })
    }
}