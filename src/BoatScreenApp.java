import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.scene.layout.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.Circle;
import javafx.scene.paint.Color;
import javafx.scene.text.*;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

import org.bson.Document;

public class BoatScreenApp extends Application {
	
	@Override
	public void start(Stage primaryStage) {

		// Connect to MongoDB
		MongoClient client = MongoClients.create("mongodb+srv://admin:<password>@solarracingdata.hzvpo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
		MongoDatabase database = client.getDatabase("SolarRacingData");
		MongoCollection<Document> boatData = database.getCollection("BoatData");
		
		final double VMIN = 11.374444;
		final double VMAX = 12.73;
		double voltage = 12.73; // Voltage Sensor
		int battery = (int)((voltage - VMIN) / (VMAX - VMIN) * 100);	
		
		double resistance = 10; // Resistance Sensor

		double power = Math.round(voltage * voltage / resistance * 100) / 100; // Solar Power output
		
		double speed = 1.5; // Motor RPM measured by Tachometer
		
		// Speed Graphic
		Circle speedCircle = new Circle();
		speedCircle.setRadius(90);
		speedCircle.setStroke(Color.LIGHTBLUE);
		speedCircle.setStrokeWidth(2);
		speedCircle.setFill(Color.WHITE);
		
		Label speedLabel = new Label("Speed: " + speed + " MPH");
		speedLabel.setTextFill(Color.BLACK);
		speedLabel.setFont(Font.font("San Francisco", 18));
		
		StackPane speedPane = new StackPane();
		speedPane.getChildren().addAll(speedCircle, speedLabel);
		
		
		// Battery Power (percentage) Graphic
		Circle batteryCircle = new Circle();
		batteryCircle.setRadius(90);
		batteryCircle.setStroke(Color.LIGHTBLUE);
		batteryCircle.setStrokeWidth(2);
		batteryCircle.setFill(Color.WHITE);
		
		Label batteryLabel = new Label("Battery: " + battery + "%");
		batteryLabel.setTextFill(Color.BLACK);
		batteryLabel.setFont(Font.font("San Francisco", 18));
		
		StackPane batteryPane = new StackPane();
		batteryPane.getChildren().addAll(batteryCircle, batteryLabel);
		
		
		// Current Graphic
		Circle powerCircle = new Circle();
		powerCircle.setRadius(90);
		powerCircle.setStroke(Color.LIGHTBLUE);
		powerCircle.setStrokeWidth(2);
		powerCircle.setFill(Color.WHITE);
		
		Label powerLabel = new Label("Power: " + power + " W");
		powerLabel.setTextFill(Color.BLACK);
		powerLabel.setFont(Font.font("San Francisco", 18));
		
		StackPane powerPane = new StackPane();
		powerPane.getChildren().addAll(powerCircle, powerLabel);
	
		
		// Title Rectangle
		Rectangle rect = new Rectangle(0, 0, 600, 50);
		rect.setFill(Color.AQUAMARINE);
		
		Label title = new Label("Stony Brook Solar Racing");
		title.setFont(Font.font("Galvji", 30));
		title.setTextFill(Color.BLACK);
		
		StackPane titlePane = new StackPane();
		titlePane.getChildren().addAll(rect, title);

		
		// Background rectangles
		Rectangle rectBackground = new Rectangle(0, 150, 600, 250);
		rectBackground.setFill(Color.LIGHTBLUE);
        
		Rectangle rectMiddle = new Rectangle(0, 50, 600, 100);
		rectMiddle.setFill(Color.LIGHTGREY);
		rectMiddle.setStroke(Color.AQUAMARINE);
		rectMiddle.setStrokeWidth(2);		
		Pane background = new Pane();
		background.getChildren().addAll(rectBackground, rectMiddle);
		
		speedPane.setLayoutX(100-90);
		speedPane.setLayoutY(175-90);
		batteryPane.setLayoutX(300-90);
		batteryPane.setLayoutY(175-90);
		powerPane.setLayoutX(500-90);
		powerPane.setLayoutY(175-90);
		
		Pane overall = new Pane();
		overall.getChildren().addAll(titlePane, background, speedPane, batteryPane, powerPane);
		
		Scene scene = new Scene(overall, 600, 400);
		
		primaryStage.setScene(scene);
		primaryStage.setTitle("Boat Speed App");
		primaryStage.show();

	}
	
	public static void main(String[] args) {
		Application.launch(args);
	}

}
