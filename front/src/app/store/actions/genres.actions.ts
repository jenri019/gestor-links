import { createAction, props } from '@ngrx/store';

/**
 * Acción para establecer propiedades en el estado de los generos.
 */
export const set = createAction(
    '[Genres] Set',
    props<{ props: { [key: string]: any } }>()
);

/**
 * Acción para restablecer el estado de los generos a su valor inicial.
 */
export const reset = createAction('[Genres] Reset');

/**
 * Objeto que agrupa todas las acciones relacionadas con los generos.
 */
const GenresActions = {
    set,
    reset
};

export default GenresActions;