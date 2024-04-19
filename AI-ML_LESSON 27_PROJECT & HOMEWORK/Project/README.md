Shopping List Analysis using Association Rule Mining
This project analyzes shopping lists and discovers associations between items commonly bought together using association rule mining.
Overview
Association rule mining is a technique used in data mining to discover interesting relationships or associations between variables in large datasets. In the context of shopping list analysis, association rule mining helps identify patterns in customer purchasing behavior.
Tools and Libraries Used
Python: Programming language used for implementing the project.
pandas: Python library for data manipulation and analysis.
extend: Python library for machine learning extensions, including implementations of association rule mining algorithms.
Installation
Clone the repository to your local machine:
git clone <repository_url>
Navigate to the project directory:
cd Install the required Python libraries:

Usage
Prepare your shopping list data in CSV format. Each row should represent a transaction (shopping basket), and each column should represent an item. The values can be binary (1 for present, 0 for absent).Example:
Milk, Bread, Butter
Bread, Eggs, Cheese
Milk, Bread, Eggs


Run the shopping_list_analysis.py script:
python shopping_list_analysis.py
View the discovered association rules printed on the console.
Customization
You can adjust the parameters such as min_support and min_threshold in the shopping_list_analysis.py script to customize the analysis according to your preferences.
Feel free to modify the input data or extend the project with additional features as needed.
