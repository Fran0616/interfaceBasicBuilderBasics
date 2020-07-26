#//this code was written with swift not python 
//Lab: User Interface Builder
//the objective of this lab is to use interface builder and the assitance editor to create a basic view,.
//  ViewController.swift
//  interfaceBasicBuilderBasics
//
// 
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var mainLabel: UILabel! //this the label
    @IBAction func changeTitle(_ sender: Any) {//this the button set to create an action
        mainLabel.text = "This app rock!" // when the button is pressed it will print this statement
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}
