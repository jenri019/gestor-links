/**
 * Interfaz que representa el estado global de la aplicación.
 */
export interface AppState {
    /**
     * Estado relacionado con las promociones.
     */
    genres: Genres;
}

export interface Genres {
    /**
     * Indica si se debe consulatr la informacion de los generos.
     */
    flag: boolean;
    /**
     * Lista de generos.
     */
    data: any[];
}