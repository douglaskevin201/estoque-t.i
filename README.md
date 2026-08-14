# Estoque T.I.

Terminal-based IT inventory management system, built with Python (OOP) and SQLAlchemy, persisted in SQLite.

## Where this came from

Practice project for a Python + OOP + SQLAlchemy course, pointed at a real problem: my workplace had no IT inventory control at all. It's both a study tool and something I plan to use at work.

## Scope

Intentionally minimal for this phase — no movement history, no supplier data, no cost tracking. Just correct, validated CRUD on `Item`, with category-specific subclasses where the extra data justifies a separate table.

## What's done

- Register items — category, name, quantity, status (Lixo / Funcionando / Conserto), full input validation
- Six categories modeled: `ItemHardware`, `ItemPeriferico`, `ItemComputador` (Desktop/Notebook, with sector and responsible user), `ItemProjetor` (model), `ItemAcessorio` — each a 1:1 relationship to `Item` via shared PK/FK (`item_id`), created only where it holds attributes `Item` doesn't
- List items — dynamic category filter, built from `.distinct()` on existing data (no hardcoded per-category branches)
- Trash view (Lixeira) — quick list of items with status `LIXO`, separate from the general listing
- Adjust stock — increase/decrease with guards against negative numbers and over-removal
- Delete an item — subclass rows are cleaned up automatically via `cascade="all, delete-orphan"`, no orphaned data left behind
- Registration writes the `Item` and its subclass in a single transaction (subclass objects are attached through the SQLAlchemy relationship, not a manual `item_id`), so a failure partway through never leaves an incomplete record
- Error handling throughout — every DB operation wrapped in try/except with rollback; the program never crashes
- Proper entry point (`if __name__ == "__main__"`, with `try/finally` to guarantee session closure) and pinned `requirements.txt`
- No machine-specific files tracked (removed a hardcoded local shortcut script)

## Tech stack

Python, SQLAlchemy (ORM), SQLite

## Running it

git clone https://github.com/douglaskevin201/estoque-t.i
cd estoque-t.i
pip install -r requirements.txt
python menu.py
The database (`estoque.db`) is created automatically on first run.

## Technical decisions

- **A category only gets its own subclass/table when it needs extra fields** — `ItemComputador` and `ItemProjetor` exist because they hold data (`setor`, `responsavel`, `modelo`) that `Item` doesn't; `ItemHardware`, `ItemPeriferico` and `ItemAcessorio` are intentionally empty, existing only to anchor the relationship for category filtering — no attribute duplication either way.
- **Subclass rows are attached via `relationship`, not a manual `item_id`** — lets a single `session.commit()` persist the `Item` and its subclass atomically, instead of two separate commits that could leave one without the other.
- **`cascade="all, delete-orphan"` on every `Item` → subclass relationship** — SQLite doesn't enforce foreign keys by default, so without this a deleted `Item` would leave its subclass row orphaned in the database.
- **IDs aren't reused after deletion** — SQLite/SQLAlchemy's default; kept intentionally in case other tables reference these IDs later.
- **`models.py` and `menu.py` are separate** — business logic and data classes isolated from the interaction layer.
- **No API yet, on purpose** — consolidating Python + SQLAlchemy fundamentals before adding one.

## Roadmap

- [x] Core data model (Item + category subclasses) with SQLAlchemy
- [x] Full CRUD with validation and error handling
- [x] Additional category classes beyond ItemHardware
- [x] Dynamic list filtering by category
- [x] Trash/discarded items view
- [x] Atomic registration (single commit) and cascade delete for subclass rows
- [x] Pinned dependencies and proper entry point
- [ ] API layer to host the database elsewhere
- [ ] Broader search (by name, by status)
- [ ] Application/interface layer for daily use at work
- [ ] Proper install/run flow, off the local .bat shortcut

## On AI usage

Claude was used as a study aid, with a limited role: reviewing code I wrote, pointing out bugs and redundant logic — never writing the solution. Conceptual doubts (e.g. `print` vs `raise`, SQLAlchemy relationships) were explained; I applied the fix myself. Same approach with GitHub Copilot day-to-day: code review and questions that push my thinking, not finished implementations.
