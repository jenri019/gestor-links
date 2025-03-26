import { Component, OnDestroy, OnInit } from '@angular/core';
import { HomePageComponent } from "./pages/home-page/home-page.component";
import { Subscription } from 'rxjs';
import { Store } from '@ngrx/store';
import { AppState, GenresTypes } from './interfaces/state.interface';
import { LoaderComponent } from './templates/loader/loader.component';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-root',
    imports: [
        HomePageComponent,
        CommonModule,
        LoaderComponent
    ],
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit, OnDestroy {
    title = 'Gestor Links';
    isLoadingGenres: boolean = false;
    isLoadingTypes: boolean = false;
    private genresSubscription!: Subscription;
    private typesSubscription!: Subscription;

    constructor(
        private store: Store<AppState>
    ) { }

    ngOnInit(): void {
        this.genresSubscription = this.store.select('genres').subscribe((genres: GenresTypes) => {
            this.isLoadingGenres = genres.flag;
        });
        this.typesSubscription = this.store.select('types').subscribe((types: GenresTypes) => {
            this.isLoadingTypes = types.flag;
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
}