
#!/usr/bin/env python3

import os
import sys

ROOT = sys.argv[1]

OLD = "randomkzn"
NEW = "gnaway0"

changed = 0
checked = 0

for current_root, dirs, files in os.walk(ROOT):
    for filename in files:
        path = os.path.join(current_root, filename)

        try:
            with open(path, "rb") as f:
                data = f.read()

            checked += 1

            old_bytes = OLD.encode()
            new_bytes = NEW.encode()

            if old_bytes not in data:
                continue

            modified = data.replace(old_bytes, new_bytes)

            with open(path, "wb") as f:
                f.write(modified)

            changed += 1
            print(f"[CHANGED] {path}")

        except Exception as e:
            print(f"[SKIPPED] {path}: {e}")

print()
print(f"Files checked: {checked}")
print(f"Files changed: {changed}")
print("Branding patch finished.")
