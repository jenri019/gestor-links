import { Component } from '@angular/core';
import { genres } from '../../data/genres';
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
  genres: any[] = genres;
}
