import { createAction, props } from '@ngrx/store';

/**
 * Acción para establecer propiedades en el estado de los tipos de elementos.
 */
export const set = createAction(
    '[Types] Set',
    props<{ props: { [key: string]: any } }>()
);

/**
 * Acción para restablecer el estado de los tipos de elementos a su valor inicial.
 */
export const reset = createAction('[Types] Reset');

/**
 * Objeto que agrupa todas las acciones relacionadas con los tipos de elementos.
 */
const TypesActions = {
    set,
    reset
};

export default TypesActions;