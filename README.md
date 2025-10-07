# Compatibility Optimizer

This repository implements an AI-based optimization algorithm for solving a group compatibility problem.  
The program reads a matrix of pairwise compatibility scores from an Excel sheet and applies a **random hill climbing** approach to find the combination of pairings that maximizes the overall compatibility score.

---

## Overview

The goal of the project is to generate an optimal set of pairings from a set of individuals, each with compatibility scores toward every other participant.  
This problem is equivalent to a **combinatorial optimization** task, where the objective is to maximize the sum of selected compatibility values under pairing constraints.

The implemented solution leverages **randomized search** and **hill climbing heuristics** to iteratively improve candidate solutions based on local fitness evaluations.

---

## Methodology

The optimizer begins with a random pairing configuration and repeatedly performs local swaps or adjustments to improve the total compatibility score.  
The process continues until either a maximum iteration threshold or a stagnation limit is reached.

### Key features
- **Stochastic initialization** – starts from a random feasible solution  
- **Random hill climbing** – explores neighboring solutions by pair swapping and retains only improvements to a depth  
- **Fitness evaluation** – total compatibility score is recalculated at each step to avoid local maxima's  
- **Convergence criteria** – stops after a defined number of iterations without improvement  

The algorithm’s accuracy relative to the theoretical optimal score (4949) is reported as:

```python
round((best_score / 4949) * 100, 1)
```

This produces a percentage accuracy rounded to one decimal place.

---

## Dependencies

The project uses the following Python modules:

- `random` – for generating random initial configurations and probabilistic moves  
- `pandas` – for reading and processing the input Excel sheet (`compatibility_input.xlsx`)  
- `openpyxl` – used by pandas as the engine to read `.xlsx` files  

Standard libraries like `os` are not required in the current implementation and may be removed if unused.

To install dependencies:
```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:
```
pandas>=2.0
openpyxl>=3.1
```

---

## File Structure

```
compatibility-optimizer/
├── compatibility_optimizer.py      # Main hill climbing solver
├── compatibility_input.xlsx        # Input data file with compatibility matrix
├── requirements.txt                # Dependency list
└── README.md                       # Project documentation
```

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/ariadruker1/compatibility-optimizer.git
   cd compatibility-optimizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the optimizer**
   ```bash
   python compatibility_optimizer.py
   ```

4. **View results**  
   The program will print output similar to:
   ```
   Best total compatibility: 4700 is 95.0% accurate towards the optimal solution
   ```

---

## Input Format

The Excel file `compatibility_input.xlsx` should contain a symmetric matrix of pairwise compatibility scores, where:
- Each row and column corresponds to a participant.
- Diagonal entries (self-scores) may be zero or omitted.
- All non-diagonal entries represent compatibility between distinct pairs.

Example:

|   | A | B | C |
|---|---|---|---|
| A | 0 | 78 | 62 |
| B | 78 | 0 | 81 |
| C | 62 | 81 | 0 |

---

## Theory and Approach

This problem belongs to the class of **NP-hard combinatorial optimization** tasks.  
A brute-force search for all possible pairings scales factorially with the number of participants and is computationally infeasible for large datasets.  

To manage complexity, this implementation uses **random hill climbing**, a local search algorithm that:
1. Starts from a random solution.  
2. Evaluates the total compatibility (fitness).  
3. Randomly alters the configuration to form a “neighboring” state.  
4. Accepts the change only if it improves the fitness score.  
5. Repeats until no significant improvement occurs.

While hill climbing cannot guarantee finding the global optimum, it provides a strong approximation within a fraction of the computation time, making it suitable for practical matching and scheduling problems.

---

## Future Extensions

Potential future improvements include:
- Implementing **simulated annealing** or **genetic algorithms** for improved global optimization.  
- Introducing **parallel optimization** for large participant sets.  
- Integrating **visualization tools** to show convergence and score progression.  
- Allowing dynamic benchmark calculation instead of the fixed value (4949).  
- Enabling user-defined constraints or categorical balancing within pairings.
