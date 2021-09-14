Can read from a file or stdin and detects FIX messages within
each line of text.

## Usage
```
$ ./fixprinter.py
usage: fixprinter.py [-h] [-f FILENAME] [--stdin] [--spec SPEC]

A pretty printer of fix messages using the quickfix library (Must specify
either --filename or --stdin)

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        a file containing fix messages to display
  --stdin               read lines from stdin instead of a file
  --spec SPEC           loads the provided XML specification (presumably from
                        the quickfix library) WARNING! The output will be
                        fairly useless without a spec
```

## Example
```
╰─ $./fix_parser.py --/fix_lib/spec FIX42.xml --f fix_messages

Output:

Found FIX message at line 1: 8=FIX.4.4|9=148|35=D|34=1080|49=TESTBUY1|52=20180920-18:14:19.508|56=TESTSELL1|11=636730640278898634|15=USD|21=2|38=7000|40=1|54=1|55=MSFT|60=20180920-18:14:19.492|10=092|

BeginString (8): FIX.4.4
BodyLength (9): 148
MsgSeqNum (34): 1080
MsgType (35): NewOrderSingle (D)
SenderCompID (49): TESTBUY1
SendingTime (52): 20180920-18:14:19.508
TargetCompID (56): TESTSELL1
ClOrdID (11): 636730640278898634
Currency (15): USD
HandlInst (21): AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK (2)
OrderQty (38): 7000
OrdType (40): MARKET (1)
Side (54): BUY (1)
Symbol (55): MSFT
TransactTime (60): 20180920-18:14:19.492
CheckSum (10): 092

Found FIX message at line 2: 8=FIX.4.4|9=289|35=8|34=1090|49=TESTSELL1|52=20180920-18:23:53.671|56=TESTBUY1|6=113.35|11=636730640278898634|14=3500.0000000000|15=USD|17=20636730646335310000|21=2|31=113.35|32=3500|37=20636730646335310000|38=7000|39=1|40=1|54=1|55=MSFT|60=20180920-18:23:53.531|150=F|151=3500|453=1|448=BRK2|447=D|452=1|10=151|

BeginString (8): FIX.4.4
BodyLength (9): 289
MsgSeqNum (34): 1090
MsgType (35): ExecutionReport (8)
SenderCompID (49): TESTSELL1
SendingTime (52): 20180920-18:23:53.671
TargetCompID (56): TESTBUY1
AvgPx (6): 113.35
ClOrdID (11): 636730640278898634
CumQty (14): 3500.0000000000
Currency (15): USD
ExecID (17): 20636730646335310000
HandlInst (21): AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK (2)
LastPx (31): 113.35
LastQty (32): 3500
OrderID (37): 20636730646335310000
OrderQty (38): 7000
OrdStatus (39): PARTIALLY_FILLED (1)
OrdType (40): MARKET (1)
Side (54): BUY (1)
Symbol (55): MSFT
TransactTime (60): 20180920-18:23:53.531
ExecType (150): TRADE (F)
LeavesQty (151): 3500
NoPartyIDs (453): count = 1
  PartyIDSource (447): PROPRIETARY_CUSTOM_CODE (D)
  PartyID (448): BRK2
  PartyRole (452): EXECUTING_FIRM (1)
CheckSum (10): 151

Found FIX message at line 3: 8=FIX.4.4|9=75|35=A|34=1092|49=TESTBUY1|52=20180920-18:24:59.643|56=TESTSELL1|98=0|108=60|10=178|

BeginString (8): FIX.4.4
BodyLength (9): 75
MsgSeqNum (34): 1092
MsgType (35): Logon (A)
SenderCompID (49): TESTBUY1
SendingTime (52): 20180920-18:24:59.643
TargetCompID (56): TESTSELL1
EncryptMethod (98): NONE (0)
HeartBtInt (108): 60
CheckSum (10): 178

Found FIX message at line 4: 8=FIX.4.2|9=163|35=D|34=972|49=TESTBUY3|52=20190206-16:25:10.403|56=TESTSELL3|11=141636850670842269979|21=2|38=100|40=1|54=1|55=AAPL|60=20190206-16:25:08.968|207=TO|6000=TEST1234|10=106|

BeginString (8): FIX.4.2
BodyLength (9): 163
MsgSeqNum (34): 972
MsgType (35): NewOrderSingle (D)
SenderCompID (49): TESTBUY3
SendingTime (52): 20190206-16:25:10.403
TargetCompID (56): TESTSELL3
ClOrdID (11): 141636850670842269979
HandlInst (21): AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK (2)
OrderQty (38): 100
OrdType (40): MARKET (1)
Side (54): BUY (1)
Symbol (55): AAPL
TransactTime (60): 20190206-16:25:08.968
SecurityExchange (207): TO
Unknown (6000): TEST1234
CheckSum (10): 106

Found 4 messages
```
