#!/bin/bash

# # Check if ipmitool is installed
if ! command -v ipmitool &> /dev/null; then
    echo "ipmitool could not be found. Please install it first."
    exit 1
fi

# Check if gnuplot is installed
if ! command -v gnuplot &> /dev/null; then
    echo "gnuplot could not be found. Please install it first."
    exit 1
fi

# Initialize data file and HTML file
DATA_FILE="power_data.csv"
HTML_FILE="power_graph.html"
echo "Timestamp,Power" > $DATA_FILE

# Function to generate the HTML graph
generate_graph() {
    gnuplot -e "
        set datafile separator ',';
        set terminal canvas;
        set output '$HTML_FILE';
        set title 'Power Consumption Over Time';
        set xlabel 'Time (seconds)';
        set ylabel 'Power (Watts)';
        set xdata time;
        set timefmt '%s';
        set format x '%H:%M:%S';
        plot '$DATA_FILE' using 1:2 with lines title 'Power (W)';
    "
}

# Function to monitor power
monitor_power() {
    echo "Monitoring power consumption... (Press 'P' to generate graph or 'S' to stop)"
    while true; do
        # Get the instantaneous power consumption
        POWER=$(sudo ipmitool dcmi power reading)
        POWER_V=$(echo $POWER | awk -F'Instantaneous power reading: ' '{print $2}' | awk '{print $1}')
        TIMESTAMP=$(date +%s)

        # Append the timestamp and power to the data file
        echo "$TIMESTAMP,$POWER_V" >> $DATA_FILE

        # Check for user input
        read -t 1 -n 1 INPUT
        if [[ $INPUT == "P" ]]; then
            generate_graph
            echo "Graph generated: $HTML_FILE"
        elif [[ $INPUT == "S" ]]; then
            echo "Stopping monitoring..."
            break
        fi
    done
}

# Start monitoring
monitor_power
# generate_graph

# Print the directory where files are stored
echo "Power data saved in: $(pwd)"
