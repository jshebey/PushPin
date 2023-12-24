#KEMET MLCC capacitor decoding tables
kemetToleranceTable = [
  ['B', '± 0.10 pF'],
  ['C', '± 0.25 pF'],
  ['D', '± 0.5 pF'],
  ['F', '± 1 %'],
  ['G', '± 2 %'],
  ['J', '± 5 %'],
  ['K', '± 10 %'],
  ['M', '± 20 %']
]

kemetVoltageTable = [
  ['8', '10 V'],
  ['4', '16 V'],
  ['3', '25 V'],
  ['5', '50 V'],
  ['1', '100 V'],
  ['2', '200 V'],
  ['A', '250 V']
]

kemetDielectricTable = [
  ['G', 'NPO'],
  ['R', 'X7R'],
  ['P', 'X5R']
]

#Meritek MA capacitor decoding tables
meritekToleranceTable = [
  ['A', '± 0.05 pF'],
  ['B', '± 0.10 pF'],
  ['C', '± 0.25 pF'],
  ['D', '± 0.5 pF'],
  ['F', '± 1 %'],
  ['G', '± 2 %'],
  ['H', '± 3 %'],
  ['I', '± 10 %'],
  ['J', '± 5 %'],
  ['K', '± 10 %'],
  ['M', '± 20 %']
]

meritekDielectricTable = [
  ['XR', 'X7R'],
  ['CG', 'NPO'],
  ['XF', 'X5R'],
  ['YV', 'Y5V']
]

#TDK C capacitor decoding tables
tdkToleranceTable = [
  ['B', '± 0.10 pF'],
  ['C', '± 0.25 pF'],
  ['D', '± 0.5 pF'],
  ['F', '± 1 %'],
  ['G', '± 2 %'],
  ['J', '± 5 %'],
  ['K', '± 10 %'],
  ['M', '± 20 %']
]

tdkVoltageTable = [
  ['0G', '4 V'],
  ['0J', '6.3 V'],
  ['1A', '10 V'],
  ['1C', '16 V'],
  ['1E', '25 V'],
  ['1V', '35 V'],
  ['1H', '50 V'],
  ['1N', '75 V']
]

#AVX KAM capacitor decoding tables
avxToleranceTable = [
  ['B', '± 0.10 pF'],
  ['C', '± 0.25 pF'],
  ['D', '± 0.5 pF'],
  ['F', '± 1 %'],
  ['G', '± 2 %'],
  ['J', '± 5 %'],
  ['K', '± 10 %'],
  ['M', '± 20 %']
]

avxVoltageTable = [
  ['0G', '4 V'],
  ['0J', '6.3 V'],
  ['1A', '10 V'],
  ['1C', '16 V'],
  ['1E', '25 V'],
  ['1H', '50 V'],
  ['2A', '100 V'],
  ['2D', '200 V'],
  ['2E', '250 V'],
  ['2H', '500 V']
]

avxDielectricTable = [
  ['R7', 'X7R'],
  ['CG', 'NPO'],
  ['S7', 'X7S'],
  ['T7', 'X7T'],
  ['R8', 'X8R'],
  ['L8', 'X8L'],
  ['G8', 'X8G']
]

avxSizeTable = [
  ['03', '0201'],
  ['05', '0402'],
  ['15', '0603'],
  ['21', '0805'],
  ['31', '1206'],
  ['32', '1210'],
  ['42', '1808'],
  ['43', '1812'],
  ['55', '2220']
]

#Darfon MLCC capacitor decoding tables
darfonToleranceTable = [
  ['A', '± 0.05 pF'],
  ['B', '± 0.10 pF'],
  ['C', '± 0.25 pF'],
  ['D', '± 0.5 pF'],
  ['F', '± 1 %'],
  ['G', '± 2 %'],
  ['J', '± 5 %'],
  ['K', '± 10 %'],
  ['M', '± 20 %']
]

darfonSizeTable = [
  ['0603', '0201'],
  ['1005', '0402'],
  ['1608', '0603'],
  ['2012', '0805'],
  ['3216', '1206'],
  ['3225', '1210'],
  ['4520', '1808'],
  ['4532', '1812']
]

