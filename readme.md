# Cable Tweeter
Tweets your ISP when your speed falls below a certain threshold.

Under construction.

To get started, clone the repo

Make a secrets.py file with these values filled in:

```
# Twitter login vars
TOKEN
TOKEN_KEY
CON_SEC
CON_SEC_KEY

# ISP quoted speed
ISP_UP_MAX
ISP_UP_MIN
ISP_DOWN_MAX
ISP_DOWN_MIN
ISP_PING_MAX
ISP_PING_MIN
```

Requires python3.5
Create a virtual environment
For anaconda users: run
```
conda env create
```
from the project directory.
(virtualenv/wrapper users, create a new environment and run pip install -r requirements.txt)

Then:
```
source activate cable_tweeter
```

and

```
python cable_tweeter.py
```

Based on this: https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet/
