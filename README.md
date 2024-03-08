# projectile-motion

This repository contains Python scripts to calculate various parameters related to projectile motion, such as velocity vector, position vector, time to reach maximum height, highest height reached, time to reach a given range, and range. The calculation is based on the initial velocity, launch angle, and initial height (if provided) of the projectile.
Files

    main.py: This script serves as the main entry point for the projectile motion calculator. It takes inputs from the command line arguments or prompts the user for input if no arguments are provided. Then, it calls the calc() function from function.py to perform the calculations and prints out the results.

    function.py: This file contains the calc() function, which performs the actual calculations related to projectile motion. It calculates the velocity vector, position vector, time to reach maximum height, highest height reached, time to reach a given range, and range based on the given inputs.

    angle.py: This script calculates the launch angle required to achieve a given range, taking into account the initial velocity and initial height (if provided). It computes the launch angle using trigonometric formulas and prints out the result.

    velocity.py: This script calculates the initial velocity required to achieve a given range at a specified angle. It computes the initial velocity based on the range and angle provided and prints out the result.

Usage:

    main.py: Run this script to calculate various parameters of projectile motion. You can either provide inputs as command-line arguments in the format [V0] [Launch angle] [Y0 (default is 0)] or input them when prompted if no arguments are provided.

    angle.py: Run this script to calculate the launch angle required to achieve a given range. Provide inputs as command-line arguments in the format [V0] [Range] [Y0 (default is 0)], or input them when prompted if no arguments are provided.

    velocity.py: Run this script to calculate the initial velocity required to achieve a given range at a specified angle. Provide inputs as command-line arguments in the format [Range] [angle] [Y0 (default is 0)], or input them when prompted if no arguments are provided.

Notes:

    All input values should be provided in appropriate units (e.g., velocity in m/s, angles in degrees).
    Make sure to have the necessary dependencies (e.g., SymPy) installed to run the scripts.
    Gravity is taken as 10 m/s^2.

Contributors:

    G00seboy

Feel free to modify and extend these scripts as needed for your specific use case. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
