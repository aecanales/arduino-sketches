const int JOY_X = 0;     // analog pin
const int JOY_Y = 1;     // analog pin
const int JOY_PRESS = 2; // digital pin

void setup()
{
  // When the joystick is pressed, it'll be read as LOW.
  pinMode(JOY_PRESS, INPUT_PULLUP);
  Serial.begin(9600); 
}

void loop()
{
  int x;
  int y;
  int pressed;  

  x = analogRead(JOY_X);
  y = analogRead(JOY_Y);
  pressed = digitalRead(JOY_PRESS);

  Serial.print(x);
  Serial.print(" ");
  Serial.print(y);
  Serial.print(" ");
  Serial.println(pressed);
}