darfonVoltageTable = [
  ['B', '4 V'],
  ['C', '6.3 V'],
  ['D', '10 V'],
  ['E', '16 V'],
  ['F', '25 V'],
  ['N', '35 V'],
  ['G', '50 V'],
  ['H', '100 V'],
  ['J', '200 V'],
  ['K', '250 V'],
  ['L', '500 V']
]

#YAGEO RC_L series resistor decoding tables
yageoToleranceTable = [
  ['B', '± 0.1 %'],
  ['D', '± 0.5 %'],
  ['F', '± 1 %'],
  ['J', '± 5 %']
]

yageoVoltageTable = [
  ['0075', '10 V'],
  ['0100', '15 V'],
  ['0201', '25 V'],
  ['0402', '50 V'],
  ['0603', '75 V'],
  ['0805', '150 V'],
  ['1206', '200 V'],
  ['1210', '200 V'],
  ['1218', '200 V'],
  ['2010', '200 V'],
  ['2512', '200 V']
]

yageoPowerTable = [
  ['0075', '0.02 W'],
  ['0100', '0.031 W'],
  ['0201', '0.05 W'],
  ['0402', '0.063 W'],
  ['0603', '0.1 W'],
  ['0805', '0.13 W'],
  ['1206', '0.25 W'],
  ['1210', '0.5 W'],
  ['1218', '1 W'],
  ['2010', '0.75 W'],
  ['2512', '1 W']
]

#Kamaya FRC series resistor decoding tables
kamayaSizeTable = [
  ['16', '0603'],
  ['20', '0805'],
  ['32', '1206']
]

kamayaPowerTable = [
  ['16', '0.063 W'],
  ['20', '0.1 W'],
  ['32', '0.125 W']
]

kamayaVoltageTable = [
  ['16', '1.79 V'],
  ['20', '2.26 V'],
  ['32', '3.53 V']
]

kamayaToleranceTable = [
  ['B', '± 0.1 %'],
  ['D', '± 0.5 %'],
  ['F', '± 1 %'],
  ['J', '± 5 %']
]

#Susumu RR series resistor decoding tables
susumuSizeTable = [
  ['0306', '0201'],
  ['0510', '0402'],
  ['0816', '0603'],
  ['1220', '0805']
]

susumuToleranceTable = [
  ['B', '± 0.1 %'],
  ['D', '± 0.5 %'],
  ['F', '± 1 %']
]

susumuPowerTable = [
  ['0306', '0.05 W'],
  ['0510', '0.063 W'],
  ['0816', '0.063 W'],
  ['1220', '0.1 W']
]

susumuVoltageTable = [
  ['0306', '15 V'],
  ['0510', '25 V'],
  ['0816', '75 V'],
  ['1220', '100 V']
]

#Bourns CRM series resistor decoding tables
bournsToleranceTable = [
  ['F', '± 1 %'],
  ['J', '± 5 %']
]

bournsVoltageTable = [
  ['0805', '150 V'],
  ['1206', '200 V'],
  ['2010', '200 V'],
  ['2512', '300 V']
]

bournsPowerTable = [
  ['0805', '0.25  W'],
  ['1206', '0.5 W'],
  ['2010', '1 W'],
  ['2512', '2 W']
]

#KOA RK73H series resistor decoding tables
koaSizeTable = [
  ['1F', '01005'],
  ['1H', '0201'],
  ['1E', '0402'],
  ['1J', '0603'],
  ['2A', '0805'],
  ['2B', '1206'],
  ['2E', '1210'],
  ['2H', '2010'],
  ['3A', '2512']
]

koaToleranceTable = [
  ['D', '± 0.5 %'],
  ['F', '± 1 %']
]

koaPowerTable = [
  ['1F', '0.03  W'],
  ['1H', '0.05 W'],
  ['1E', '0.1 W'],
  ['1J', '0.1 W'],
  ['2A', '0.25  W'],
  ['2B', '0.25 W'],
  ['2E', '0.5 W'],
  ['2H', '0.75 W'],
  ['3A', '1  W']
]

koaVoltageTable = [
  ['1F', '20 V'],
  ['1H', '25 V'],
  ['1E', '75 V'],
  ['1J', '75 V'],
  ['2A', '150 V'],
  ['2B', '200 V'],
  ['2E', '200 V'],
  ['2H', '200 V'],
  ['3A', '200 V']
]