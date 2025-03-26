/**
 * Interfaz que representa el estado global de la aplicación.
 */
export interface AppState {
    /**
     * Estado relacionado con las promociones.
     */
    genres: GenresTypes;
    /**
     * Estado relacionado con los tipos de elementos.
     */
    types: GenresTypes;
}

export interface GenresTypes {
    /**
     * Indica si se debe consulatr la informacion de los generos.
     */
    flag: boolean;
    /**
     * Lista de generos.
     */
    data: any[];
}