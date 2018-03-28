# Smug Yoshi

An experimental playground to eventually try to auto-moderate communities.

## Requirements

Python 3.5+, `discord.py`, willingness and patience to learn the Disccord API.

Create a virtual environment and do `pip install -r requirements.txt`.

You will have to generate your own API keys though.

### Bot usage

Commands begin with a `?`.

Blacklist phrases with `?blacklist <phrase>`, the bot will delete messages with them going forward.

Do `?print_blacklist to receive a message via whisper containing
    the current set of bad words.`

Check `yoshi.py` for more.