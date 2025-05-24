#!/bin/bash
cd "$(dirname "$0")"
# echo 'pwd; venv/bin/python3 trader.py' > run_trader.command; chmod +x run_trader.command; open run_trader.command
cd venv/bin
python3 ../../trader.py