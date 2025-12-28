# DM Data Processing & Visualization

A small Python app to load Discord DM JSON exports, extract and process messages, count word usage per user, and visualize messages over time.

---

## Features

- **Load** JSON message exports from `input_data/`
- **Process** messages into simplified records (`sender`, `timestamp`, `message`)
- **Count** word usage per user and save results to `output_data/dm_message_counts.json`
- **Visualize** monthly message counts per user using `matplotlib`

---

## Prerequisites

- Python 3.8+
- Packages: `pandas`, `matplotlib`
- On Windows, ensure `tkinter` is available (usually included with Python)

Install the required packages:

```
pip install pandas matplotlib
```

---

## Run the app

From the project root:

```
python main.py
```

This launches the Tkinter GUI.

---

## Usage (GUI)

1. In the GUI, enter a JSON filename (e.g. `dms.json`) and click **Load JSON**. Files are read from `input_data/`.
2. (Optional) Set "entry process count" to limit the number of processed messages (default = all).
3. Click **Process** to prepare the simplified dataset.
4. Click **Count** under "Count different messages" to compute per-user word counts. Output saved to `output_data/dm_message_counts.json`.
5. Click **Count** under "Map messages over time" to display monthly message counts per user (matplotlib plot).

> The input JSON should be arranged in Discord's message format, from a program like DiscordChatExporter:
>
> ```json
>   {
>       "id": "459684",
>       "type": "Default",
>       "timestamp": "2018-01-13T19:38:43.063+00:00",
>       "timestampEdited": null,
>       "callEndedTimestamp": null,
>       "isPinned": false,
>       "content": "Message",
>       "author": {
>           "id": "456456759",
>           "name": "username",
>           "discriminator": "0000",
>           "nickname": "User",
>           "color": null,
>           "isBot": false,
>           "roles": [],
>           "avatarUrl": "https://cdn.discordapp.com/avatars/53453/avatar.png"
>       },
>       "attachments": [],
>       "embeds": [],
>       "stickers": [],
>       "reactions": [],
>       "mentions": [],
>       "inlineEmojis": []
>   },
> ```

---

## Important files

- `main.py` — app entry point
- `interface.py` — Tkinter UI
- `data_processing.py` — JSON loading & processing
- `data_analysis.py` — word counts & plotting
- `input_data/` — place your JSON files here
- `output_data/` — outputs (e.g., `dm_message_counts.json`)

---

## Troubleshooting

- FileNotFoundError when loading: ensure the filename exists in `input_data/` and include the `.json` extension (the GUI will append it if missing).
- If plots do not show, check your matplotlib backend or run outside environments that block GUIs.

---

## Tips for Developers

You can import and call functions directly:

```python
from data_processing import load_json, extract_processing_info
from data_analysis import count_words, messages_over_time
```

---