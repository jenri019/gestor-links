import { Component, HostBinding, Input } from '@angular/core';

@Component({
  selector: 'app-loader',
  imports: [],
  templateUrl: './loader.component.html',
  styleUrl: './loader.component.scss'
})
export class LoaderComponent {
  @Input() color: string = '#3f51b5'; // Color por defecto (puedes cambiarlo)
  @Input() thickness: string = '3px'; // Grosor del spinner
  @Input() speed: string = '1s'; // Velocidad de animación

  @HostBinding('style.display') display = 'block';
  @HostBinding('style.width') width = '100%';
  @HostBinding('style.height') height = '100%';
}
