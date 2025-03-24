import { Component } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";
import { CardComponent } from "../../components/card/card.component";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home-page',
  imports: [
    CommonModule,
    ManageItemComponent,
    CardComponent
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {
  cards: any[] = [
    {
      id: 1,
      title: 'Card 1',
      description: 'Description 1',
    },
    {
      id: 2,
      title: 'Card 2',
      description: 'Description 2',
    },
    {
      id: 3,
      title: 'Card 3',
      description: 'Description 3',
    }
  ];
}
