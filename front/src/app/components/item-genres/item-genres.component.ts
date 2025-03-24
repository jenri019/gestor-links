import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-item-genres',
  imports: [
    CommonModule
  ],
  templateUrl: './item-genres.component.html',
  styleUrl: './item-genres.component.scss'
})
export class ItemGenresComponent {
  genres: any[] = [
    { id: 1, name: 'Action' },
  ];
}
