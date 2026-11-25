import os

# Snooze Button Roast: the alarm clock is not a helper, it is a spectator
# that rings at 6 AM on a Saturday just to watch its owner lose to a button.
ENTRY = "Saturday, 6 AM: my alarm clock rings, not to wake me, but to get a front-row seat while I lose an argument with a button."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    # One line only, no trailing newline: the gate counts characters.
    f.write(ENTRY)
