package com.sbusolarracing.boatscreen;

import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class BoatScreenController {
    @FXML
    private Label rpmLabel, batteryLabel, powerLabel;
    @FXML
    public void setRpmLabel(double rpm){
        rpmLabel.setText("Motor RPM: " + rpm);
    }
    @FXML
    public void setBatteryLabel(double battery){
        batteryLabel.setText("Battery: " + battery + "%");
    }
    @FXML
    public void setPowerLabel(double power){
        powerLabel.setText("Power: " + power + " W");
    }

    /*
    @FXML
    private Label welcomeText;
    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }
     */
}