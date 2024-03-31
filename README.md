# Subject to Grade Correlation
The correlation between the grade of one subject(s), to the grade of other subject(s).

## Important notes
- All the report cards (in the `report_cards` directory) are all fake and were generated by ChatGPT
- If you want to use this project with a report card of another format, you will have to modify the `report_cards.main()` function (in `report_cards.py`).
- If you run the `analyze.py` script directly (not as an import), the script will generate an excel spreadsheet file called `correlation_results.xlsx`.

## Setup
- Install required dependencies: `pip3 install -r requirements.txt`

## Run
Run the main script: `python3 main.py`
The main script will first run the `report_cards.main()` function, which will extract all the grades from the pdf report cards (in the `report_cards` directory), and store them in json files.
And then it will run a heatmap and network nodes to visualize the correlation coefficient of the subjects.

## License
This project is under the GPL-3.0 license. Read more [here](LICENSE).