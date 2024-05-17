// C++ code
//
int temp = A1;


void setup()
{
  pinMode(temp,INPUT);
  pinMode(A2,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int g = analogRead(A1);
  char t[10];
  itoa(g,t, 10);
  delay(500);
  Serial.write(t,4);
}