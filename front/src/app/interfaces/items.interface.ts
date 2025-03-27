export interface ItemResponse {
    data: any[];
    message: string;
    status: number;
}

export interface Item {
    id: number;
    title: string;
    type: string;
    description: string;
    url: string;
    current_chapter: number;
    on_going: boolean;
    genres: ItemGenres;
}

interface ItemGenres {
    ids: number[];
    names: string;
}