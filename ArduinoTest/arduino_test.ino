#include <Arduino.h>

//// Подключение светодиода с ШИМ
//bool done = false;
//
//const int PinLed = 9;
//
//void setup() {
//    // put your setup code here, to run once:
//    pinMode(PinLed, OUTPUT);
//}
//
//void loop() {
//    // put your main code here, to run repeatedly:
//    if(!done){
//        digitalWrite(PinLed, 1);
//        delay(1000);
//
//        for (int i = 0; i < 255; ++i) {
//            analogWrite(PinLed, i);
//            delay(10);
//        }
//    }
//    done = true;
//}

//// Подключение DHT11
//#include "libraries/DHT/DHT.cpp"
//
//const int PinDHT = 2;
//double humidity, temperature;
//
//DHT dht(PinDHT, DHT11);
//
//void setup() {
//    Serial.begin(9600);
//    dht.begin();
//}
//
//void loop() {
//    humidity = dht.readHumidity();
//    temperature = dht.readTemperature();
//
//
//    Serial.print("Humidity: ");
//    Serial.print(humidity);
//    Serial.print("\t");
//    Serial.print("Temperature: ");
//    Serial.print(temperature);
//    Serial.print('\n');
//
//    delay(1000);
//}


//// Подключение дисплея LCD 1602
//#include "LiquidCrystal.h"
//
//const int PinRS{2}, PinE{3}, PinD4{4}, PinD5{5}, PinD6{6}, PinD7{7};
//
//LiquidCrystal lcd(PinRS, PinE, PinD4, PinD5, PinD6, PinD7);
//
//void setup() {
//    lcd.begin(16, 2);
//    lcd.setCursor(0, 0);
//    lcd.print("Hello World!");
//    lcd.setCursor(0, 1);
//    lcd.print("Maksim Nakhodnov");
//}
//
//void loop() {
//}