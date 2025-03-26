import { createReducer, on } from '@ngrx/store';
import TypesActions from '../actions/types.actions';
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
const _typesReducer = createReducer(
    initialState,
    on(TypesActions.set, (state, { props }) => ({
        ...state,
        ...props
    })),
    on(TypesActions.reset, () => {
        return defaultState;
    })
);

/**
 * Función reductor que maneja el estado y las acciones de los generos.
 * @param state Estado actual.
 * @param action Acción despachada.
 * @returns Nuevo estado.
 */
export function typesReducer(state: any, action: any) {
    return _typesReducer(state, action);
}