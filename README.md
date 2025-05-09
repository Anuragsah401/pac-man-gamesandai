# 🕹️ Pac-Man with AI Ghost (KOL304CR CW3)

This is a simple Pac-Man-inspired game implemented in Python using Pygame, developed as part of the **KOL304CR Games and AI** coursework. The game features basic player controls and an AI-controlled ghost using the **A* (A-star)** pathfinding algorithm to chase the player through a maze.

## 🎮 Gameplay Overview

- Use arrow keys to control the yellow Pac-Man character.
- Collect dots to increase your score.
- Avoid the red ghost that actively chases you using A* pathfinding.
- Collision with the ghost ends the game.

## 🧠 AI Techniques

This game implements a **real-time pathfinding AI** using the A* algorithm, which:
- Calculates the shortest path from the ghost to the player.
- Avoids walls using maze constraints.
- Recalculates the path dynamically as the player moves.

### A* Logic Highlights:
- **Heuristic**: Manhattan Distance.
- **Search Space**: Grid-based map defined in `maze.py`.
- **Execution**: Recomputed each time the ghost reaches a new tile or loses path.

Refer to [`ghost.py`](./ghost.py) for the A* implementation details.

## 📁 Project Structure

.
├── main.py # Game loop, rendering, event handling
├── player.py # Player input, movement, scoring
├── ghost.py # Ghost class and A* pathfinding
├── maze.py # Maze layout, dot tracking, collision constraints
├── settings.py # Game constants (colors, size, FPS)
├── video/ # Folder to store gameplay demo 


## ▶️ Demo Video

A 2-minute gameplay video is available in the `video/` folder and also accessible via:  
🔗 https://github.com/Anuragsah401/pac-man-gamesandai

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `pygame` module

### Installation

1. Clone the repo (ensure private access is granted to module lead):
   ```bash
   git clone https://github.com/Anuragsah401/pac-man-gamesandai
   cd pac-man-gamesandai

Install dependencies:

##bash

pip install pygame
Run the game:

##bash
python main.py
