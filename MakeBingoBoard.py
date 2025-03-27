import random
from Npp import *

# Parameters
GRID_SIZE = 5  # 5x5 bingo board

# Get all non-empty lines from the current editor
editor.beginUndoAction()
lines = [line.strip() for line in editor.getText().splitlines() if line.strip()]
editor.endUndoAction()

# Total squares needed
total_cells = GRID_SIZE * GRID_SIZE

# If the grid has a center and is odd-sized, subtract one for the free space
has_free_space = GRID_SIZE % 2 == 1
if has_free_space:
    total_cells -= 1

# Pad lines with empty strings if not enough
lines += [''] * (total_cells - len(lines))
random.shuffle(lines)

# Insert FREE SPACE into the middle
if has_free_space:
    middle_index = (GRID_SIZE // 2) * GRID_SIZE + (GRID_SIZE // 2)
    lines.insert(middle_index, "FREE SPACE")

# Generate the board as text
board_lines = []
for i in range(GRID_SIZE):
    row = lines[i * GRID_SIZE:(i + 1) * GRID_SIZE]
    board_lines.append(" | ".join("{:^20}".format(cell) for cell in row))
    board_lines.append("-" * (GRID_SIZE * 23))

# Replace the document text
editor.setText("\n".join(board_lines))
