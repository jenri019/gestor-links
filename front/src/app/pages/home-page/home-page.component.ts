import { Component, OnDestroy, OnInit } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";
import { CardComponent } from "../../components/card/card.component";
import { CommonModule } from '@angular/common';
import { Subscription } from 'rxjs';

import { Store } from '@ngrx/store';
import { AppState, CustomState } from '../../interfaces/state.interface';

import { GenresService } from '../../services/genres.service';
import { TypesService } from '../../services/types.service';
import { ItemsService } from '../../services/items.service';

import GenresActions from '../../store/actions/genres.actions';
import TypesActions from '../../store/actions/types.actions';
import ItemsActions from '../../store/actions/items.actions';

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
    items: any[] = [];
    
    private genresSubscription!: Subscription;
    private typesSubscription!: Subscription;
    private itemsSubscription!: Subscription;
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
        private _itemsService: ItemsService,
        private store: Store<AppState>
    ) { }

    ngOnInit(): void {
        this.genresSubscription = this.store.select('genres').subscribe((genres: CustomState) => {
            if (genres.flag) this.onGetGenres();
            else this.genres = genres.data;
        });

        this.typesSubscription = this.store.select('types').subscribe((types: CustomState) => {
            if (types.flag) this.onGetTypes();
            else this.types = types.data;
        });

        this.itemsSubscription = this.store.select('items').subscribe((items: CustomState) => {
            if (items.flag) this.onGetItems();
            else this.items = items.data;
        });
    }

    ngOnDestroy(): void {
        if (this.genresSubscription) {
            this.genresSubscription.unsubscribe();
        }
        if (this.typesSubscription) {
            this.typesSubscription.unsubscribe();
        }
        if (this.itemsSubscription) {
            this.itemsSubscription.unsubscribe();
        }
    }

    onGetGenres = () => {
        this._genresService.onGetGenres().subscribe({
            next: (resp) => {
                this.store.dispatch(GenresActions.set({ props: { data: resp.data, flag: false } }));
                this.store.dispatch(TypesActions.set({ props: { flag: true } }));
            },
            error: (err) => {
            }
        })
    }

    onGetTypes = () => {
        this._typesService.onGetTypes().subscribe({
            next: (resp) => {
                this.store.dispatch(TypesActions.set({ props: { data: resp.data, flag: false } }));
                this.store.dispatch(ItemsActions.set({ props: { flag: true } }));
            },
            error: (err) => {
            }
        })
    }

    onGetItems = () => {
        this._itemsService.onGetItems().subscribe({
            next: (resp) => {
                this.store.dispatch(ItemsActions.set({ props: { data: resp.data, flag: false } }));
            },
            error: (err) => {
            }
        })
    }
}