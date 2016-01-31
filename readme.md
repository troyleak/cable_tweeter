# Cable Tweeter
Tweets your ISP when your speed falls below a certain threshold. Under active development

Make a secrets.py file with these values:

```
TOKEN
TOKEN_KEY
CON_SEC
CON_SEC_KEY
ISP_UP_MAX
ISP_UP_MIN
ISP_DOWN_MAX
ISP_DOWN_MIN
ISP_PING_MAX
ISP_PING_MIN
```

To get started, clone the repo and run conda env create from the project directory.

```source activate cable_tweeter```

and

```
python cable_tweeter.py
```
