# FGO Wiki Parser
A Python script used to transform quest .JSON files from the [Atlas Academy Database](https://apps.atlasacademy.io/db/) into wiki markup for the [Fate/Grand Order Wiki](https://fategrandorder.fandom.com), with some edits required by the user to format to wiki standards.

To use, place the .JSON files you want parsed inside an "inputs" directory, and then run in the command line:

```python reader.py```

For the script to work properly, the .JSON files should be the `nice` versions instead of the `raw` ones. The code's designed to assume that the data language is JP, but it should still mostly work even if it's in a different language.