#!/bin/bash

# Directory containing the CSV files
DIRECTORY="./"  # Change this to your directory containing CSV files
OUTPUT_FILE_NODES="power_consumption_nodes.png"
OUTPUT_FILE_AGGREGATE="cluster_aggregate_power_consumption.png"
DATA_FILE_NODES="nodes_data.csv"
DATA_FILE_AGGREGATE="aggregate_data.csv"

WORKER1="68_power_data.csv"
WORKER2="171_power_data.csv"
OUTPUT_WORKER1="68_power_data.png"
OUTPUT_WORKER2="171_power_data.png"

####  Data file processing

process_data(){
    # Check if the directory exists
    if [ ! -d "$DIRECTORY" ]; then
        echo "Directory $DIRECTORY does not exist."
        exit 1
    fi

    # Initialize the data files
    echo "Timestamp,Power,Hostname" > $DATA_FILE_NODES
    echo "Timestamp,AggregatePower" > $DATA_FILE_AGGREGATE

    # Loop through each CSV file in the directory to read the data
    for file in "$DIRECTORY"/*.csv; do
        # Extract hostname from the filename if needed or read from the file
        while IFS=',' read -r TIMESTAMP POWER HOSTNAME; do
            # Skip the header row
            if [[ "$TIMESTAMP" != "Timestamp" ]]; then
                # Append node-specific data
                echo "$TIMESTAMP,$POWER,$HOSTNAME" >> $DATA_FILE_NODES
                
                # Add to aggregate power consumption
                if ! grep -q "$TIMESTAMP" $DATA_FILE_AGGREGATE; then
                    echo "$TIMESTAMP,$POWER" >> $DATA_FILE_AGGREGATE
                else
                    # Update aggregate power
                    awk -v ts="$TIMESTAMP" -v power="$POWER" 'BEGIN {FS=OFS=","} $1 == ts {$2 += power} 1' $DATA_FILE_AGGREGATE > temp && mv temp $DATA_FILE_AGGREGATE
                fi
            fi
        done < "$file"
    done

}



####  Instantaneous power consumption of all nodes over the time
node_power_comparison(){
    gnuplot -e "
        set datafile separator ',';
        set terminal png;
        set title 'Power Consumption Over Time';
        set xlabel 'Time (seconds)';
        set ylabel 'Power (Watts)';
        set xdata time;
        set timefmt '%s';
        set output '$OUTPUT_FILE_NODES';
        set timefmt '%s';
        set format x '%H:%M:%S';
        set key outside;
        set style line 1 linecolor rgb 'red' lw 2;
        set style line 2 linecolor rgb 'blue' lw 2;
        plot 'nodes_data.csv' using 1:2 with linespoints linestyle 1 title 'kube-worker-171', '' using 1:2 with linespoints linestyle 2 title 'kube-worker-68';
    "
    echo "File created"

}
####  Instantaneous power consumption of the node over the time
node_power() {
    gnuplot -e "
        set datafile separator ',';
        set terminal png size 1000,800;
        set title 'Power Consumption kube-worker-68';
        set xlabel 'Time (seconds)';
        set ylabel 'Power (Watts)';
        set xdata time;
        set timefmt '%s';
        set output '$OUTPUT_WORKER1';
        set timefmt '%s';
        set format x '%H:%M';
        plot '$WORKER1'using 1:2 with lines title 'Power (W)';
    "
    echo "File $OUTPUT_WORKER1 created"

    gnuplot -e "
        set datafile separator ',';
        set terminal png size 1000,800;
        set title 'Power Consumption - kube-worker-171';
        set xlabel 'Time (seconds)';
        set ylabel 'Power (Watts)';
        set xdata time;
        set timefmt '%s';
        set output '$OUTPUT_WORKER2';
        set timefmt '%s';
        set format x '%H:%M';
        plot '$WORKER2'using 1:2 with lines title 'Power (W)';
    "
    echo "File $OUTPUT_WORKER2 created"
}

####  Aggregated instantaneous power consumption of the cluster over the time

aggregate_power() {
    gnuplot -e "
        set datafile separator ',';
        set terminal png size 1000,800;
        set title 'Power Consumption Over Time';
        set xlabel 'Time (seconds)';
        set ylabel 'Power (Watts)';
        set xdata time;
        set timefmt '%s';
        set output '$OUTPUT_FILE_AGGREGATE';
        set timefmt '%s';
        set format x '%H:%M';
        plot '$DATA_FILE_AGGREGATE' using 1:2 title 'Power';
    "
    echo "File created"
}
node_power
aggregate_power
