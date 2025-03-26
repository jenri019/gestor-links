/**
 * Interfaz que representa el estado global de la aplicación.
 */
export interface AppState {
    /**
     * Estado relacionado con las promociones.
     */
    genres: CustomState;
    /**
     * Estado relacionado con los tipos de elementos.
     */
    types: CustomState;
    /**
     * Estado relacionado con los items.
     */
    items: CustomState;
}

export interface CustomState {
    /**
     * Indica si se debe consulatr la informacion.
     */
    flag: boolean;
    /**
     * Listado e elemtos.
     */
    data: any[];
}