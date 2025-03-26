import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

import { provideStore } from '@ngrx/store';
import { genresReducer } from './store/reducers/genres.reducer';
import { typesReducer } from './store/reducers/types.reducer';

export const appConfig: ApplicationConfig = {
    providers: [
        provideZoneChangeDetection({ eventCoalescing: true }),
        provideRouter(routes),
        provideHttpClient(),
        // Configuración del store global con reducers para diferentes estados
        provideStore({
            genres: genresReducer,
            types: typesReducer
        })
    ]
};