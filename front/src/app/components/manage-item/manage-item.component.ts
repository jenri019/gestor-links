import { Component } from '@angular/core';
import { ItemGenresComponent } from "../item-genres/item-genres.component";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-manage-item',
  imports: [
    CommonModule,
    ItemGenresComponent
  ],
  templateUrl: './manage-item.component.html',
  styleUrl: './manage-item.component.scss'
})
export class ManageItemComponent {
  show_form: boolean = false;

  handleChangeFormVisibility() {
    this.show_form = !this.show_form;
  }
}
