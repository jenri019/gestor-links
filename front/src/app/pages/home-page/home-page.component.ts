import { Component, OnDestroy, OnInit } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";
import { CardComponent } from "../../components/card/card.component";
import { CommonModule } from '@angular/common';
import { GenresService } from '../../services/genres.service';
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState, GenresTypes } from '../../interfaces/state.interface';
import GenresActions from '../../store/actions/genres.actions';
import { TypesService } from '../../services/types.service';
import TypesActions from '../../store/actions/types.actions';

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
    types: any[] = [];
    
    private genresSubscription!: Subscription;
    private typesSubscription!: Subscription;
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
        private _typesService: TypesService,
        private store: Store<AppState>
    ) { }

    ngOnInit(): void {
        this.genresSubscription = this.store.select('genres').subscribe((genres: GenresTypes) => {
            if (genres.flag) this.onGetGenres();
            else this.genres = genres.data;
        });

        this.typesSubscription = this.store.select('types').subscribe((types: GenresTypes) => {
            if (types.flag) this.onGetTypes();
            else this.types = types.data;
        });
    }

    ngOnDestroy(): void {
        if (this.genresSubscription) {
            this.genresSubscription.unsubscribe();
        }
        if (this.typesSubscription) {
            this.typesSubscription.unsubscribe();
        }
    }

    onGetGenres = () => {
        this.isLoading = true;
        this._genresService.onGetGenres().subscribe({
            next: (resp) => {
                this.store.dispatch(GenresActions.set({ props: { data: resp.data, flag: false } }));
            },
            error: (err) => {
            }
        })
    }

    onGetTypes = () => {
        this.isLoading = true;
        this._typesService.onGetTypes().subscribe({
            next: (resp) => {
                this.store.dispatch(TypesActions.set({ props: { data: resp.data, flag: false } }));
            },
            error: (err) => {
            }
        })
    }
}