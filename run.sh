echo ""
echo "-- Life360 Credentials --"
echo "Username: "
read username

echo "Password: "
read -s password

echo ""
echo "How long do you want to collect data?"
echo "Select Units:"
echo "1) minutes"
echo "2) hours"
echo "3) days"
echo ""
echo "Select by inputting the desired number"
read unit

echo ""
echo "How many?"
echo "Input a number value: "
read amount

echo ""
echo "Initiating Program"
echo ""

nohup python main.py $username $password $amount $unit 
