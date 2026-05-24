# 🐍 Python Snake Game (with Greedy AI Mode)

An extended version of the classic arcade Snake game built using Python's `turtle` library. This project builds upon the foundation from Angela Yu's "100 Days of Code" by adding an automated **AI Mode** that uses a greedy search algorithm to hunt down food efficiently.

---

## 🚀 Features

* **Manual Mode**: Play manually using standard arrow key controls.
* **Greedy AI Mode**: An automated pathfinding algorithm that calculates the shortest path to food at each step using a greedy search method.
* **Real-time Score Tracking**: Keeps score and updates live during gameplay.
* **Collision Detection**: Full game-over logic for wall impacts and self-collisions.
* **Object-Oriented Design**: Clean modular structure split into dedicated classes.

---

## 🛠️ Tech Stack & Concepts Used

* **Language**: Python 3
* **Graphics Library**: `turtle` (built-in GUI toolkit)
* **Algorithms**: Greedy Search (Pathfinding / Goal Tracking)
* **Object-Oriented Programming (OOP)**: Class inheritance, encapsulation, and clear separation of concerns.

---

## 📂 Project Structure

* `main.py`: Main execution loop, screen refresh rules, and switching logic between player and AI modes.
* `snake.py`: Controls snake rendering, directional constraints, and segments. Contains pathfinding hooks for the AI.
* `food.py`: Handles randomized coordinate spawning for food targets.
* `scoreboard.py`: Manages UI rendering, text overlays, and game-over updates.

---

## 💻 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com
   ```
2. **Navigate to the directory**:
   ```bash
   cd PythonProject1
   ```
3. **Run the game**:
   ```bash
   python main.py
   ```
<img width="898" height="948" alt="Screenshot 2026-05-24 152431" src="https://github.com/user-attachments/assets/d5bf2803-1c8d-4e38-a5fa-136821d79380" />
