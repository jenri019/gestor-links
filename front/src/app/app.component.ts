import { Component } from '@angular/core';
import { HomePageComponent } from "./pages/home-page/home-page.component";

@Component({
  selector: 'app-root',
  imports: [HomePageComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Gestor Links';
}