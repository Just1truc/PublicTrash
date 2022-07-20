import { Component, OnInit } from '@angular/core';
import { Clipboard } from '@angular/cdk/clipboard';

@Component({
  selector: 'app-gen-key',
  templateUrl: './gen-key.component.html',
  styleUrls: ['./gen-key.component.scss']
})
export class GenKeyComponent implements OnInit {

  public key: string = '';

  constructor(
    private _clipoard : Clipboard
  ) { }

  ngOnInit(): void {
  }

  public copyToClipboard() : void {
    this._clipoard.copy(this.key);
  }

  public generateKey() : void {
    this.key = 'ofnezjjfjkefzejofjozejofezjofezhgjzrgbjjjojjoiojiojiojiojiojiljjojojoijojjioijoozrgjoeovuirehguirhugrieqhgurioevhurieovhruioeqhgurioeoshgutioghutrik';
  }

}
