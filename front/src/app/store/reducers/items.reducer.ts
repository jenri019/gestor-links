import { createReducer, on } from '@ngrx/store';
import ItemsActions from '../actions/items.actions';
import { CustomState } from '../../interfaces/state.interface';

const defaultState: CustomState = {
    flag: true,
    data: []
};

/**
 * Estado inicial para los generos.
 */
const initialState: CustomState = defaultState;

/**
 * Reductor para manejar las acciones relacionadas con los generos.
 */
const _itemsReducer = createReducer(
    initialState,
    on(ItemsActions.set, (state, { props }) => ({
        ...state,
        ...props
    })),
    on(ItemsActions.reset, () => {
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
    return _itemsReducer(state, action);
}