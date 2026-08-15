# CLI Number Guessing Game

A modular, interactive number guessing game built in Python. Features customizable difficulty boundaries, conditional feedback loops, and session replay management.

## Technical Highlights

* **Dynamic Difficulty Range:** Allows the user to specify an upper limit ($1 \le x \le N$), generating pseudo-random target integers dynamically via `random.randint()`.
* **State-Driven Feedback Loop:** Utilizes a `while True` control loop comparing user inputs against the target number to provide immediate directional hints (`Too low!` or `Too high!`).
* **Modular Function Architecture:** Organized into isolated procedural functions (`display_the_heading`, `play_game`, `main`) to enforce clean separation of responsibilities.
* **Boolean Session Management:** Leverages boolean return evaluations (`play_again == 'y'`) to smoothly control game replay cycles or trigger terminal exit states.

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (uses built-in `random` module—zero external `pip` dependencies required).

## Usage

```bash
python main.py
