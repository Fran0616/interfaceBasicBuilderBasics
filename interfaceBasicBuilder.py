Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> //Lab: User Interface Builder
//the objective of this lab is to use interface builder and the assitance editor to create a basic view,.
//  ViewController.swift
//  interfaceBasicBuilderBasics
//
//  Created by Francisco Francillon on 7/21/20.
//  Copyright © 2020 Francisco Francillon. All rights reserved.
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
