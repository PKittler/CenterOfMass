# CenterOfMass
Tool to find the center of mass in a 3-axis-system to analyze the structure and concentration of groups.

## ToDos
- Page: All Cases Overview
- Page: Add Case
- Page: Edit Case
- Page: Single Case Overview
- Page: Add Point
- Page: Edit Point
- Page: COM Model
- Function: (All Cases Overview) Delete Case
- Function: (Add Case) Save Case
- Function: (Add Case) Cancel
- Function: (Edit Case) Save Case
- Function: (Edit Case) Cancel
- Function: (Add Point) Save Point
- Function: (Add Point) Cancel
- Function: (Edit Point) Save Point
- Function: (Edit Point) Cancel
- Function: (Single Case Overview) Delete Point

## Software Structure
- Django
- xeogl
- Calculations for center of mass

## Center of Mass
The position of the center of mass is declared by a vector r.

r = (r_1 * m_1 + r_2 * m_2 + ... + r_n * m_n) / m
