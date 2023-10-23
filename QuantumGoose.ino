//Arduino code for the Quantum Goose project
// Written in VScode, not validated in Arduino IDE
// incomplete, not tested

#include <Stepper.h>
#include <OneButton.h>


const int motorPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
const int stepperPin = 10;
const int dirPin = 11;
const int enPin = 13;

const int buttonPin = 11;

class Goose {
    private:
        int motorPins[8];
        int stepperPin;
        int buttonPin;

        int coordinate;
        int getButtonState;

        int CalculateCoordinate(){
            int currentPosition;
            currentPosition = stepper.getPosition();
            return currentPosition;
        }
        
    public:
        Goose(int motorPins, int stepperPin, int buttonPin){

            this->motorPins = motorPins;
            this->stepperPin = stepperPin;
            this->buttonPin = buttonPin;
            this->coordinate = CalculateCoordinate();
        }


    void geeseSpin(int coordinate, int getButtonState){
        for(int i = 0; i < 8; i++){
            digitalWrite(motorPins[i], HIGH);
        }
    }

    int getButtonState(){
        return digitalRead(buttonPin);
    }

    int pressedButton(){
        if(getButtonState == HIGH){
            return coordinate;
        }
    }

    void stepperSpinManager(int getButtonState){

        if(getButtonState == HIGH){

            // digitalWrite(dirPin, HIGH);
            // digitalWrite(enPin, LOW);
            // digitalWrite(stepperPin, HIGH);
            // delay(10); 
            // digitalWrite(stepperPin, LOW);
            // delay(10);
            // digitalWrite(enPin, HIGH);
        }
    }
};

Stepper stepper(stepperPin, dirPin, enPin, 200);
Goose goose = Goose(motorPins, stepperPin, buttonPin);

void setup(){
    for(int i = 0; i < 8; i++){
    pinMode(motorPins[i], OUTPUT);
    }

    pinMode(stepperPin, OUTPUT);
    pinMode(dirPin, OUTPUT);
    pinMode(enPin, OUTPUT);
    pinMode(buttonPin, INPUT);
}

void loop(){

}
