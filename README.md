# interfaceBasicBuilderBasics
use the interface builder and the assistance editor to create a basic view


Objective: 
The purpose of this lab is to use the interface builder and the assistance editor to create a basic view. In this lab I will use an outlet and a button to create an action when the button is clicked. 
Ukit: 
I will import the UIKit which is used to construct and manage the graphical, event-driven user interface for an IOS device. It provides the window and view architecture for implementing an interface, the event handling infrastructure for delivering multi-Touch and other types of input to your app. Some additional features offered by this framework includes animation support, document support, drawing and printing support. 
ViewController: 
The view controllers manage the interface using view controllers and facilitate navigation around the app's content. 

The view controller consists of the button object and the label. They are both types within the UIkit framework. The UIButton is connected with the storyboard as an interface builder outlet. And the label is set as an action. 

Function: 
The @IBOutlet font changeTittle consist of the mainLabel.text = “this app rock” which will cause the app to display “this app rocks” when the button is press

The method viewDidLoad is called after the view control has loaded. This method can perform additional initialization on views, but in this lab there was no need for it.
