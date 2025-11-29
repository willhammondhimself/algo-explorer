# Algo Explorer

## Team

Will Hammond, David Aguinada, Kai Yeung

## About

A PyQt5 app for visualizing data structures. We made this for our CSCI046 data structures and algorithms class because I (Will) kept getting confused by BST visualizations and pointer operations in the lecture slides. We wanted to actually *see* what happens step by step, so I built this visualizer. Turns out it helps a lot for understanding how the slow/fast pointer trick works for finding the middle of a linked list too.

## What It Does

- **Stack** - Push, pop, peek. Also has a recursive reverse function
- **Queue** - Basic FIFO queue, plus a challenge to implement it using two stacks
- **Linked List** - Insert/delete/search, with the slow/fast pointer algorithm for finding middle
- **BST** - Insert, delete (all three cases), search, and tree traversals

Everything draws on a canvas so you can see the operations happening. You can zoom/pan if the tree gets big.

## Running It

```bash
pip install -r requirements.txt
python main.py
```

You need Python 3.7+ and PyQt5.

## Tests

There are some unit tests in the `tests/` folder. Run them with:

```bash
pip install pytest
pytest
```

I tried to cover the main cases and edge cases for each data structure.

## Jupyter Notebooks

I also made some Jupyter notebooks in the `notebooks/` folder that walk through each data structure with examples and complexity explanations. They're useful if you want to play around with the code interactively.

```bash
pip install jupyter
jupyter notebook notebooks/
```

## Challenge Mode

Each data structure has a challenge problem:
- Stack: Reverse using recursion
- Queue: Implement queue with two stacks
- Linked List: Find middle in one pass
- BST: Build balanced tree from sorted array

Click "Start Challenge" in the app to try them.

## How It Works

The code is organized into:
- `data_structures/` - The actual stack, queue, linked list, and BST implementations
- `ui/` - PyQt5 interface stuff
- `visuals/` - Drawing logic for each data structure
- `challenges/` - Challenge mode logic
- `tests/` - Unit tests

I used the Command pattern for undo/redo (Ctrl+Z/Ctrl+Y work).

## Known Issues

- The zoom is kinda jumpy on trackpads sometimes
- Challenge mode button throws an error on first click (have to click twice) - **FIXED**
- Tree layout gets cramped if you insert like 20+ nodes
- Would be cool to add graph algorithms (Dijkstra, BFS) next

## Keyboard Shortcuts

- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+Q` - Quit

Built with Python and PyQt5 for CSCI046.
