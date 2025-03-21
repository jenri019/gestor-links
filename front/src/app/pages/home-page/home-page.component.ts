import { Component } from '@angular/core';
import { ManageItemComponent } from "../../components/manage-item/manage-item.component";

@Component({
  selector: 'app-home-page',
  imports: [ManageItemComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {

}
