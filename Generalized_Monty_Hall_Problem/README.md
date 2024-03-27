# Generalized Monty Hall Problem

### Team
- Animesh Madaan
- Arush Upadhyaya
- Sankalp Mittal
- Maharaajan J
- Wattamwar Akanksha Balaji

### Instructions
This is a source code written in `python`. This can be run on any machine having a python interpreter installed. 

Ensure that the aforementioned interpreter is added to `PATH`

- Go to the directory in which the code is saved 
- Install the requirements
```bash 
pip install -r requirements.txt
```
- Run the following command in the *terminal* 
```bash
python monty.py
```
A surface plot of $n$, $k$ versus $\frac{P(win | W)}{P(win | T)}$ is displayed, where $n$ is the number of doors and $k$ is the number of cars. $W$ denotes switching whereas $T$ denoted sticking. 

### Logic

Here, the probability $P(win | W)$ is calculated as follows -
$$P(win | W) = P(C) * P(win | W | C) + P( \overline{C} ) * P(win | W | \overline{C})$$
$$P(win | W) = \frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}$$
where $C$ denoted the event of choosing a door with car behind it before switching.

The probability $P(win | T)$ can be calculated trivially as follows -
$$P(win | T) = P(C) = \frac{k}{n}$$

Therefore,
$$\frac{P(win | W)}{P(win | T)} = \frac{\frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}}{\frac{k}{n}}$$
$$\frac{P(win | W)}{P(win | T)} = \frac{n - 1}{n - 2}$$