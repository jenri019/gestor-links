import { createReducer, on } from '@ngrx/store';
import GenresActions from '../actions/genres.actions';
import { GenresTypes } from '../../interfaces/state.interface';

const defaultState: GenresTypes = {
    flag: true,
    data: []
};

/**
 * Estado inicial para los generos.
 */
const initialState: GenresTypes = defaultState;

/**
 * Reductor para manejar las acciones relacionadas con los generos.
 */
const _genresReducer = createReducer(
    initialState,
    on(GenresActions.set, (state, { props }) => ({
        ...state,
        ...props
    })),
    on(GenresActions.reset, () => {
        return defaultState;
    })
);

/**
 * Función reductor que maneja el estado y las acciones de los generos.
 * @param state Estado actual.
 * @param action Acción despachada.
 * @returns Nuevo estado.
 */
export function genresReducer(state: any, action: any) {
    return _genresReducer(state, action);
}