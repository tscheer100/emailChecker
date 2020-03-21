# emailChecker

**This is a simple script that I made to text me whenever my uncle Dave e-mails me. The reason why this script is necessary is because I never check my email and my uncle pays me to account for his receipts. Anyone can use this script by editing the vars.json file.**

## Requirements
- A gmail account
- A phone number with a known carrier
- Python must be installed
- (Optional) a service or device to continuously run the python script such as an [orangepi](http://www.orangepi.org/) or a [raspberry pi.](https://www.raspberrypi.org)

## How to use emailChecker
Before running emailChecker, you must edit the vars.json to coorespond to the appropriate variables within the json file. For example, in the vars.json file ```"target": "receive-from@email.com",``` the "Receive-from@email.com" should be changed to whichever email you are expecting to receive from to trigger a text message. In my case, it would be the e-mail of my uncle Dave.

Note: here are the supported carriers that can be changed within the .json file.

```buildoutcfg
    att
    tmobile
    verizon
    sprint
    boost mobile
    cricket
    metroPCS
    tracfone
    US cellular
    virgin
```

### What I've learned from this project
- familizarized myself with linux
- familiarized myself with ssh
- familiarized myself with using git-hub within a terminal
- got aquainted with imapclient
- troubleshooting through issues with finding specific IP addresses in linux
- used PuTTY serial to access the orange pi on windows
