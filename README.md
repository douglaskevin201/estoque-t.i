# Estoque T.I.

Terminal-based IT inventory management system, built with Python (OOP) and SQLAlchemy, persisted in SQLite.

## Where this came from

Practice project for a Python + OOP + SQLAlchemy course, pointed at a real problem: my workplace had no IT inventory control at all. It's both a study tool and something I plan to use at work.

## Scope

Intentionally minimal for this phase — no movement history, no supplier data, no cost tracking. Just correct, validated CRUD on `Item` and `ItemHardware`. Hardware is the first category modeled this way; more are planned.

## What's done

- Register items — category, name, quantity, status (Lixo / Funcionando / Conserto), full input validation
- List items — all, or filtered by hardware category
- Adjust stock — increase/decrease with guards against negative numbers and over-removal
- Delete an item
- `ItemHardware` — 1:1 relationship to `Item` via shared PK/FK (`item_id`), avoiding data duplication
- Error handling throughout — every DB operation wrapped in try/except with rollback; the program never crashes
- Proper entry point (`if __name__ == "__main__"`) and pinned `requirements.txt`
- No machine-specific files tracked (removed a hardcoded local shortcut script)

## Tech stack

Python, SQLAlchemy (ORM), SQLite

## Running it

```
git clone https://github.com/douglaskevin201/estoque-t.i
cd estoque-t.i
pip install -r requirements.txt
python menu.py
```

The database (`estoque.db`) is created automatically on first run.

## Technical decisions

- **IDs aren't reused after deletion** — SQLite/SQLAlchemy's default; kept intentionally in case other tables reference these IDs later.
- **`models.py` and `menu.py` are separate** — business logic and data classes isolated from the interaction layer.
- **No API yet, on purpose** — consolidating Python + SQLAlchemy fundamentals before adding one.

## Roadmap

- [x] Core data model (Item, ItemHardware) with SQLAlchemy
- [x] Full CRUD with validation and error handling
- [x] List filtering (all items / hardware only)
- [x] Pinned dependencies and proper entry point
- [ ] Additional category classes beyond ItemHardware
- [ ] API layer to host the database elsewhere
- [ ] Broader search (by name, by status)
- [ ] Application/interface layer for daily use at work
- [ ] Proper install/run flow, off the local .bat shortcut

## On AI usage

Claude was used as a study aid, with a limited role: reviewing code I wrote, pointing out bugs and redundant logic — never writing the solution. Conceptual doubts (e.g. `print` vs `raise`) were explained; I applied the fix myself. Same approach with GitHub Copilot day-to-day: code review and questions that push my thinking, not finished implementations.
