# Gemini Trading App

## Pre-requisites

1. A Gemini trading account
2. A server that you can keep on and connected to the internet at all times
   during the bot's runtime.

## Setup

1. In your Gemini account, you need to generate API keys for the application.
   You'll need a public key and an API secret. These should contain a heartbeat, so
   make sure the "heartbeat" option is selected.

2. Copy those keys into a new file named `gem.txt` like so (line by line):
   - `gemini public key with heartbeat:<YOUR_KEY_HERE>`
   - `gemini api secret with heartbeat:<YOUR_KEY_HERE>`
   - `gemini public key without heartbeat:<YOUR_KEY_HERE>`
   - `gemini api secret without heartbeat:<YOUR_KEY_HERE>`

## To run:

### MacOS

Double click the shell file `1_DOUBLE_CLICK_TO_RUN.sh`

### Windows

For now, you'll need to run this via an IDE. I use PyCharm Community version.
Open up the gemini-trading-app project in PyCharm, and add the trader.py file to your
run configuration. Then simply hit the Play button.

## User Inputs

### USD Amount:

The amount of USD you'd like to trade. The bot will use this amount to
calculate the corresponding crypto quantity to be purchased. You must
have sufficient funds in your Gemini account to support this. Otherwise,
the bot will throw an error.

Example - "I want to spend $500 on this trade. My USD amount will be 500."

### Entry Price:

The token price at which you want to buy in. The bot will place a
limit buy at the specified price.

Example - "The price of ETH is at $2000. I want to buy in at $1900. My
entry price will be 1900."

### Sell Price 1 & Stop Limit:

The token price at which you want to sell. Once the limit buy
order has been filled, a limit sell order, as well as a stop
limit order, will be placed for the same quantity calculated at
the beginning of the trade. Once one of the orders gets filled,
the other will cancel automatically. The stop limit order is
REQUIRED for the bot to run.

Example - "My USD amount is 500. My entry price for ETH is 1900. I
want to profit off a $100 jump, so I'll make my sell price 2000. In
case ETH crashes, I want to protect myself from big losses, so I'll
set my stop limit to 1500."

## Other Considerations

1. The computer running the bot MUST NOT LOSE INTERNET CONNECTION.
   This means the computer cannot:<br>
   a. Go to sleep<br>
   b. Shut down<br>
   c. Disconnect from the internet<br>

If any of these things happen, the trade will be cancelled. This
could be dangerous in the event that the user was in the middle of
a trade. For example - your buy order clears, and your sell order
& stop limit get placed. But your computer dies, and the sell orders
get cancelled. If ETH crashes at that point, you're stuck with the loss.

Again - make sure your computer is ALWAYS connected while the bot is running.
