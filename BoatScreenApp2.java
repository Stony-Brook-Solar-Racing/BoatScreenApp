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
import java.util.*;

public class Chapter16_2 extends Application{
	
	@Override
	
	public void start(Stage primaryStage) {
		
		double VMIN = 11.374444;
		double VMAX = 12.73;
		double voltage = 12.73;											// Voltage Sensor
		int battery = (int)((voltage - VMIN) / (VMAX - VMIN) * 100);	
		
		double current = 10;											// Current Sensor

		double power = Math.round(voltage * current * 100);				// Solar Power output
		power = power / 100;
		
		double speed = 1.5;												// Motor RPM measured by Tachometer

		//graph of power vs time
		
		//System.out.print(Font.getFontNames());
		
		
		//Speed Graphic
		Circle speed_circle = new Circle();
		speed_circle.setRadius(90);
		speed_circle.setStroke(Color.BLUE);
		speed_circle.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		
		Label speedlb = new Label("Speed: " + speed + " mph");
		speedlb.setTextFill(Color.WHITE);
		speedlb.setFont(Font.font("San Francisco", 18));
		
		StackPane speed_pane = new StackPane();
		speed_pane.getChildren().addAll(speed_circle, speedlb);
		
		
		//Battery Power (percentage) Graphic
		Circle battery_circle = new Circle();
		battery_circle.setRadius(90);
		battery_circle.setStroke(Color.BLUE);
		battery_circle.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		
		Label batterylb = new Label("Battery: " + battery + " %");
		batterylb.setTextFill(Color.WHITE);
		batterylb.setFont(Font.font("San Francisco", 18));
		
		StackPane battery_pane = new StackPane();
		battery_pane.getChildren().addAll(battery_circle, batterylb);
		
		
		//Current Graphic
		Circle power_circle = new Circle();
		power_circle.setRadius(90);
		power_circle.setStroke(Color.BLUE);
		power_circle.setFill(Color.BLACK);	//circle.setFill(new Color(0.5, 0.5, 0.5, 1);
		
		Label powerlb = new Label("Power: " + power + " W");
		powerlb.setTextFill(Color.WHITE);
		powerlb.setFont(Font.font("San Francisco", 18));
		
		StackPane power_pane = new StackPane();
		power_pane.getChildren().addAll(power_circle, powerlb);
	
		
		//Title Rectangle
		Rectangle rect = new Rectangle(0, 0, 600, 50);
		rect.setFill(Color.BLACK);
		
		Label title = new Label("Stony Brook Solar Racing");
		title.setFont(Font.font("San Francisco", FontWeight.BOLD, 30));
		title.setTextFill(Color.WHITE);
		
		StackPane title_pane = new StackPane();
		title_pane.getChildren().addAll(rect, title);

		
		// Background rectangles
		Rectangle rect_bg = new Rectangle(0, 150, 600, 250);
		rect_bg.setFill(Color.BLUE);
		
		Rectangle rect_middle = new Rectangle(0, 50, 600, 100);
		rect_middle.setFill(Color.BLACK);
		
		Pane background = new Pane();
		background.getChildren().addAll(rect_bg, rect_middle);
		
		speed_pane.setLayoutX(100-90);
		speed_pane.setLayoutY(175-90);
		battery_pane.setLayoutX(300-90);
		battery_pane.setLayoutY(175-90);
		power_pane.setLayoutX(500-90);
		power_pane.setLayoutY(175-90);
		
		Pane overall = new Pane();
		overall.getChildren().addAll(title_pane, background, speed_pane, battery_pane, power_pane);
		
	

		
		Scene scene = new Scene(overall, 600, 400);
		
		primaryStage.setScene(scene);
		primaryStage.setTitle("Boat Speed App");
		primaryStage.show();

		
	}
	
	public static void main(String[] args) {
		
		Application.launch(args);
		
		
	}
}