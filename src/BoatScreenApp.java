import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.util.Duration;
import javafx.scene.layout.*;
import javafx.scene.shape.Rectangle;
import javafx.scene.shape.Circle;
import javafx.scene.paint.Color;
import javafx.scene.text.*;

import static com.mongodb.client.model.Sorts.*;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

import org.bson.Document;

public class BoatScreenApp extends Application {

	// Sensor readings
	double voltage = 12.73; // Voltage Sensor
	double resistance = 10; // Resistance Sensor
	double rpm = 1.5; // Motor RPM measured by Tachometer
	String mongoURI = "";
	
	@Override
	public void start(Stage primaryStage) {

		try {
			File auth = new File("auth.txt");
			Scanner input = new Scanner(auth);
			mongoURI = input.nextLine();
			input.close();
		} catch (FileNotFoundException e) {
			System.out.println("File was not found.");
			e.printStackTrace();
			return;
		}

		// Connect to MongoDB
		MongoClient client = MongoClients.create(mongoURI);
		MongoDatabase database = client.getDatabase("SolarRacingData");
		MongoCollection<Document> rpmData = database.getCollection("RPM");
		
		final double VMIN = 11.374444;
		final double VMAX = 12.73;
		int battery = (int)((voltage - VMIN) / (VMAX - VMIN) * 100);	

		double power = Math.round(voltage * voltage / resistance * 100) / 100; // Solar Power output
		
		// Speed Graphic
		Circle rpmCircle = new Circle();
		rpmCircle.setRadius(90);
		rpmCircle.setStroke(Color.LIGHTBLUE);
		rpmCircle.setStrokeWidth(2);
		rpmCircle.setFill(Color.WHITE);
		
		Label rpmLabel = new Label("Motor RPM: " + rpm);
		rpmLabel.setTextFill(Color.BLACK);
		rpmLabel.setFont(Font.font("San Francisco", 18));
		
		StackPane rpmPane = new StackPane();
		rpmPane.getChildren().addAll(rpmCircle, rpmLabel);
		
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
		
		rpmPane.setLayoutX(100-90);
		rpmPane.setLayoutY(175-90);
		batteryPane.setLayoutX(300-90);
		batteryPane.setLayoutY(175-90);
		powerPane.setLayoutX(500-90);
		powerPane.setLayoutY(175-90);
		
		Pane overall = new Pane();
		overall.getChildren().addAll(titlePane, background, rpmPane, batteryPane, powerPane);

		// Setup Auto-Update
		Timeline update = new Timeline(
			new KeyFrame(
				Duration.seconds(1),
				new EventHandler<ActionEvent>() {
					@Override
					public void handle(ActionEvent event) {
						// Update RPM
						double newRPM = Double.valueOf(rpmData.find().sort(descending("_id")).first().get("RPM").toString());
						if (newRPM != rpm) {
							rpmLabel.setText("Motor RPM: " + newRPM);
							rpm = newRPM;
						}
						// TODO: Update Battery
						// TODO: Update Power
					}
				}
			)
		);
		update.setCycleCount(Timeline.INDEFINITE);
		update.play();

		// Set scene
		
		Scene scene = new Scene(overall, 600, 400);
		
		primaryStage.setScene(scene);
		primaryStage.setTitle("Boat Speed App");
		primaryStage.show();

	}
	
	public static void main(String[] args) {
		Application.launch(args);
	}

}
