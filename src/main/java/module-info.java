module com.sbusolarracing.boatscreen {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires org.mongodb.driver.sync.client;
    requires org.mongodb.driver.core;
    requires org.mongodb.bson;

    opens com.sbusolarracing.boatscreen to javafx.fxml;
    exports com.sbusolarracing.boatscreen;
}