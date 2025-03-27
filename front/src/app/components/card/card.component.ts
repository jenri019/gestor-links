import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { Item } from '../../interfaces/items.interface';

@Component({
  selector: 'app-card',
  imports: [
    CommonModule
  ],
  templateUrl: './card.component.html',
  styleUrl: './card.component.scss'
})
export class CardComponent {
  @Input() card!: Item;
}