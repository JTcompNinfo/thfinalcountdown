# Quest for the Lost Artifact: A Text-Based Adventure Game
## Python Programming Project - 12th Grade Computer Science

---

## PROJECT DESCRIPTION

You will create an immersive text-based adventure game where players navigate through different locations, collect items, interact with characters, make decisions that affect the story, and ultimately complete a quest. This project synthesizes all the Python skills you've learned this semester into one cohesive application.

---

## GAME REQUIREMENTS

### Core Features (Required)

#### 1. Game World Structure
- Minimum of 8 distinct locations players can visit
- Each location must have a unique description
- Locations connected in a logical map (players can move between them)
- At least one location must be "locked" and require an item or condition to access

#### 2. Player System
- Player has a name (collected at game start)
- Health points system (player can take damage and heal)
- Inventory system to collect and use items
- Player statistics tracking (items collected, locations visited, etc.)

#### 3. Inventory Management
- Players can pick up, drop, and use items
- Minimum of 6 different items in the game world
- Some items must be required to progress in the game
- Display inventory command that shows current items

#### 4. Interactive Characters (NPCs)
- Minimum of 4 non-player characters
- Characters provide information, quests, or items
- At least one character must require an item trade
- Dialogue system for character interactions

#### 5. Combat or Challenge System
- At least 3 encounters where player must make choices
- Consequences for different choices (health loss, item gain, story branching)
- At least one "puzzle" that requires specific items or knowledge

#### 6. Game State Management
- Track completed quests or objectives
- Win condition (how to complete the game)
- Lose condition (game over scenario)
- Game statistics displayed at end

#### 7. Commands System
- Movement commands (north, south, east, west, etc.)
- Action commands (take, use, talk, examine, etc.)
- System commands (inventory, help, stats, quit)
- Invalid command handling with helpful feedback

---

## TECHNICAL REQUIREMENTS

### 1. Variables and Data Types
- Use strings for text, descriptions, and names
- Use integers for health, damage, scores
- Use floats if incorporating any decimal values (optional)
- Use booleans for game states and conditions

### 2. Data Structures
- **Dictionary** for storing location information
- **Dictionary** for storing item information
- **List** for player inventory
- **Dictionary** or **List** for NPC information
- **Tuple** for coordinate systems or immutable data (optional but encouraged)

### 3. Control Structures
- Branching (if/elif/else) for decision-making and game logic
- While loop for main game loop
- For loops for iterating through items, locations, or displaying information

### 4. Functions
- Minimum of 8 custom functions
- Function for displaying location descriptions
- Function for processing player commands
- Function for combat/challenge encounters
- Function for inventory management
- Function for NPC interactions
- Function for win/lose conditions
- Use the main() function pattern

### 5. String Manipulation
- Format output with proper spacing and presentation
- Parse user input (handle uppercase/lowercase, extra spaces)
- String concatenation for dynamic messages
- Multi-line strings for descriptions

---

## BONUS FEATURES (Optional - Extra Credit)

- Save/load game functionality using file operations
- Random events or encounters
- Consumable items (food, potions) that affect stats
- Day/night cycle or time-based events
- Multiple endings based on player choices
- ASCII art for locations or items
- Color-coded text output (using simple ANSI codes)
- Hidden secrets or Easter eggs
- Difficulty levels

---

## STORY SUGGESTIONS

Your game needs a compelling narrative. Here are some themes (choose one or create your own):

1. **Fantasy Quest** - Retrieve a magical artifact from an ancient dungeon
2. **Mystery Investigation** - Solve a crime by gathering clues in a mansion
3. **Space Exploration** - Repair your spaceship and escape an alien planet
4. **Zombie Survival** - Gather supplies and find survivors in an apocalypse
5. **Time Travel Adventure** - Fix timeline disruptions across different eras
6. **Underwater Discovery** - Explore a sunken city searching for treasure

---

## PROJECT TIMELINE

- **Week 1-2:** Design game world, write story outline, plan data structures
- **Week 3-4:** Implement basic location system and navigation
- **Week 5-6:** Add inventory system and items
- **Week 7-8:** Implement NPCs and dialogue system
- **Week 9-10:** Add combat/challenge system and game logic
- **Week 11-12:** Testing, debugging, polishing, and documentation

---

## DELIVERABLES

### 1. Game Design Document (submit by end of Week 2)
- Story overview and objectives
- Map of locations with connections
- List of all items and their purposes
- List of all NPCs and their roles
- Flowchart of major game decisions

### 2. Python Source Code (final submission)
- Single .py file or organized multiple files
- Comprehensive comments explaining code sections
- Proper function documentation
- Clean, readable code with consistent naming conventions

### 3. README File
- How to run the game
- List of all available commands
- Brief walkthrough or hints
- Known bugs or limitations

### 4. Playthrough Video or Written Documentation (optional but recommended)
- Demonstrate all major features
- Show win condition
- Highlight bonus features if implemented

---

## CODE STYLE REQUIREMENTS

- Use descriptive variable names (no single letters except loop counters)
- Include comments for complex logic sections
- Consistent indentation (4 spaces)
- Function names use lowercase with underscores (snake_case)
- Constants in UPPERCASE
- Organize code with functions, don't put everything in main()

---

## TESTING CHECKLIST

Before submitting, verify:

- [ ] Game starts without errors
- [ ] All commands work as expected
- [ ] Invalid commands are handled gracefully
- [ ] Player can navigate to all locations
- [ ] All items can be collected and used
- [ ] NPCs respond appropriately
- [ ] Win condition can be achieved
- [ ] Lose condition works properly
- [ ] Game provides clear instructions to player
- [ ] No infinite loops or crashes

---

## GRADING

This project is worth 200 points and will be graded on:

- **Game Design and Planning** (20 points)
- **Core Game Structure** (40 points)
- **Data Structures** (30 points)
- **Game Features** (50 points)
- **Functions** (25 points)
- **Control Structures** (20 points)
- **Code Quality** (15 points)
- **Bonus Features** (up to 20 extra points)

See the detailed grading rubric for specific criteria.

---

## ACADEMIC INTEGRITY

This is an individual project. While you may discuss general concepts with classmates, all code must be your own work. Using code from the internet, AI tools, or other students without proper attribution constitutes plagiarism and will result in a zero on the project.

---

## GETTING HELP

- Attend office hours for one-on-one assistance
- Use the class discussion board for general questions
- Review the lesson plans and example code provided
- Start early so you have time to work through challenges

---

**Good luck, and have fun creating your adventure game!**
