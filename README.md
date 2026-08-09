# Estoque T.I.

A terminal-based IT inventory management system, built with Python (OOP) and SQLAlchemy, persisted in SQLite.

## Where this came from

I'm a Systems Analysis and Development student and an IT intern. This project started as practice for a Python + OOP + SQLAlchemy course, but instead of leaving it as a disconnected exercise, I pointed it at a real problem: my workplace's IT inventory had no structured tracking, just loose spreadsheets. So the project became both a study tool and something I plan to actually use at work.

## Why it's scoped the way it is

This isn't meant to be a commercial or generic inventory system. The scope is intentionally minimal for this phase — no movement history, no supplier data, no cost tracking — just correct, validated CRUD on `Item` and `ItemHardware`. Hardware is only the first category modeled this way; more category classes are planned as the project grows.

## What's done

- **Register items** — category, name, quantity, and status (`Lixo` / `Funcionando` / `Conserto`), with full input validation (no empty fields, status must match one of the three options, quantity must be a positive integer)
- **List items** — filter by all items or by hardware category specifically
- **Adjust stock** — increase or decrease quantity, with guards against negative numbers and against removing more than what's in stock
- **Delete an item**
- **ItemHardware** — a 1:1 relationship to `Item` via a shared primary key/foreign key (`item_id`), so hardware-specific items don't duplicate the base item's data
- **Error handling throughout** — every database operation is wrapped in `try/except`, with rollback on failure; the program never crashes, it always returns a clear message and goes back to the menu
- **Proper entry point** (`if __name__ == "__main__"`) and a pinned `requirements.txt` for reproducible installs
- **No machine-specific files tracked** — a personal Windows shortcut script was removed from the repo, since it hardcoded a local path and had no value for anyone else cloning the project

## Tech stack

- Python
- SQLAlchemy (ORM)
- SQLite

## Running it

```bash
git clone https://github.com/douglaskevin201/estoque-t.i
cd estoque-t.i

pip install -r requirements.txt

python menu.py
```

The database (`estoque.db`) is created automatically on first run.

## Technical decisions

Some choices came from real problems found during development, not decisions made upfront:

- **IDs are not reused after deletion** — deleting an item doesn't reclaim its ID for the next entry; the sequence keeps moving forward. This is SQLite/SQLAlchemy's default behavior, kept intentionally to avoid ambiguity if other tables ever reference these IDs.
- **`models.py` and `menu.py` are separate** — business logic and data classes are isolated from the user-interaction layer, for easier maintenance and future expansion.
- **No API yet, on purpose** — kept to plain Python + SQLAlchemy for this phase, to consolidate those concepts before introducing an API layer.

## Roadmap

1. ✅ Core data model (`Item`, `ItemHardware`) with SQLAlchemy
2. ✅ Full CRUD with validation and error handling
3. ✅ List filtering (all items / hardware only)
4. ✅ Pinned dependencies (`requirements.txt`) and proper entry point
5. ⬜ Additional category classes beyond `ItemHardware` (following the same 1:1 relationship pattern)
6. ⬜ API layer to host the database elsewhere
7. ⬜ Broader search (by name, by status, not just hardware filter)
8. ⬜ Application/interface layer for real day-to-day use at work
9. ⬜ Move off the local `.bat` shortcut toward a proper install/run flow

## On AI usage

Claude was used as a study aid throughout the project, with a deliberately limited role: reviewing code I wrote myself, pointing out real bugs, logic that didn't behave as expected, and redundant code — never writing the finished solution for me. When I had a conceptual doubt (e.g. `print` vs `raise`, or why use `try/except`), it explained the reasoning, and I applied the fix myself.

I asked for the same guided-help format from other AI tools used day-to-day, like GitHub Copilot: code review and questions that push my thinking, never the final implementation handed to me.
