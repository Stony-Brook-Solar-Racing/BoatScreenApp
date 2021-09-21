import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.scene.layout.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.Circle;
import javafx.scene.paint.Color;
import javafx.scene.text.*;
import javafx.geometry.*;

public class Chapter16_2 extends Application{
	
	@Override
	
	public void start(Stage primaryStage) {
		
		System.out.print(Font.getFontNames());
		
		StackPane pane = new StackPane();
		
		Circle cspeed = new Circle();
		
		cspeed.setRadius(90);
		cspeed.setStroke(Color.BLUE);
		cspeed.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		Label speedlb = new Label("Speed: " + 1.5);
		speedlb.setTextFill(Color.WHITE);
		speedlb.setFont(Font.font("San Francisco", 18));
		pane.getChildren().addAll(cspeed, speedlb);
		
		
		Circle cbattery = new Circle();
		
		cbattery.setRadius(90);
		cbattery.setStroke(Color.BLUE);
		cbattery.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		Label batterylb = new Label("Battery Power: " + 5);
		batterylb.setTextFill(Color.WHITE);
		batterylb.setFont(Font.font("San Francisco", 18));
		
		StackPane pane2 = new StackPane();
		pane2.getChildren().addAll(cbattery, batterylb);
		
		Circle ccurrent = new Circle();
		
		ccurrent.setRadius(90);
		ccurrent.setStroke(Color.BLUE);
		ccurrent.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		Label currentlb = new Label("Current: " + 10);
		currentlb.setTextFill(Color.WHITE);
		currentlb.setFont(Font.font("San Francisco", 18));
		
		StackPane pane3 = new StackPane();
		pane3.getChildren().addAll(ccurrent, currentlb);
	
		StackPane pane4 = new StackPane();
		Rectangle rect = new Rectangle(0, 0, 600, 50);
		rect.setFill(Color.BLACK);
		
		Label title = new Label("Solar Racing Data");
		title.setFont(Font.font("San Francisco", FontWeight.BOLD, 30));
		title.setTextFill(Color.WHITE);
		pane4.getChildren().addAll(rect, title);

		Rectangle rect_bg = new Rectangle(0, 150, 600, 250);
		rect_bg.setFill(Color.BLUE);
		Pane pane5 = new Pane();
		Rectangle rect_middle = new Rectangle(0, 50, 600, 100);
		rect_middle.setFill(Color.BLACK);
		pane5.getChildren().addAll(rect_bg, rect_middle);
		
		pane.setLayoutX(100-90);
		pane.setLayoutY(175-90);
		pane2.setLayoutX(300-90);
		pane2.setLayoutY(175-90);
		pane3.setLayoutX(500-90);
		pane3.setLayoutY(175-90);
		
		Pane overall = new Pane();
		overall.getChildren().addAll(pane4, pane5, pane, pane2, pane3);
		
		

		
		Scene scene = new Scene(overall, 600, 400);
		
		primaryStage.setScene(scene);
		primaryStage.setTitle("Boat Speed App");
		primaryStage.show();

		
	}
	
	public static void main(String[] args) {
		
		Application.launch(args);
		
		
	}
}