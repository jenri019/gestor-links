import { createAction, props } from '@ngrx/store';

/**
 * Acción para establecer propiedades en el estado de los items.
 */
export const set = createAction(
    '[Items] Set',
    props<{ props: { [key: string]: any } }>()
);

/**
 * Acción para restablecer el estado de los items a su valor inicial.
 */
export const reset = createAction('[Items] Reset');

/**
 * Objeto que agrupa todas las acciones relacionadas con los items.
 */
const ItemsActions = {
    set,
    reset
};

export default ItemsActions;