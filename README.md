# 🐉 Monster Fight

A fun text-based battle game built with Python where you fight a monster — attack or heal your way to victory!

---

## 🎮 How to Play

1. Run the game
2. Choose your action each turn:
   - Type `attack` — deal damage to the monster
   - Type `heal` — restore your own health
3. The monster fights back every turn automatically
4. Win by reducing the monster's health to 0 before yours runs out!

---

## ⚔️ Game Features

- 🎲 **Random damage system** — every attack and heal is randomized
- ⏱️ **Dramatic delays** — output appears line by line for a cinematic feel
- 💚 **Health tracking** — your health and monster health displayed after every round
- 🏆 **Win/Lose conditions** — see if you can defeat the monster!

---

## 🧮 Game Stats

| Stat | Range |
|------|-------|
| Player starting health | 100 |
| Monster starting health | 100 |
| Player attack damage | 10 – 20 |
| Player heal amount | 10 – 20 |
| Monster attack damage | 15 – 25 |

> ⚠️ The monster hits harder than you — choose wisely when to heal!

---

## 🚀 How to Run

### Requirements
- Python 3.x

### Steps

```bash
# Clone the repository
git clone https://github.com/mrabulhasnainkhan-collab/Monster_Fight.git

# Navigate into the folder
cd Monster_Fight

# Run the game
python Monster_Fight.py
```

---

## 📁 Project Structure

```
Monster_Game/
│
├── Monster_Fight.py             # Main game file
└── README.md                    # Project documentation
```

---

## 🖥️ Sample Output

```
WELCOME! WELCOME!
TO THE
MONSTER FIGHT!!!

What you wanna choose do you want to (attack) or (heal)? attack

Don't be Scared
You dealt 17 damage to the monster!
Ohhh Nooo
The monster dealt 21 damage to you!

Your health: 79, Monster's health: 83
The fight is still on!!
```

---

## 🛠️ Built With

- **Python 3** — core language
- **random** module — for randomized damage/heal values
- **time** module — for dramatic output delays

---

## 👨‍💻 Author

**Abul Hasnain Khan**  
GitHub: [@mrabulhasnainkhan-collab](https://github.com/mrabulhasnainkhan-collab)

---

## 📜 License

This project is open source and available for learning purposes.
